
from pyautogui import *
import pyautogui
from time import sleep
import pydirectinput

def combo(letra:str):

    pydirectinput.keyDown(letra)
    pydirectinput.keyUp(letra)

def click(x, y):
    pyautogui.moveTo(x+60, y+120)

 
    pyautogui.click(x+60,+120,button=RIGHT)

    combo("e")
    combo("w")
    combo("q") 
    combo("r")


def check_screen():
    button_pos = pyautogui.locateOnScreen('./Image/boneco.png', confidence=0.7)
            
    if button_pos != None:
        #print(f'Found {button_pos}')

        click(button_pos.left, button_pos.top)

        return True
    
    return False


def main():

    print('To esperando imagem', end="\n\n")
    
    while True:
        if check_screen():
 
            print('Combei...')
      

main()            