"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE=10
window= GWindow()
dot_number=0
dot = GOval(SIZE, SIZE)
x=0
y=0

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(function)



def function(dot):
    global dot_number,SIZE,x,y
    dot_number += 1
    dot.filled= True
    dot.fill_color= 'black'
    if dot_number%2==0:
        maybe_object=  window.get_object_at(x, y)
        window.remove(maybe_object)
        dot = GLine(x, y, dot.x, dot.y)
        window.add(dot)
    else:
        x = dot.x
        y = dot.y
        dot=GOval(SIZE,SIZE,x=dot.x - SIZE / 2, y=dot.y - SIZE / 2)
        window.add(dot)






if __name__ == "__main__":
    main()
