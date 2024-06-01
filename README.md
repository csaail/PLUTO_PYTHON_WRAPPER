# PLUTO_PYTHON_WRAPPER

Pluto can be operated using Python for various tasks. Python is a versatile programming language known for its simplicity and readability.

## Basic Flight Controls/ Commands:
![image](https://github.com/csaail/PLUTO_PYTHON_WRAPPER/assets/87662482/0c2c1fd0-8676-4b9c-ab87-48ce3d7c87af)
Pitch => Forward/Back.<br/> Roll => Left/right.<br/>  Yaw => Left/right rotation around the centre of the frame.<br/>  Throttle => Changed altitude/speed.

# plutocontrol

plutocontrol is a Python library for controlling Pluto drones. This library provides various methods to interact with the drone, including connecting, controlling movements, and accessing sensor data.

## Installation

```bash
pip install plutocontrol
```

## Usage

After installing the package, you can import and use the `Pluto` class in your Python scripts.

### Example Usage

#### Example 1

```python
from plutocontrol import Pluto

# Create an instance of the Pluto class
pluto = Pluto()

# Connect to the drone
pluto.connect()

# Arm the drone
pluto.arm()

# Disarm the drone
pluto.disarm()

# Disconnect from the drone
pluto.disconnect()
```



## Keyboard Controls:

To set up keyboard controls for your Pluto drone, follow these general steps:

1. Locate Keyboard Control Files:
   - Navigate to the appropriate directory based on your operating system:
     - For Windows users: Keyboard/windows
     - For Linux/Mac users: Keyboard/linux,mac

2. Run Keyboard Control Script:
   - Locate the keyboard.py file in the respective directory and run it.

### Specific Instructions:

#### For Windows Users:
- Navigate to the Keyboard/windows directory.
- Run the ```keyboard.py``` script.

#### For Linux/Mac Users:
- Navigate to the Keyboard/linux_mac directory.
- Run the ```keyboard.py``` script.

![W](https://github.com/csaail/PLUTO_PYTHON_WRAPPER/assets/87662482/2ed955e3-dea1-4dfe-adc3-5ba69d3fdc1d)

## Joystick Controls Setup:

To set up joystick controls for your Pluto drone, follow these general steps:

1. Ensure Necessary Libraries:
   - Make sure you have the required libraries installed for your operating system.

2. Locate Joystick Control Files:
   - Navigate to the appropriate directory based on your operating system:
     - For Windows users: Joystick/windows
     - For Ubuntu (Linux) users: Joystick/linux
     - For macOS users: Joystick/mac

3. Run Joystick Control Script:
   - Locate the ```joystick.py``` file in the respective directory and run it.

### Specific Instructions:

#### For Windows Users:
- Ensure that you have the necessary libraries installed.
- Navigate to the Joystick/windows directory.
- Run the joystick.py script.

#### For Ubuntu (Linux) Users:
- Make sure you have the Evdev library installed on your system.
- Navigate to the Joystick/linux directory.
- Run the joystick.py script.

#### For macOS Users:
- Ensure that you have the Pygame library installed.
- Navigate to the Joystick/mac directory.
- Run the joystick.py script.

Currently the default settings are: (Note: you can change them according to your need)
![joystick](https://github.com/csaail/PLUTO_PYTHON_WRAPPER/assets/87662482/17bdba11-c7b0-4a49-a892-8efce235e57e)
![joystick tp](https://github.com/csaail/PLUTO_PYTHON_WRAPPER/assets/87662482/79608307-4590-41d0-8d1b-ab737c30b94a)

## Voice Controlled Drone

We've developed a script that enables you to control your Pluto drone using your voice!

1. **Download Pre-trained Voice Model:**
   - Visit [Vosk Models](https://alphacephei.com/vosk/models) to download a pre-trained voice model.
   - Recommended models: `vosk-model-small-en-us-0.15` or `vosk-model-en-in-0.5`.

2. **Configure Voice Command Script:**
   - Copy the path where you've stored your downloaded model.
   - Paste the path into the `voice_cmd.py` file located in the "voice" folder.

3. **Run Voice Command Script:**
   - Navigate to the "voice" folder.
   - Run the file:
     `
     voice_cmd.py
     `

Currently, the drone responds to the following voice commands:
- "hello" to arm the drone.
- "take off" to initiate takeoff.
- "land" to initiate landing.

Feel free to customize these commands according to your preferences.


## Structure of the Wrapper:
![image](https://github.com/csaail/PLUTO_PYTHON_WRAPPER/assets/87662482/927591e8-36cd-4f2d-ae88-0016fa9479c9)
