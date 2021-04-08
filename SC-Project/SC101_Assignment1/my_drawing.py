"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine, GArc, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    lovely Patrick Star !!
    """
    window=GWindow(width=400,height=500)
    body=GPolygon()
    body.add_vertex((150,150))
    body.add_vertex((250,150))
    body.add_vertex((275,350))
    body.add_vertex((125,350))
    body.filled=True
    body.color='pink'
    body.fill_color='pink'
    window.add(body)

    head=GOval(100,100,x=150,y=100)
    head.filled= True
    head.fill_color= 'pink'
    head.color='pink'
    window.add(head)

    upleg=GRect(150,75,x=125,y=350)
    upleg.filled= True
    upleg.color= 'seagreen'
    upleg.fill_color='seagreen'
    window.add(upleg)

    lleg=GRect(60,10,x=125, y=425)
    lleg.filled= True
    lleg.color = 'seagreen'
    lleg.fill_color = 'seagreen'
    window.add(lleg)

    rleg = GRect(60, 10, x=215, y=425)
    rleg.filled = True
    rleg.color = 'seagreen'
    rleg.fill_color = 'seagreen'
    window.add(rleg)

    lfeet=GPolygon()
    lfeet.add_vertex((135, 435))
    lfeet.add_vertex((175, 435))
    lfeet.add_vertex((155, 460))
    lfeet.filled = True
    lfeet.color = 'pink'
    lfeet.fill_color = 'pink'
    window.add(lfeet)

    rfeet = GPolygon()
    rfeet.add_vertex((225, 435))
    rfeet.add_vertex((265, 435))
    rfeet.add_vertex((245, 460))
    rfeet.filled = True
    rfeet.color = 'pink'
    rfeet.fill_color = 'pink'
    window.add(rfeet)

    leyebrow1 = GLine(165,150,185,147)
    leyebrow1.fill='black'
    window.add(leyebrow1)
    leyebrow2 = GLine(165, 155, 185, 152)
    leyebrow2.fill = 'black'
    window.add(leyebrow2)
    leyebrow3= GLine(165,160,185,157)
    leyebrow3.fill='black'
    window.add(leyebrow3)

    reyebrow1= GLine(215,147,235,150)
    reyebrow1.fill = 'black'
    window.add(reyebrow1)
    reyebrow2= GLine(215,152,235,155)
    reyebrow2.fill = 'black'
    window.add(reyebrow2)
    reyebrow3= GLine(215,157,235,160)
    reyebrow3.fill = 'black'
    window.add(reyebrow3)

    leye=GOval(35,75,x=165,y=170)
    leye.filled=True
    leye.fill_color='white'
    window.add(leye)

    reye = GOval(35, 75, x=200, y=170)
    reye.filled = True
    reye.fill_color = 'white'
    window.add(reye)

    lcore= GOval(10,10,x=180,y=205)
    lcore.filled = True
    lcore.fill_color = 'black'
    lcore.color= 'black'
    window.add(lcore)

    rcore = GOval(10, 10, x=210, y=205)
    rcore.filled = True
    rcore.fill_color = 'black'
    rcore.color = 'black'
    window.add(rcore)

    smile=GArc(100,50,180,180,x=150,y=265)
    window.add(smile)

    lhand=GPolygon()
    lhand.add_vertex((75,250 ))
    lhand.add_vertex((125, 350))
    lhand.add_vertex((200, 350))
    lhand.filled = True
    lhand.color = 'pink'
    lhand.fill_color = 'pink'
    window.add(lhand)

    rhand = GPolygon()
    rhand.add_vertex((325, 250))
    rhand.add_vertex((275, 350))
    rhand.add_vertex((200, 350))
    rhand.filled = True
    rhand.color = 'pink'
    rhand.fill_color = 'pink'
    window.add(rhand)

    line=GLine(75,250,75,100)
    window.add(line)

    ball= GOval(100,75,x=35,y=50)
    ball.filled=True
    ball.fill_color='red'
    window.add(ball)

    label=GLabel('Stancode_SC101',x=40,y=95)
    label.color='white'
    window.add(label)

if __name__ == '__main__':
    main()
