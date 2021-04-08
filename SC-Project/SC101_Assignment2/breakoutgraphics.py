"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).
P_X=0                  # Calculate position_x
P_Y=0                  # Calculate position_y
COUNT=1


INITIAL_Y_SPEED = 5.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        self.ball_radius = ball_radius
        self.__dx=0
        self.__dy=0

        self.set_ball_v()

        # Create a graphical window, with some extra space.
        self.paddle_offset = paddle_offset
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow (width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.paddle= GRect(width=paddle_width,height=paddle_height,x=(self.window_width-paddle_width)/2,y=self.window_height-brick_offset)
        self.paddle.filled=True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball=GOval(self.ball_radius*2,self.ball_radius*2,x=self.window_width/2-ball_radius,y=self.window_height/2-ball_radius)
        self.ball.filled=True
        self.ball.fill_color='black'
        self.window.add(self.ball)

        # Initialize our mouse listeners.
        self.switch = False
        onmousemoved(self.function1)
        onmouseclicked(self.turn_on)

        # Draw bricks.
        self.cols = brick_cols
        self.rows = brick_rows
        self.width = BRICK_WIDTH
        self.height = BRICK_HEIGHT
        self.space = BRICK_SPACING
        self.brick_offset= BRICK_OFFSET
        self.px = P_X
        self.py = P_Y+ BRICK_OFFSET
        self.count=COUNT

        for i in range(1,self.cols+1):
            for j in range(1,self.rows+1):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled=True
                if self.count<=self.cols/5:
                    self.brick.fill_color='red'
                elif self.cols/5<self.count<=2*self.cols/5:
                    self.brick.fill_color = 'orange'
                elif 2*self.cols/5<self.count<=3*self.cols/5:
                    self.brick.fill_color='yellow'
                elif 3*self.cols/5<self.count<=4*self.cols/5:
                    self.brick.fill_color= 'green'
                elif 4*self.cols/5<self.count<=self.cols:
                    self.brick.fill_color= 'blue'
                self.window.add(self.brick,x=self.px, y=self.py)
                self.px+=self.width+self.space
            self.px=0
            self.py+=self.height+self.space
            self.count+=1

    def function1(self,event):
        self.paddle.y = self.window.height - self.paddle_offset
        if self.paddle.width/2 <= event.x <= self.window.width-self.paddle.width/2:
            self.paddle.x=event.x-self.paddle.width/2
        elif event.x<=self.paddle.width/2:
            self.paddle.x=0
        else:
            self.paddle.x=self.window.width-self.paddle.width

    def set_ball_p(self):
        self.ball.x=self.window_width/2-self.ball_radius
        self.ball.y=self.window.height/2-self.ball_radius
        
    # Default initial velocity for the ball.
    def set_ball_v(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if (random.random() > 0.5):
            self.__dx = -self.__dx
        if (random.random()>0.5):
            self.__dy=-self.__dy

    def getter(self):
        return self.__dx, self.__dy

    # click to start
    def turn_on(self,event):
        self.switch = True

    def ball_under_paddle(self):
        is_ball_under_paddle= self.ball.y>= self.window.height-self.paddle_offset
        return is_ball_under_paddle

    def reset_ball(self):
        self.set_ball_p()
        while self.ball_under_paddle():
            self.set_ball_p()
        self.set_ball_v()
        self.window.add(self.ball)
