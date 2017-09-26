#Jack Robey
#9/26/17
#warmup5.py - displays a yellow diamond with the user's name inside in blue

from ggame import *

yellow = Color(0xFFFF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

yellowDiamond = PolygonAsset([(300,300), (500,500), (700,300), (500,100)],blackOutline,yellow)
text = TextAsset('Jack', fill=blue, style='bold 40pt Times')

Sprite(yellowDiamond)
Sprite(text,(460,300))
App().run()