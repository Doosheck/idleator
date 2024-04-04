'''This script is the main script for the Idleator project.
Its purpose is to move the mouse a little bit every few seconds to prevent the computer from going to sleep.
This is useful for when you are watching a video or reading a long article and you don't want the computer to go to sleep. '''

import time
import pyautogui

def main():
    while True:
        # Check if the mouse was moved in the last 240 seconds
        if pyautogui.onScreen(0, 0):
            pyautogui.moveRel(1, 1)
            pyautogui.moveRel(-1, -1)
            time.sleep(240)
            print('Mouse moved')
        else:
            time.sleep(240)


if __name__ == '__main__':
    main()