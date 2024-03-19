from  tkinter import *
import random

GAME_WIDTH=700
GAME_HEIGHT=700
SPEED=50
SPACE_SIZE=50
BODY_PART=3
SNAKE_COLOR="#00FF00"
FOOD_COLOR="#FF0000"
BACKGROUND_COLOR="#000000"

class snake():
    pass
class food():
    pass
def nextTurn():
    pass
def changeDirection():
    pass
def checkCollision():
    pass
def gameOver():
    pass
window=Tk()
window.title("Snake Game")
window.resizable(False,False)
score=0
direction='down'
label=Label(window,text='Score{}'.format(score),font=('consolas', 40))
label.pack()
canvas=Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()
window.mainloop()