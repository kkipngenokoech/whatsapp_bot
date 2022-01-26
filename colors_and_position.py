import pyautogui as pt
from time import sleep
while True:
    pt_XY=pt.position()#tells us the position where our mouse pointer is
    print(pt_XY,pt.pixel(pt_XY[0],pt_XY[1]))#prints out the postiton and the color
    sleep(1)#slower the printing rate-a delay of one second
    if pt_XY[0]==0:
        break
