from PySide6.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QFileDialog
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
        self.clarinetVol.valueChanged.connect(self.update_trumpet_volume)
        self.recordButton.clicked.connect(self.start_recording)
        self.stopButton.clicked.connect(self.stop_recording)

        # Arduino
        self.arduino1 = serial.Serial('COM5', 9600)
        self.arduino2 = serial.Serial('COM6', 9600)
        self.arduino3 = serial.Serial('COM7', 9600)
        time.sleep(2)  # Wait for Arduino to initialize

        # Set up directories for samples
        BASE_DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
        SAMPLES_DIR = os.path.join(BASE_DIR, "Resources", "piano", "samples24bit")
        TRUMPET_DIR = os.path.join(BASE_DIR, "Resources", "trumpet-solo")

        # Initialize NotePlayback
        self.note_playback = NotePlayback(SAMPLES_DIR,TRUMPET_DIR)


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


        # Connect all checkboxes to the toggle method
        self.checkboxes = [
            self.L5d, self.L5u, self.L4d, self.L4u, self.L3d, self.L3u, self.L2d, self.L2u, self.L1d, self.L1u,
            self.R1d, self.R1u, self.R2d, self.R2u, self.R3d, self.R3u, self.R4d, self.R4u, self.R5d, self.R5u
        ]
        # Initialize mappings for checkboxes
        self.master_to_piano = {
            self.L1u: self.L1u_2, self.L1d: self.L1d_2,
            self.L2u: self.L2u_2, self.L2d: self.L2d_2,
            self.L3u: self.L3u_2, self.L3d: self.L3d_2,
            self.L4u: self.L4u_2, self.L4d: self.L4d_2,
            self.L5u: self.L5u_2, self.L5d: self.L5d_2,
            self.R1u: self.R1u_2, self.R1d: self.R1d_2,
            self.R2u: self.R2u_2, self.R2d: self.R2d_2,
            self.R3u: self.R3u_2, self.R3d: self.R3d_2,
            self.R4u: self.R4u_2, self.R4d: self.R4d_2,
            self.R5u: self.R5u_2, self.R5d: self.R5d_2,
        }

        self.master_to_trumpet = {
            self.L1u: self.L1u_3, self.L1d: self.L1d_3,
            self.L2u: self.L2u_3, self.L2d: self.L2d_3,
            self.L3u: self.L3u_3, self.L3d: self.L3d_3,
            self.L4u: self.L4u_3, self.L4d: self.L4d_3,
            self.L5u: self.L5u_3, self.L5d: self.L5d_3,
            self.R1u: self.R1u_3, self.R1d: self.R1d_3,
            self.R2u: self.R2u_3, self.R2d: self.R2d_3,
            self.R3u: self.R3u_3, self.R3d: self.R3d_3,
            self.R4u: self.R4u_3, self.R4d: self.R4d_3,
            self.R5u: self.R5u_3, self.R5d: self.R5d_3,
        }

        self.master_to_upload = {
            self.L5u: self.L5u_5, self.L5d: self.L5d_5,
            self.L4u: self.L4u_5, self.L4d: self.L4d_5,
            self.L3u: self.L3u_5, self.L3d: self.L3d_5,
            self.L2u: self.L2u_5, self.L2d: self.L2d_5,
            self.L1u: self.L1u_5, self.L1d: self.L1d_5,
            self.R1u: self.R1u_5, self.R1d: self.R1d_5,
            self.R2u: self.R2u_5, self.R2d: self.R2d_5,
            self.R3u: self.R3u_5, self.R3d: self.R3d_5,
            self.R4u: self.R4u_5, self.R4d: self.R4d_5,
            self.R5u: self.R5u_5, self.R5d: self.R5d_5,
        }

        # Call the setup_checkboxes method
        self.setup_checkboxes()

        # Initialize file tracking for upload buttons
        self.uploaded_files = {}

        # Map buttons and labels
        self.upload_buttons_labels = {
            # Left side
            self.uploadButtonL: self.upload_label_L_1,
            self.uploadButtonL_2: self.upload_label_L_2,
            self.uploadButtonL_3: self.upload_label_L_3,
            self.uploadButtonL_4: self.upload_label_L_4,
            self.uploadButtonL_5: self.upload_label_L_5,
            self.uploadButtonL_6: self.upload_label_L_6,
            self.uploadButtonL_7: self.upload_label_L_7,
            self.uploadButtonL_8: self.upload_label_L_8,
            self.uploadButtonL_9: self.upload_label_L_9,
            self.uploadButtonL_10: self.upload_label_L_10,

            # Right side
            self.uploadButtonR_1: self.upload_label_R_1,
            self.uploadButtonR_2: self.upload_label_R_2,
            self.uploadButtonR_3: self.upload_label_R_3,
            self.uploadButtonR_4: self.upload_label_R_4,
            self.uploadButtonR_5: self.upload_label_R_5,
            self.uploadButtonR_6: self.upload_label_R_6,
            self.uploadButtonR_7: self.upload_label_R_7,
            self.uploadButtonR_8: self.upload_label_R_8,
            self.uploadButtonR_9: self.upload_label_R_9,
            self.uploadButtonR_10: self.upload_label_R_10,
        }

        # Connect all upload buttons to the same handler
        for button in self.upload_buttons_labels.keys():
            button.clicked.connect(lambda checked, btn=button: self.handle_upload_remove(btn))

    def resolve_upload_button(self, master_checkbox):
        # same order as master_to_upload
        upload_widgets = list(self.master_to_upload.values())
        # same order as upload_buttons_labels
        upload_buttons = list(self.upload_buttons_labels.keys())

        # check if master checkbox is valid
        upload_widget = self.master_to_upload.get(master_checkbox)
        if upload_widget:
            # Find the index of the resolved widget in `upload_widgets`
            widget_index = upload_widgets.index(upload_widget)
            # Use the same index to find the corresponding button
            if 0 <= widget_index < len(upload_buttons):
                resolved_button = upload_buttons[widget_index]
                #print(f"Resolved button: {resolved_button.objectName()} for checkbox: {master_checkbox.objectName()}")
                return resolved_button
        print(f"No upload button resolved for checkbox: {master_checkbox.objectName()}")
        return None

    @Slot()
    def handle_upload_remove(self, button):
        # Find corresponding label
        label = self.upload_buttons_labels[button]

        if button.text() == "upload":
            # Open file dialog
            file_path, _ = QFileDialog.getOpenFileName(self, "Upload Sound File", "", "Audio Files (*.wav *.mp3)")
            if file_path:
                self.uploaded_files[button.objectName()] = file_path  # Track uploaded file
                button.setText("remove")  # Change button text
                label.setText(f"File: {os.path.basename(file_path)}")  # Update label
                print(f"Uploaded: {file_path}")  # Debug log
                #print(f"Uploaded files mapping: {self.uploaded_files}")

            else:
                print("No file selected.")
        else:
            # Remove uploaded file
            if button.objectName() in self.uploaded_files:
                del self.uploaded_files[button.objectName()]
            button.setText("upload")  # Reset button text
            label.setText("No File Uploaded")  # Reset label
            print("File removed.")  # Debug log

    def handle_arduino_input(self):
        selected_library = self.masterLibraryComboBox.currentText()
        for arduino in [self.arduino1, self.arduino2, self.arduino3]:
            if arduino.in_waiting > 0:
                data = arduino.readline().decode().strip()
                print(f"Received from Arduino: {data}")
                try:
                    fsr_number, velocity, action = map(int, data.split(','))

                    # Validate FSR number and map it to the corresponding MIDI note
                    if 1 <= fsr_number <= 20:
                        note_index = fsr_number - 1  # FSRs are 1-indexed, so subtract 1 for 0-indexed list

                        if note_index < len(self.midi_values):
                            note = self.midi_values[note_index]

                            # Check if the corresponding checkbox is checked (enabled)
                            if self.checkboxes[note_index].isChecked() and selected_library == "Piano":
                                if action == 1:  # Start note
                                    self.note_playback.start_piano_note_playback(note, velocity)
                                elif action == 0:  # Stop note
                                    self.note_playback.stop_piano_note_playback(note)
                            elif self.checkboxes[note_index].isChecked() and selected_library == "Trumpet":
                                if action == 1:  # Start note
                                    self.note_playback.start_trumpet_note_playback(note, velocity)
                                elif action == 0:  # Stop note
                                    self.note_playback.stop_trumpet_note_playback(note)
                            elif self.checkboxes[note_index].isChecked() and selected_library == "Custom":
                                if action == 1:  # Start note
                                    if self.master_to_piano[self.checkboxes[note_index]].isChecked():
                                        self.note_playback.start_piano_note_playback(note, velocity)
                                    elif self.master_to_trumpet[self.checkboxes[note_index]].isChecked():
                                        self.note_playback.start_trumpet_note_playback(note, velocity)
                                    elif self.master_to_upload[self.checkboxes[note_index]].isChecked():
                                        #print("Yay!")
                                        upload_button = self.resolve_upload_button(self.checkboxes[note_index])
                                        if upload_button:
                                            file_path = self.uploaded_files.get(upload_button.objectName())
                                            #print(f"Resolved upload button: {upload_button.objectName()}, File Path: {file_path}")
                                            if not file_path:
                                                print(f"Uploaded files (debug): {self.uploaded_files}")  # Log the full dictionary for debugging
                                            if file_path:
                                                self.note_playback.start_uploaded_note_playback(file_path)
                                elif action == 0:  # Stop note
                                    if self.master_to_piano[self.checkboxes[note_index]].isChecked():
                                        self.note_playback.stop_piano_note_playback(note)
                                    elif self.master_to_trumpet[self.checkboxes[note_index]].isChecked():
                                        self.note_playback.stop_trumpet_note_playback(note)
                                    elif self.master_to_upload[self.checkboxes[note_index]].isChecked():
                                        upload_button = self.resolve_upload_button(self.checkboxes[note_index])
                                        if upload_button:
                                            file_path = self.uploaded_files.get(upload_button.objectName())
                                            #print(f"Resolved upload button: {upload_button.objectName()}, File Path: {file_path}")
                                            if not file_path:
                                                print(f"Uploaded files (debug): {self.uploaded_files}")  # Log the full dictionary for debugging
                                            if file_path:
                                                self.note_playback.stop_uploaded_note_playback(file_path)
                                        else:
                                            print(
                                                f"No upload button resolved for checkbox: {self.checkboxes[note_index].objectName()}")


                            else:
                                print(f"Note {note} is disabled and will not produce sound.")
                                # self.textBrowser.append(f"Note {note} is disabled and will not produce sound.")

                        else:
                            print(f"FSR number {fsr_number} is out of range for the current MIDI values.")
                    else:
                        print(f"Invalid FSR number: {fsr_number}")
                except ValueError:
                    print("Invalid data received from Arduino")

    # def handle_arduino_input(self):
    #     selected_library = self.masterLibraryComboBox.currentText()
    #     for arduino in [self.arduino1, self.arduino2]:
    #         if arduino.in_waiting > 0:
    #             data = arduino.readline().decode().strip()
    #             print(f"Received from Arduino: {data}")
    #             try:
    #                 fsr_number, velocity, action = map(int, data.split(','))
    #
    #                 # Validate FSR number and map it to the corresponding MIDI note
    #                 if 1 <= fsr_number <= 20:
    #                     note_index = fsr_number - 1  # FSRs are 1-indexed, so subtract 1 for 0-indexed list
    #
    #                     if note_index < len(self.midi_values):
    #                         note = self.midi_values[note_index]
    #
    #                         # Check if the corresponding checkbox is checked (enabled)
    #                         if self.checkboxes[note_index].isChecked() and selected_library == "Piano":
    #                             if action == 1:  # Start note
    #                                 self.note_playback.start_piano_note_playback(note, velocity)
    #                             elif action == 0:  # Stop note
    #                                 self.note_playback.stop_piano_note_playback(note)
    #                         elif self.checkboxes[note_index].isChecked() and selected_library == "Trumpet":
    #                             if action == 1:  # Start note
    #                                 self.note_playback.start_trumpet_note_playback(note, velocity)
    #                             elif action == 0:  # Stop note
    #                                 self.note_playback.stop_trumpet_note_playback(note)
    #                         elif self.checkboxes[note_index].isChecked() and selected_library == "Custom":
    #                             if action == 1:  # Start note
    #                                 self.note_playback.start_trumpet_note_playback(note, velocity)
    #                             elif action == 0:  # Stop note
    #                                 self.note_playback.stop_trumpet_note_playback(note)
    #                         else:
    #                             print(f"Note {note} is disabled and will not produce sound.")
    #                             # self.textBrowser.append(f"Note {note} is disabled and will not produce sound.")
    #
    #                     else:
    #                         print(f"FSR number {fsr_number} is out of range for the current MIDI values.")
    #                 else:
    #                     print(f"Invalid FSR number: {fsr_number}")
    #             except ValueError:
    #                 print("Invalid data received from Arduino")

    def setup_checkboxes(self):
        # Connect master tab checkboxes to toggle behavior
        for master_checkbox in self.master_to_piano.keys():
            master_checkbox.setChecked(False)  # Unchecked by default
            master_checkbox.stateChanged.connect(self.sync_with_tabs)
        for master_checkbox in self.master_to_trumpet.keys():
            master_checkbox.setChecked(False)
            master_checkbox.stateChanged.connect(self.sync_with_tabs)
        for master_checkbox in self.master_to_upload.keys():
            master_checkbox.setChecked(False)
            master_checkbox.stateChanged.connect(self.sync_with_tabs)

    @Slot()
    def sync_with_tabs(self):
        selected_library = self.masterLibraryComboBox.currentText()

        # Ensure mutual exclusivity between tabs
        for master_checkbox, piano_checkbox in self.master_to_piano.items():
            if piano_checkbox.isChecked():
                # Uncheck corresponding trumpet/upload checkboxes
                self.master_to_trumpet[master_checkbox].setChecked(False)
                self.master_to_upload[master_checkbox].setChecked(False)
        for master_checkbox, trumpet_checkbox in self.master_to_trumpet.items():
            if trumpet_checkbox.isChecked():
                # Uncheck corresponding piano/upload checkboxes
                self.master_to_piano[master_checkbox].setChecked(False)
                self.master_to_upload[master_checkbox].setChecked(False)
        for master_checkbox, upload_checkbox in self.master_to_upload.items():
            if upload_checkbox.isChecked():
                # Uncheck corresponding piano/trumpet checkboxes
                self.master_to_piano[master_checkbox].setChecked(False)
                self.master_to_trumpet[master_checkbox].setChecked(False)

        # Enable or disable checkboxes based on the selected library
        for master_checkbox, piano_checkbox in self.master_to_piano.items():
            piano_checkbox.setEnabled(selected_library == "Custom" and master_checkbox.isChecked())
        for master_checkbox, trumpet_checkbox in self.master_to_trumpet.items():
            trumpet_checkbox.setEnabled(selected_library == "Custom" and master_checkbox.isChecked())
        for master_checkbox, upload_checkbox in self.master_to_upload.items():
            upload_checkbox.setEnabled(selected_library == "Custom" and master_checkbox.isChecked())

    # def sync_with_tabs(self):
    #     selected_library = self.masterLibraryComboBox.currentText()
    #
    #     # Enable/Disable checkboxes based on the selected library and master checkbox state
    #     for master_checkbox, piano_checkbox in self.master_to_piano.items():
    #         piano_checkbox.setEnabled(selected_library == "Custom" and master_checkbox.isChecked())
    #     for master_checkbox, trumpet_checkbox in self.master_to_trumpet.items():
    #         trumpet_checkbox.setEnabled(selected_library == "Custom" and master_checkbox.isChecked())
    #     for master_checkbox, upload_checkbox in self.master_to_upload.items():
    #         upload_checkbox.setEnabled(selected_library == "Custom" and master_checkbox.isChecked())

    @Slot()
    def toggle_enable_disable(self):
        for index, checkbox in enumerate(self.checkboxes):
            if checkbox.isChecked():
                print(f"{checkbox.objectName()} enabled")
            else:
                print(f"{checkbox.objectName()} disabled")
                note_to_stop = self.midi_values[index] if index < len(self.midi_values) else None
                if note_to_stop is not None:
                    self.note_playback.stop_piano_note_playback(note_to_stop)  # Use the NotePlayback instance
                    self.note_playback.stop_trumpet_note_playback(note_to_stop)

    def enable_all_tab_buttons(self):
        for checkbox in self.master_to_piano.values():
            checkbox.setEnabled(True)
        for checkbox in self.master_to_trumpet.values():
            checkbox.setEnabled(True)
        for checkbox in self.master_to_upload.values():
            checkbox.setEnabled(True)

    def disable_all_tab_buttons(self):
        for checkbox in self.master_to_piano.values():
            checkbox.setEnabled(False)
        for checkbox in self.master_to_trumpet.values():
            checkbox.setEnabled(False)
        for checkbox in self.master_to_upload.values():
            checkbox.setEnabled(False)

    def update_note_range(self):
        selected_library = self.masterLibraryComboBox.currentText()
        self.startingNote.setEnabled(True)
        self.startingOct.setEnabled(True)

        if selected_library == "Piano":
            self.filter_note_octave_range(21, 108, "Piano")  # Piano range: A0 (21) to C8 (108)
            self.disable_all_tab_buttons()
        elif selected_library == "Trumpet":
            self.filter_note_octave_range(56, 84, "Trumpet")  # Trumpet range: G#3 (?) to C6 (?)
            self.disable_all_tab_buttons()
        elif selected_library == "Custom":
            #self.populate_note_octave_options()  # Custom option shows all notes and octaves
            self.filter_note_octave_range(21, 108, "Custom")  # Piano range: A0 (21) to C8 (108)
            self.enable_all_tab_buttons()
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
            elif selected_library == "Trumpet":
                lower_midi_limit = 56  # G#3
                upper_midi_limit = 84  # C6
            else:
                lower_midi_limit = 21  # General MIDI lower limit
                upper_midi_limit = 108  # General MIDI upper limit

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
    def update_trumpet_volume(self, value):
        self.label_21.setText(str(value))
        print(f"Trumpet volume set to: {value}")

    @Slot()
    def start_recording(self):
        print("Recording started")

    @Slot()
    def stop_recording(self):
        print("Recording stopped")

    def closeEvent(self, event):
        self.server.stop()
        self.server.shutdown()
        self.arduino1.close()
        self.arduino2.close()
        self.arduino3.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    window = DuoStepApp()
    window.show()
    app.exec()
