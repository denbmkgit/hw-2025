import arcade

SCREEN_WIDTH =800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong Game"

class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__()


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
    
    def on_draw(self):
        self.clear((255, 255, 255))





if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
