import arcade
from pyglet.event import EVENT_HANDLE_STATE


class Game(arcade.Window):
    def on_draw(self) -> EVENT_HANDLE_STATE:
        self.clear((255, 255, 255))





if __name__ == '__main__':
    window = Game()
    arcade.run()
