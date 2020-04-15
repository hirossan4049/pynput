pynput
======

This library allows you to control and monitor input devices.

Currently, mouse and keyboard input and monitoring are supported.

See `here <https://pynput.readthedocs.io/en/latest/>`_ for the full
documentation.

hirossan4049 changeLog
------------
**develop branch**
* GlobalHotKeys 引数対応。




how to use GlobalHotKeys
--------------

code-block:: python
    from pynput import keyboard

    def press(string):
        print("press:"+string)

    with keyboard.GlobalHotKeys([
        ["<shift>+w", press, "shift+wwwwwww"],
        ["<ctrl>+<shift>+o", press, "c+s+ooooo!!"]] as h:
        h.join()





