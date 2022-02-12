
from pyautogui import *
import pyautogui
from time import sleep
import pydirectinput

def combo(letra:str):

    pydirectinput.keyDown(letra)
    pydirectinput.keyUp(letra)

def click(x, y):
    
    
    pyautogui.click(x,y,button=RIGHT)

    combo("q") 

    sleep(1)


def check_screen():
    button_pos = pyautogui.locateOnScreen('./Image/minio.png', confidence=0.8)
            
    if button_pos != None:
        
        #print(f'Found {button_pos}')

        click(button_pos.left, button_pos.top)

        return True
    
    return False


def main():

    print('To esperando imagem', end="\n\n")
    
    while True:
        if check_screen():
 
            print('acertei um q...')
      

main()            