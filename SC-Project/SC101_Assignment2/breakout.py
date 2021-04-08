"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE =2000 / 120 # 120 frames per second.
NUM_LIVES = 3
dx=0
dy=0

def main():
    global dx,dy
    graphics = BreakoutGraphics()
    lives= NUM_LIVES
    dx,dy=graphics.getter() # getter設計用來 return coder端 隱藏的dx,dy
    while True:
        pause(FRAME_RATE)
        if graphics.switch:

            if graphics.ball_under_paddle():
                lives-=1
                if lives>=0:
                    graphics.reset_ball()
                else:
                    break
            graphics.ball.move(dx,dy)
            if graphics.ball.x<=0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                dx=-dx
            if graphics.ball.y<=0: #故意撞到底面不反彈
                dy=-dy
            check(graphics)




def check(graphics): #check whether the collision happened
    obj1=graphics.window.get_object_at(graphics.ball.x,graphics.ball.y)
    obj2=graphics.window.get_object_at(graphics.ball.x+graphics.ball.width,graphics.ball.y)
    obj3=graphics.window.get_object_at(graphics.ball.x+graphics.ball.width,graphics.ball.y+graphics.ball.height)
    obj4=graphics.window.get_object_at(graphics.ball.x,graphics.ball.y+graphics.ball.height)

    if obj1 is None:
        if obj2 is None:
            if obj3 is None:
                if obj4 is None:
                    pass
                else:
                    bounce(obj4,graphics)
            else:
                bounce(obj3,graphics)
        else:
            bounce(obj2,graphics)
    else:
        bounce(obj1,graphics)


# bounce & identify
def bounce(a,graphics):
    global dx,dy
    if a.y>= graphics.window.height/2: #在下半部的板子碰到只會反彈
        dy = -dy
    else:
        graphics.window.remove(a)
        dy = -dy



if __name__ == '__main__':
    main()
