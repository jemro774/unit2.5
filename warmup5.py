#Jack Robey
#9/26/17
#warmup5.py - displays a yellow diamond with the user's name inside in blue

from ggame import *

blue = Color(0x0000FF,1)

blackOutline = LineStyle(1,black)

blueDiamond = PolygonAsset([(400,400), (600,600), (800,400), (600,200)],blackOutline,blue)