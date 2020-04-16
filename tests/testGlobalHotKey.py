from pynput import keyboard

def press(string):
    print("pressed!")
    print(string)


with keyboard.GlobalHotKeys([
        ["<shift>+w", press,"hello,W"],
        ["<shift>+h", press,"shiftHH"]]) as h:
    h.join()
