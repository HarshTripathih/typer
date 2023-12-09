import pyautogui

import time

time.sleep(10)
with open('data.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        pyautogui.write(line.lstrip())
        

        