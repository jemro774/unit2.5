#Jack Robey
#9/20/17
#house.py - displays a picture of a house

from ggame import *

purple = Color(0x8c03c6,1)
red = Color(0xFF0000,1)
yellow = Color(0xfcfc02,1)
brown = Color(0x3f3f36,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

purpleRectangle = RectangleAsset(200,200,blackOutline,purple)

Sprite(purpleRectangle)



