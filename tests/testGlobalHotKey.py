from pynput import keyboard

def press(string):
    print("pressed!")
    print(string)


with keyboard.GlobalHotKeys([["<shift>+w", press,"hello"]]) as h:
    h.join()
