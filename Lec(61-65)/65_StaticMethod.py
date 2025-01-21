class Game:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def start():
        print("Game has started!")

    @staticmethod
    def end():
        print("Game has ended!")

# Example usage
Game.start()
Game.end()
a = Game("Chess")
print(a.name)