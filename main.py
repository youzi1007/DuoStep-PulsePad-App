from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot, QTimer
from pyo import Server
import serial
import time
import os

# Import the generated UI class
from ui_main_window import Ui_MainWindow
from note_playback import NotePlayback

class DuoStepApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Initialize Pyo server
        self.server = Server(sr=44100, buffersize=1024, duplex=0)
        self.server.boot()
        self.server.start()
        print("Pyo server started with output.")

        # UI elements to methods
        self.masterVol.valueChanged.connect(self.update_master_volume)
        self.pianoVol.valueChanged.connect(self.update_piano_volume)
        self.clarinetVol.valueChanged.connect(self.update_clarinet_volume)
        self.recordButton.clicked.connect(self.start_recording)
        self.stopButton.clicked.connect(self.stop_recording)

        # Arduino
        self.arduino = serial.Serial('COM4', 9600)
        time.sleep(2)  # Wait for Arduino to initialize

        # Set up directories for samples
        BASE_DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
        SAMPLES_DIR = os.path.join(BASE_DIR, "Resources", "piano", "samples24bit")

        # Initialize NotePlayback
        self.note_playback = NotePlayback(SAMPLES_DIR)

        # Setup timer for Arduino input handling
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_arduino_input)
        self.timer.start(50)  # Check every 50ms

        # UI configurations
        self.populate_note_octave_options()
        self.masterLibraryComboBox.currentIndexChanged.connect(self.update_note_range)

        # ComboBox: note and octave selections
        self.startingNote.currentIndexChanged.connect(self.update_note_assignment)
        self.startingOct.currentIndexChanged.connect(self.update_note_assignment)
        self.midi_values=[]

        # Initialize NotePlayback
        self.note_playback = NotePlayback(SAMPLES_DIR)



        # Connect all checkboxes to the toggle method
        self.checkboxes = [
            self.L1u, self.L1d, self.L2u, self.L2d, self.L3u, self.L3d, self.L4u, self.L4d, self.L5u, self.L5d,
            self.R1u, self.R1d, self.R2u, self.R2d, self.R3u, self.R3d, self.R4u, self.R4d, self.R5u, self.R5d
        ]
        self.setup_checkboxes()

    def handle_arduino_input(self):
        if self.arduino.in_waiting > 0:
            data = self.arduino.readline().decode().strip()
            print(f"Received from Arduino: {data}")
            try:
                fsr_number, velocity, action = map(int, data.split(','))

                # Validate FSR number and map it to the corresponding MIDI note
                if 1 <= fsr_number <= 20:
                    note_index = fsr_number - 1  # FSRs are 1-indexed, so subtract 1 for 0-indexed list

                    if note_index < len(self.midi_values):
                        note = self.midi_values[note_index]

                        # Check if the corresponding checkbox is checked (enabled)
                        if self.checkboxes[note_index].isChecked():
                            if action == 1:  # Start note
                                self.note_playback.start_note_playback(note, velocity)
                            elif action == 0:  # Stop note
                                self.note_playback.stop_note_playback(note)
                        else:
                            print(f"Note {note} is disabled and will not produce sound.")
                    else:
                        print(f"FSR number {fsr_number} is out of range for the current MIDI values.")
                else:
                    print(f"Invalid FSR number: {fsr_number}")
            except ValueError:
                print("Invalid data received from Arduino")



    def setup_checkboxes(self):
        for checkbox in self.checkboxes:
            checkbox.setChecked(True)  # Checked means enabled
            checkbox.stateChanged.connect(self.toggle_enable_disable)

    @Slot()
    def toggle_enable_disable(self):
        for index, checkbox in enumerate(self.checkboxes):
            if checkbox.isChecked():
                print(f"{checkbox.objectName()} enabled")
            else:
                print(f"{checkbox.objectName()} disabled")
                note_to_stop = self.midi_values[index] if index < len(self.midi_values) else None
                if note_to_stop is not None:
                    self.note_playback.stop_note_playback(note_to_stop)  # Use the NotePlayback instance

    def enable_all_checkboxes(self):
        # Enable all checkboxes in the Piano and Clarinet tabs
        for checkbox in self.get_all_checkboxes():
            checkbox.setEnabled(True)

    def disable_all_checkboxes(self):
        # Disable (gray out) all checkboxes in the Piano and Clarinet tabs
        for checkbox in self.get_all_checkboxes():
            checkbox.setEnabled(False)

    def update_note_range(self):
        selected_library = self.masterLibraryComboBox.currentText()
        self.startingNote.setEnabled(True)
        self.startingOct.setEnabled(True)

        if selected_library == "Piano":
            self.filter_note_octave_range(21, 108, "Piano")  # Piano range: A0 (21) to C8 (108)
        elif selected_library == "Clarinet":
            self.filter_note_octave_range(50, 94, "Clarinet")  # Clarinet range: D3 (50) to Bb6 (94)
        else:
            self.populate_note_octave_options()  # Custom option shows all notes and octaves

    def filter_note_octave_range(self, min_midi, max_midi, instrument):
        notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        min_octave = (min_midi // 12) - 1
        max_octave = (max_midi // 12) - 1
        max_selectable_midi = max_midi - 20 + 1  #highest selectable MIDI note to fit 20 keys
        # Clear existing items in combo boxes
        self.startingNote.clear()
        self.startingOct.clear()

        # Populate octaves based on the given range
        for octave in range(min_octave, max_octave + 1):
            self.startingOct.addItem(str(octave))

        # Populate notes only once for the given range
        valid_notes = set()
        for midi_value in range(min_midi, max_midi + 1):
            note_index = midi_value % 12
            note_name = notes[note_index]
            if note_name not in valid_notes:
                valid_notes.add(note_name)
                self.startingNote.addItem(note_name)

        # Check if the current selection is out of range and reset if necessary
        start_note_index = self.startingNote.currentIndex()
        start_octave_index = self.startingOct.currentIndex()

        # Calculate the MIDI value of the selected starting note and octave
        if start_note_index >= 0 and start_octave_index >= 0:
            selected_note = self.startingNote.itemText(start_note_index)
            selected_octave = int(self.startingOct.itemText(start_octave_index))
            selected_midi = (selected_octave + 1) * 12 + notes.index(selected_note)

            # Check if the selected MIDI value exceeds the allowable range
            if selected_midi > max_selectable_midi:
                self.textBrowser.append("Index too high for twenty notes to all be populated on the pulsepad.")
                # Default to the highest valid starting note and octave
                highest_valid_midi = max_selectable_midi
                highest_valid_octave = (highest_valid_midi // 12) - 1
                highest_valid_note = notes[highest_valid_midi % 12]

                # Set combo boxes to the highest valid values
                self.startingNote.setCurrentText(highest_valid_note)
                self.startingOct.setCurrentText(str(highest_valid_octave))

    def populate_note_octave_options(self):
        self.startingNote.clear()
        self.startingOct.clear()

        # Add all possible notes and octaves
        notes = ["A", "B", "C", "D", "E", "F", "G"]
        octaves = [str(i) for i in range(0, 9)]  # Octaves 0-8

        for note in notes:
            self.startingNote.addItem(note)
        for octave in octaves:
            self.startingOct.addItem(octave)

    @Slot()
    def update_note_assignment(self):
        try:
            start_note = self.startingNote.currentText()
            start_octave = int(self.startingOct.currentText())
            notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

            if start_note not in notes:
                raise ValueError("Invalid note selection")

            note_index = notes.index(start_note)
            start_midi = (start_octave + 1) * 12 + note_index

            # upper and lower MIDI limits based on the selected library
            selected_library = self.masterLibraryComboBox.currentText()
            if selected_library == "Piano":
                lower_midi_limit = 21  # A0
                upper_midi_limit = 108  # C8
            elif selected_library == "Clarinet":
                lower_midi_limit = 50  # D3
                upper_midi_limit = 94  # Bb6
            else:
                lower_midi_limit = 0  # General MIDI lower limit
                upper_midi_limit = 127  # General MIDI upper limit

            # highest and lowest valid starting MIDI notes for a 20-note range
            highest_valid_start_midi = upper_midi_limit - 19
            lowest_valid_start_midi = lower_midi_limit

            # Check if start_midi is above the upper limit and adjust
            if start_midi > highest_valid_start_midi:
                start_midi = highest_valid_start_midi
                start_note = notes[start_midi % 12]
                start_octave = (start_midi // 12) - 1

                # Update the UI for adjusted note and octave
                self.startingNote.setCurrentText(start_note)
                self.startingOct.setCurrentText(str(start_octave))

                self.textBrowser.append(
                    f"Index too high for twenty notes to all be populated on the pulsepad. "
                    f"Adjusted to highest available: {start_note}{start_octave}"
                )
            # Check if start_midi is below the lower limit and adjust
            elif start_midi < lowest_valid_start_midi:
                start_midi = lowest_valid_start_midi
                start_note = notes[start_midi % 12]
                start_octave = (start_midi // 12) - 1

                # Update the UI for adjusted note and octave
                self.startingNote.setCurrentText(start_note)
                self.startingOct.setCurrentText(str(start_octave))

                self.textBrowser.append(
                    f"Index too low for twenty notes to all be populated on the pulsepad. "
                    f"Adjusted to lowest available: {start_note}{start_octave}"
                )
            else:
                # Remove the warning if the selection is valid
                self.textBrowser.clear()

            # Ensure the MIDI values do not exceed the instrument's upper limit
            self.midi_values = [start_midi + i for i in range(20) if start_midi + i <= upper_midi_limit]

            # Determine the range of notes selected and display it
            first_note = notes[self.midi_values[0] % 12]
            first_octave = (self.midi_values[0] // 12) - 1
            last_note = notes[self.midi_values[-1] % 12]
            last_octave = (self.midi_values[-1] // 12) - 1
            self.textBrowser.append(
                f"{selected_library} range: {first_note}{first_octave}-{last_note}{last_octave}"
            )

            print("Assigned MIDI values:", self.midi_values)
        except ValueError as e:
            print(f"Error in note assignment: {e}")

    @Slot()
    def update_master_volume(self, value):
        self.label_19.setText(str(value))
        print(f"Master volume set to: {value}")

    @Slot()
    def update_piano_volume(self, value):
        self.label_20.setText(str(value))
        print(f"Piano volume set to: {value}")

    @Slot()
    def update_clarinet_volume(self, value):
        self.label_21.setText(str(value))
        print(f"Clarinet volume set to: {value}")

    @Slot()
    def start_recording(self):
        print("Recording started")

    @Slot()
    def stop_recording(self):
        print("Recording stopped")

    def closeEvent(self, event):
        self.server.stop()
        self.server.shutdown()
        self.arduino.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    window = DuoStepApp()
    window.show()
    app.exec()
