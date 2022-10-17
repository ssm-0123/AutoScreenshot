import pyautogui
import time

def screenshot1():
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

def screenshot2():
    x1 = int(input("Set X1"))
    y1 = int(input("Set Y1"))
    x2 = int(input("Set X2"))
    y2 = int(input("Set Y2"))
    time.sleep(1)
    x = 0
    pyautogui.screenshot(str(x)+".png", region=(x1,y1,x2,y2))
    for i in range(0,100):
        time.sleep(0.5)
        a = str(x)+".png"
        bb = pyautogui.locateCenterOnScreen(a)
        print(bb)
        if bb == None:
            x = x+1
            pyautogui.screenshot(str(x)+".png", region=(x1,y1,x2,y2))

screenshot1()