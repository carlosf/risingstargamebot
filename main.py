# This is a sample Python script.
from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api
import win32con

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32.api.mouse_event(win32con.MOUSEEVENTF_LEFTUP.0.0)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    time.sleep(2)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
