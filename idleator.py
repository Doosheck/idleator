'''This script is the main script for the Idleator project.
Its purpose is to move the mouse a little bit every few seconds to prevent the computer from going to sleep.
This is useful for when you are watching a video or reading a long article and you don't want the computer to go to sleep. '''

import time
import pyautogui
import keyboard

def main():
    count = 0
    while True:
        # Check if the escape key is pressed
        if keyboard.is_pressed('esc'):
            print("Execution stopped by user.")
            break
        
        # Check if the mouse was moved in the last 240 seconds
        if pyautogui.onScreen(0, 0):
            # Move the mouse in a circle
            pyautogui.move(20, 0, duration=0.25)
            pyautogui.move(0, 20, duration=0.25)
            pyautogui.move(-20, 0, duration=0.25)
            pyautogui.move(0, -20, duration=0.25)
            # Move to the top left corner of the screen and click
            pyautogui.moveTo(100, 100, duration=0.25)
            pyautogui.click()
            #Go back to the center of the screen
            pyautogui.moveTo(960, 540, duration=0.25)
            time.sleep(1)
            count += 1
            print('Mouse moved, count:', count)
        else:
            time.sleep(240)


if __name__ == '__main__':
    main()