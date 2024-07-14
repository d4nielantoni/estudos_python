import pyautogui
from time import sleep

pyautogui.click(981, 1055)
sleep(2)

pyautogui.keyDown('ctrl')
pyautogui.press('t')
pyautogui.keyUp('ctrl')

sleep(1)
pyautogui.click(74, 324)
sleep(4)

pyautogui.keyDown('ctrl')
pyautogui.press('f')
pyautogui.keyUp('ctrl')

pyautogui.write('orcamento')