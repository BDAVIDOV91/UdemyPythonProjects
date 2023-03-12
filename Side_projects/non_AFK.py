import pyautogui as pag
import random
import time 
import keyboard


while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x, y, 0.5)
    time.sleep(2)
    
    
    if keyboard.is_pressed('esc'):
        break