import random
import signal
import sys

from UserInterface import CommandLineInterface


class Game(object):
    def __init__(self):
        self.turns = 30
        self.user_interface = CommandLineInterface()
        self.user_score = 0
        self.difficulty_level = 0
        self.users_correct_answer_streak = 0

    def play(self):
        self.user_interface.display_welcome()
        turn_counter = 0
        while turn_counter < self.turns:
            turn = self.Turn(self)
            turn.play_turn()
            turn_counter += 1
        self.user_interface.display_endgame(self.user_score, self.turns)

    def reset_user_streak(self):
        self.users_correct_answer_streak = 0

    def increase_user_score(self):
        self.user_score += 1
        self.users_correct_answer_streak += 1
        if self.users_correct_answer_streak == 5:
            self.increase_game_difficulty()

    def increase_game_difficulty(self):
        self.user_interface.display_increased_difficulty_message()
        self.difficulty_level += 1

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

            is_user_answer_correct = self.check_user_input(user_answer)
            self.game.increase_user_score() if is_user_answer_correct else self.game.reset_user_streak()
            self.ui.display_answer(self.answer) if not is_user_answer_correct else None

        def check_user_input(self, user_answer):
            return str(user_answer).isdigit() and int(user_answer) == self.answer


if __name__ == "__main__":
    game = Game()
    game.play()
