def alinha():
    from pyautogui import locateOnScreen, click    


    button_pos = locateOnScreen('./Image/boneco.png', confidence=0.80)         #  "locateOnScreen" com base na imagem posta, localiza na tela padrão de pixel semelhante a imagem,
                                                                               #  "confidence=0.80" é a quantidade de "certeza" de que a imagem base é igual a imagem da tela.
    button_pos2 = locateOnScreen('./Image/boneco2.png', confidence=0.80)
            
    if button_pos != None:

        click(button_pos.left+65,button_pos.top+110)                           # "click" tem como usar para clicar, mas apenas ta movendo o mouse       
    
        return True

    if button_pos2 != None:

        click(button_pos2.left+65,button_pos2.top+110) 

        return True

    return False

print("Esperando imagem...")

ligado = True

while True:
    from keyboard import is_pressed
    from time import sleep
    

    if is_pressed('s') and ligado == False:         # "is_pressed()" indentifica se a tecla esta sendo pressionada.
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
            
       
               

          
