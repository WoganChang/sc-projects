"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
VY=0
DELAY = 20
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
times=0
switch = False

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global times,switch,VY
    ball=GOval(SIZE,SIZE,x=START_X,y=START_Y)
    ball.filled= True
    ball.fill_color='black'
    window.add(ball)
    switch = False
    onmouseclicked(turn_on)
    while True:
        pause(DELAY)
        if switch==True:
            VY+=GRAVITY
            ball.move(VX,VY)
            pause(DELAY)
            if ball.y>window.height:
                VY=-REDUCE*VY
            if ball.x>window.width:
                ball.x=START_X
                ball.y=START_Y
                times +=1
            if times>=3:
                break
        else:
            pass

def turn_on(Event):
    global switch
    switch=True




if __name__ == "__main__":
    main()
