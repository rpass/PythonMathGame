import random
import signal
import sys

from UserInterface import CommandLineInterface


class Game(object):
    def __init__(self):
        self.turns = 30
        self.user_interface = CommandLineInterface()
        self.user_score = 0

    def play(self):
        self.user_interface.display_welcome()
        turn_counter = 0
        while turn_counter < self.turns:
            turn = self.Turn(self)
            turn.play_turn()
            turn_counter += 1
        self.user_interface.display_endgame(self.user_score, self.turns)

    class Turn(object):
        def __init__(self, this_game):
            self.game = this_game
            operand_range_min = 1
            operand_range_max = 9
            self.operands = (random.randint(operand_range_min, operand_range_max),
                             random.randint(operand_range_min, operand_range_max))
            self.answer = self.operands[0] + self.operands[1]
            self.ui = self.game.user_interface

        def play_turn(self):
            def turn_timeout_handler(signum, stack):
                self.ui.display_out_of_time_message()
                sys.exit()

            def register_timer():
                signal.signal(signal.SIGALRM, turn_timeout_handler)

            def end_timer():
                signal.alarm(0)

            def start_timer():
                signal.alarm(4)

            register_timer()
            start_timer()
            user_answer = self.ui.ask_question(self.operands)
            end_timer()

            user_answer_is_correct = self.process_user_input(user_answer)
            self.ui.display_answer(self.answer) if not user_answer_is_correct else None

        def process_user_input(self, user_answer):
            users_answer_is_valid_and_correct = str(user_answer).isdigit() and int(user_answer) == self.answer

            if users_answer_is_valid_and_correct:
                self.game.user_score += 1
                return True
            else:
                return False


if __name__ == "__main__":
    game = Game()
    game.play()
