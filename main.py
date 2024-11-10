import pyautogui
from time import sleep

def getCenter(box):
    return box.left + box.width/2, box.top + box.height/2

def writeCommand(command):
    mousePos = pyautogui.position()
    if (mousePos.x, mousePos.y) != (1280, 787):
        pyautogui.press("esc")
    pyautogui.press("t")
    pyautogui.typewrite(command)
    pyautogui.press("enter")