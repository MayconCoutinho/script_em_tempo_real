### ***<h1 align="center"> 🕹 Script em python LoL </h1>***

## ***📌 Observações:***

&emsp; Apesar de ser um script simples e com poucas linhas, acredito ser bem eficiente para projetos simples em que não exige reação acima de 2 segundos para indentificar uma imagem em tempo real. Acredito que tenha como diminuir o tempo de reação atavés de uma imagem com menos pixel ou diminuindo a "certeza" de que as duas imagens são semelhantes, a "certeza" esta em 0.8 ou 80%, no entanto isso costuma diminuir a eficiencia do script.

   

&nbsp;

<img src="https://github.com/MayconCoutinho/script_lol/blob/main/Anima%C3%A7%C3%A3o213564.gif" alt="Image">


&nbsp;

## ***📌 Oque o Script faz :***
&nbsp;
   - [x] Indentificar o inimigo.
   - [x] Mira nele ao pressionar uma habilidade ("q","w","e","r").
   - [x] Desativar e ativar script apertando "s".

&nbsp;

## ***📡 Imports :***


```python
 
from pyautogui import locateOnScreen, click   # "locateOnScreen" reconhecimento de imagem em tempo real, "click" mover o mouse.
from keyboard import is_pressed               # "is_pressed" identificar se alguma tecla específica esta sendo pressionada do teclado
from time import sleep                        # "sleep" permite definir pausas de tempo antes de ativar alguma coisa.         

```
