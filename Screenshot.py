import pyautogui
import time
time.sleep(1)
x = 0
pyautogui.screenshot(str(x)+".png")
for i in range(0,100):
    time.sleep(0.5)
    a = str(x)+".png"
    bb = pyautogui.locateCenterOnScreen(a)
    print(bb)
    if bb == None:
        x = x+1
        pyautogui.screenshot(str(x)+".png")
