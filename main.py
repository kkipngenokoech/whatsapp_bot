import pyautogui as pt
import pyperclip
import random
from time import sleep
sleep(3)
position_1=pt.locateOnScreen("whatsapp\\smiley_paperclip.png",confidence=.6)#the confidence allows a chance of 60% similarity
X,y=position_1[0],position_1[1]
#gets the message
def get_message():
    global x,y
    position=pt.locateOnScreen("whatsapp\\smiley_paperclip.png",confidence=.6)#the confidence allows a chance of 60% similarity
    x,y=position[0],position[1]
    pt.moveTo(x,y,duration=6)
    pt.moveTo(x+40,y-70,duration=.6)
get_message()