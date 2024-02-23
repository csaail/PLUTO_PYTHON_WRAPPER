import os   # Importing the os module for operating system-specific functionality
import sys  # Importing the sys module for system-specific parameters and functions
import keyboard_control  # Importing the keyboard_control module for controlling the drone via keyboard

keyboard_cmds = {  # Dictionary containing the key pressed and value associated with it
    'up': 10,
    'left': 30,
    'right': 40,
    'w': 50,
    's': 60,
    'space': 70,
    'r': 80,
    't': 90,
    'p': 100,
    'down': 110,
    'n': 120,
    'q': 130,
    'e': 140,
    'a': 150,
    'd': 160,
    '+': 15,
    '1': 25,
    '2': 30,
    '3': 35,
    '4': 45,
    'v': 69,
    '[A': 10,
    '[D': 30,
    '[C': 40,
    ' ': 70,
    '[B': 110
}

if os.name == 'nt':   # Check if the operating system is Windows
    import keyboard # Importing the keyboard module for keyboard input handling

    def get_key():
        event = keyboard.read_event()    # Read keyboard events
        key = event.name
        if event.event_type == keyboard.KEY_DOWN:   # Check if it's a key down event
            if key in keyboard_cmds:
                return key

elif os.name == 'posix':  # Check if the operating system is POSIX (Linux/Mac)
    import select
    import termios
    import tty

    settings = termios.tcgetattr(sys.stdin)

    def get_key():
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
            if key == '\x1b':
                key = sys.stdin.read(2)
            sys.stdin.flush()
            return key

def identify_key(key, platform):
    if key in keyboard_cmds:
        msg = keyboard_cmds[key]
        if platform == 'Windows':
            keyboard_control.identify_key(msg)
        elif platform == 'Linux/Mac':
            keymac.identify_key(msg)
    else:
        msg = 80
        if platform == 'Windows':
            keyboard_control.identify_key(msg)
        elif platform == 'Linux/Mac':
            keymac.identify_key(msg)

while True:
    key = get_key()
    if key == 'e':
        print("Stopping")
        break
    if key:
        identify_key(key, 'Windows' if os.name == 'nt' else 'Linux/Mac')
