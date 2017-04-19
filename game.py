import random


class Game(object):
    def __init__(self):
        self.turns = 30
        self.user_interface = self.CommandLineInterface()

    def play(self):
        self.user_interface.display_welcome()
        turn_counter = 0
        while turn_counter < self.turns:
            turn = self.Turn(self)
            turn.play_turn()
            turn_counter += 1
        print("Thank you for playing!")

    class Turn(object):
        def __init__(self, this_game):
            self.game = this_game
            operand_range_min = 1
            operand_range_max = 100
            self.operands = (random.randint(operand_range_min, operand_range_max),
                             random.randint(operand_range_min, operand_range_max))
            self.answer = self.operands[0] + self.operands[1]

        def play_turn(self):
            ui = self.game.user_interface
            ui.ask_question(self.operands)
            ui.display_answer(self.answer)

    class CommandLineInterface(object):
        @staticmethod
        def display_welcome():
            print("/ Hello, welcome to the math game \\")
            print("--------- Don't be fooled ---------")
            print("~~~~~~~~~~~~ ! Begin ! ~~~~~~~~~~~~")
            print()
            input(" Ready? \n")

        @staticmethod
        def format_operand(operand):
            padding_spaces = " " * (5 - len(str(operand)))
            return padding_spaces + str(operand)

        def prepare_question(self, operands):
            return "%s\n%s +\n ----" % (self.format_operand(operands[0]),
                                        self.format_operand(operands[1]))

        def ask_question(self, operands):
            question = self.prepare_question(operands)
            input(question)

        def display_answer(self, answer):
            print("%s\n" % self.format_operand(answer))


if __name__ == "__main__":
    game = Game()
    game.play()
