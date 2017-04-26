import unittest

from MathGame import Game


class GameTest(unittest.TestCase):
    def test_turn_answer_is_the_sum_of_the_operands(self):
        game = Game()
        turn = game.Turn(game)
        self.assertEqual(turn.answer, turn.operands[0] + turn.operands[1])

    def test_check_user_input_increments_game_score_for_correct_input(self):
        game = Game()
        turn = game.Turn(game)
        turn.ui = MockUI(turn)
        turn.play_turn()
        self.assertEqual(game.user_score, 1)

    def test_check_user_input_handles_none_string_input_as_an_incorrect_answer(self):
        game = Game()
        turn = game.Turn(game)
        user_answer = ''
        turn.check_user_input(user_answer)
        user_answer = 1
        turn.check_user_input(user_answer)
        user_answer = 'one'
        turn.check_user_input(user_answer)
        user_answer = '3.14'
        turn.check_user_input(user_answer)
        user_answer = '!@#$'
        turn.check_user_input(user_answer)
        # Unicode for sunglass face emoji
        user_answer = '\u1F60E'
        turn.check_user_input(user_answer)
        self.assertEqual(game.user_score, 0)

    def test_5_correct_answers_increases_difficulty_level_by_one(self):
        game = Game()

        for i in range(5):
            self.simulate_turn(MockUI, game)

        self.assertEqual(game.difficulty_level, 1)

    def simulate_turn(self, MockUI, game):
        turn = game.Turn(game)
        turn.ui = MockUI(turn)
        turn.play_turn()


class MockUI(object):
    def __init__(self, turn):
        self.correct_answer = turn.answer

    def ask_question(self, operands):
        return self.correct_answer


if __name__ == '__main__':
    unittest.main()
