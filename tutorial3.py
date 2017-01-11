from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

green = Color(0x00ff00, 1)
black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, green)
bg = Sprite(bg_asset, (0,0))

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
