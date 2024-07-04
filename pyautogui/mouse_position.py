from time import sleep
import pyautogui
 
while True:
    x, y = pyautogui.position()

    print(f"({x}, {y})") #print mouse position

    sleep(2)
