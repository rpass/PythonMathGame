import unittest

from MathGame import Game


class GameTest(unittest.TestCase):
    def test_turn_answer_is_the_sum_of_the_operands(self):
        game = Game()
        turn = game.Turn(game)
        self.assertEqual(turn.answer, turn.operands[0] + turn.operands[1])

    def test_process_user_input_increments_game_score_for_correct_input(self):
        game = Game()
        turn = game.Turn(game)
        user_answer = str(turn.answer)
        turn.process_user_input(user_answer)
        self.assertEqual(game.user_score, 1)

    def test_process_user_input_handles_no_input_as_an_incorrect_answer(self):
        game = Game()
        turn = game.Turn(game)
        user_answer = ''
        turn.process_user_input(user_answer)
        user_answer = 'one'
        turn.process_user_input(user_answer)
        user_answer = '3.14'
        turn.process_user_input(user_answer)
        user_answer = '!@#$'
        turn.process_user_input(user_answer)
        # Unicode for sunglass face emoji
        user_answer = '\u1F60E'
        turn.process_user_input(user_answer)
        self.assertEqual(game.user_score, 0)


if __name__ == '__main__':
    unittest.main()
