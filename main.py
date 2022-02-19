def alinha():

    from pyautogui import locateOnScreen, click    


    button_pos = locateOnScreen('./Image/boneco.png', confidence=0.80)

    button_pos2 = locateOnScreen('./Image/boneco2.png', confidence=0.80)
            
    if button_pos != None:

        click(button_pos.left+65,button_pos.top+110) # Se adicionar button="RIGHT" o botão do mouse direito e clicador 
    
        return True

    if button_pos2 != None:

        click(button_pos2.left+65,button_pos2.top+110) # Se adicionar button="RIGHT" o botão do mouse direito e clicador 

        return True

    return False

def farma_minio():

    from pyautogui import locateOnScreen, click

    button_pos = locateOnScreen('./Image/minio.png', confidence=0.8)
            
    if button_pos != None:
        
        #print(f'Found {button_pos}')

        click(button_pos.left, button_pos.top, button="RIGHT", interval=1)

        return True
    
    return False

print("Esperando imagem...")

ligado = True

print("Ta ligado")

while True:
    from keyboard import is_pressed
    from time import sleep
    

    if is_pressed('s') and ligado == False:
        ligado = True
        print('Ta ligado')
        sleep(1)
    elif is_pressed('s') and ligado == True:
        ligado = False
        print('Ta desligado')
        sleep(1)
               

    if ligado == True:
 
        if is_pressed('q'):
            alinha()
                
        elif is_pressed('w'):
            alinha()
               
        elif is_pressed('e'):
            alinha()    
                      
        elif is_pressed('r'):
            alinha()
            
       
               

          