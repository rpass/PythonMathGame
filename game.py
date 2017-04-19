import random


def format_operand(operand):
    padding_spaces = " " * (5 - len(str(operand)))
    return padding_spaces + str(operand)


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
            operand_range_min = 1
            operand_range_max = 100
            self.operands = (random.randint(operand_range_min, operand_range_max),
                             random.randint(operand_range_min, operand_range_max))
            self.question = "%s\n%s +\n ----" % (format_operand(self.operands[0]),
                                                 format_operand(self.operands[1]))
            self.answer = self.operands[0] + self.operands[1]
            self.answer_string = "%s" % format_operand(self.answer)

        def play_turn(self):
            input(self.question)
            print(self.answer_string + "\n")


if __name__ == "__main__":
    game = Game()
    game.play()
