import random


class Game(object):
    def __init__(self):
        self.turns = 30

    def play(self):
        turn_counter = 0
        while turn_counter < self.turns:
            turn = self.Turn()
            turn.play_turn()
            turn_counter += 1
        print("Thank you for playing!")

    class Turn(object):
        def __init__(self):
            self.operands = (random.randint(-100, 100), random.randint(-100, 100))
            self.question = "%d + %d = ?" % self.operands
            self.answer = "%d" % (self.operands[0] + self.operands[1])

        def play_turn(self):
            print(self.question)
            input()
            print(self.answer)


if __name__ == "__main__":
    game = Game()
    game.play()
