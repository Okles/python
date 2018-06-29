Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pyautogui
>>> pyautogui.size()
(1920, 1080)
>>> width, height = pyautogui.size()
>>> width
1920
>>> height
1080
>>> pyautogui.position()
(1196, 179)
>>> pyautogui.position()
(1618, 1079)
>>> pyautogui.position()
(0, 0)
>>> pyautogui.moveTo(15,15)
>>> pyautogui.moveTo(15,15, duration=1.5)
>>> pyautogui.moveRel(20,0, duration=1.5)
>>> pyautogui.moveRel(820,220, duration=1.5)
>>> pyautogui.moveRel(520,220, duration=1.5)
>>> pyautogui.position()
(1249, 34)
>>> pyautogui.click(1249, 34)
>>> pyautogui.click(1249, 34, duration=1)
>>> pyautogui.doubleclick(1249, 34, duration=1)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    pyautogui.doubleclick(1249, 34, duration=1)
AttributeError: module 'pyautogui' has no attribute 'doubleclick'
>>> pyautogui.rightclick(520,220, duration=1.5)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    pyautogui.rightclick(520,220, duration=1.5)
AttributeError: module 'pyautogui' has no attribute 'rightclick'
>>> ## useful tool for measuring a mouse position:
## pyautogui.displayMousePosition() IN CMD!

