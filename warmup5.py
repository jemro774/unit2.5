#Jack Robey
#9/26/17
#warmup5.py - displays a yellow diamond with the user's name inside in blue

from ggame import *

blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

blueDiamond = PolygonAsset([(300,300), (500,500), (700,300), (500,100)],blackOutline,blue)
text = TextAsset('Jack', fill=black, style='bold 40pt Times')

Sprite(blueDiamond)
Sprite(text,(460,300))
App().run()