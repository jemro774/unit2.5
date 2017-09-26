#Jack Robey
#9/20/17
#house.py - displays an image of a house

from ggame import *

purple = Color(0x8c03c6,1)
red = Color(0xFF0000,1)
yellow = Color(0xfcfc02,1)
brown = Color(0x3f3f36,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

yellowRectangle1 = RectangleAsset(50,50,blackOutline,yellow)
yellowRectangle2 = RectangleAsset(50,50,blackOutline,yellow)
purpleRectangle = RectangleAsset(250,250,blackOutline,purple)
redTriangle = PolygonAsset([(450,250), (625,100), (800,250)],blackOutline,red)
brownRectangle = RectangleAsset(50,80,blackOutline,brown)

Sprite(purpleRectangle,(500,250))
Sprite(redTriangle)
Sprite(yellowRectangle1,(535,300))
Sprite(yellowRectangle2,(665,300))
Sprite(brownRectangle,(600,420))
App().run()


