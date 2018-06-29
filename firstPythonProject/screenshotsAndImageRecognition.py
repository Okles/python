Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pyautogui
>>> pyautogui.screenshot()
<PIL.Image.Image image mode=RGB size=1920x1080 at 0xEB3B90>
>>> pyautogui.screenshot(r'c:\examples\example_ss.jpg')
<PIL.Image.Image image mode=RGB size=1920x1080 at 0x32AA5B0>
>>> pyautogui.locateOnScreen(r'c:\examples\5key.png')
>>> pyautogui.locateOnScreen(r'c:\examples\5key.png')
(684, 360, 30, 23)
>>> pyautogui.locateCenterOnScreen(r'c:\examples\5key.png')
(699, 371)
>>> pyautogui.moveTo((699, 371))
>>> pyautogui.click((699, 371))
>>> pyautogui.locateCenterOnScreen(r'c:\examples\5key.png')
(726, 378)
>>> pyautogui.moveTo((699, 371))
>>> pyautogui.click((699, 371))
>>> pyautogui.locateOnScreen(r'c:\examples\5key.png')
(711, 367, 30, 23)
>>> pyautogui.locateCenterOnScreen(r'c:\examples\5key.png')
(726, 378)
pyautogui.locateCenterOnScreen(r'c:\examples\5key.png')
>>> pyautogui.moveTo((699, 371))
>>> pyautogui.click((699, 371))
>>> 
