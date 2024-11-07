# DuoStep: PulsePad App

DuoStep: PulsePad is a user-friendly, Arduino-integrated musical app that’s all about giving music lovers and developers an expressive, customizable experience. Built with PySide6 and Qt for a slick and intuitive interface, the app offers detailed control over sound playback, sound libraries, and instrument configurations, with real-time sensor feedback and solid error handling.
## Features at a Glance

### 1. **User Interface**
- **Master Tab**: 
  - **Instrument Library Selector**: Choose between pre-set instrument libraries (Piano and Clarinet) or a Custom mode. In Piano and Clarinet modes, all keys are automatically assigned to the selected instrument, while in Custom mode, you can individually assign keys to either library.
  - **Note and Octave Range Control**: Users can define the starting note and octave for playback. The app grays out or disables out-of-range notes dynamically, ensuring foolproof adjustments. For instance, Piano notes are limited to the range A0 (MIDI 21) to C8 (MIDI 108), while Clarinet notes span D3 (MIDI 50) to Bb6 (MIDI 94).
  - **Enable/Disable Button Functionality**: Each key can be individually enabled or disabled. Disabled keys will produce no sound, and in the Piano and Clarinet tabs, corresponding checkboxes are grayed out.
- **Piano and Clarinet Tabs**: In these tabs, users can further fine-tune the playback settings. If a key is disabled in the Master tab, its corresponding control here will also be grayed out. If enabled, users can opt to play sounds from one or both libraries simultaneously.

### 2. **Playback Configuration**
- **Multi-Note Playback**: Extend playback functionality to support different notes dynamically, mapping force sensor readings to MIDI values.
- **Velocity-Based Volume Control**: The app adjusts sound volume or playback speed based on sensor input intensity, simulating a more expressive musical performance.
- **Pitch Shifting**: Handles multi-sample playback with dynamic pitch shifting to cover all notes efficiently. For example, a single C4 sample can be pitch-shifted to cover C#4 using the `calculate_speed` function.
- **Error Handling and Warnings**: The app ensures that all notes remain within valid ranges. If a user tries to select a note outside the valid range, the app provides an automatic adjustment and displays a warning message in the text box.

### 3. **Real-Time Arduino Integration**
- **Force Sensor Inputs**: The app listens for input from force-sensitive resistors (FSRs) connected to an Arduino. FSR numbers (1-20) are mapped to MIDI values based on the user-selected range.
- **Efficient Data Handling**: The app efficiently parses and handles incoming serial data from the Arduino, starting or stopping note playback based on the data received.

## Installation and Setup
1. **Clone the Repository**
   ```bash
   git clone <https://github.com/youzi1007/DuoStep-PulsePad-App>
   cd yourPath/DuoStep-PulsePad-App-main
   ```
2. **Set Up the Python Environment**
   - It is recommended to use a virtual environment to manage dependencies.
   - Please use Anaconda3 to create virtual environment, or else pyo won't install
   ```bash
   conda create -n myenv python=3.10
   conda activate DuoStepEnv
   ```
   - If need to deactivate the env
   ```bash
   conda deactivate
3. **Install Required Libraries**
   - **PySide6**: For the GUI (graphical user interface)
     ```bash
     pip install PySide6
     ```
   - **Pyo**: For audio playback
     ```bash
     pip install pyo
     ```
   - **PySerial**: For serial communication with the Arduino
     ```bash
     pip install pyserial
     ```
4. **Arduino Setup**
   - Connect your force-sensitive resistors (FSRs) to the Arduino and ensure it is set to communicate over the correct COM port (update the code if needed).

## Usage Instructions
1. **Launch the Application**
   - Run the main script to open the GUI.
   ```bash
   python main.py
   ```
2. **Configure Your Settings**
   - **Master Tab**: Select your instrument library, configure note ranges, and enable or disable keys.
   - **Instrument Tabs**: Customize individual key settings for Piano and Clarinet.
3. **Play Notes with Arduino Input**
   - The app will listen to Arduino input and respond to FSR readings, playing notes with corresponding volume and speed adjustments.

## How It Works
- **Note Range Adjustment**: The app dynamically adjusts starting notes to prevent out-of-range selections. For example, if the highest valid note is C8 (MIDI 108), the starting note will default to the highest possible position within the range of 20 consecutive notes.
- **Error Handling**: The app handles invalid selections gracefully by resetting to valid defaults and displaying warnings.
- **Sound Playback**: Uses `pyo` to handle audio playback with real-time pitch shifting and volume control.

## Future Enhancements
- **Multi-Instrument Support**: Add more instruments or sound libraries.
- **GUI Enhancements**: Improve the interface for better usability and control.
- **Advanced Sound Effects**: Introduce more dynamic audio effects and customizable playback options.
- **Less Delay**: Introducing new sensor and new filtering algorithm to reduce delay while decreasing note playback flickering
- **Recording Functionality**: Add a recording feature to better serve MIDI creators, making it easy to capture and refine musical ideas directly within the app.


## Troubleshooting
- **Serial Port Issues**: Ensure your Arduino is correctly connected and the COM port matches the one specified in the code.
- **Audio Playback Problems**: Check if the `pyo` server is properly initialized and that your audio device is configured correctly.

Enjoy creating music with DuoStepApp!
