#Jack Robey
#9/26/17
#germany.py - displays the German flag

from ggame import *

black = Color(0x000000,1)
red = Color(0xFF0000,1)
gold = Color(0xFFCC00,1)

blackOutline = LineStyle(1,black)

blackRectangle = RectangleAsset(500,100,blackOutline,black)
redRectangle = RectangleAsset(500,100,blackOutline,red)
goldRectangle = RectangleAsset(500,100,blackOutline,gold)

Sprite(blackRectangle,(250,50))
Sprite(redRectangle,(250,50))
Sprite(goldRectangle,(250,50))
App().run()
