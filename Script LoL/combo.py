from time import sleep
import pydirectinput

def combo(letra:str):

    pydirectinput.keyDown(letra)
    pydirectinput.keyUp(letra)

sleep(2)

combo("e",)
combo("w",)
combo("q",)