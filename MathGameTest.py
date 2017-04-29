import unittest

from MathGame import Game


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.turn = self.game.Turn(self.game)

    def test_turn_answer_is_the_sum_of_the_operands(self):
        self.assertEqual(self.turn.answer, self.turn.operands[0] + self.turn.operands[1])

    def test_check_user_input_increments_game_score_for_correct_input(self):
        self.turn.ui = MockUI(self.turn)
        self.turn.play_turn()
        self.assertEqual(self.game.user_score, 1)

    def test_check_user_input_handles_none_string_input_as_an_incorrect_answer(self):
        user_answers = ['', 1, 'one', '3.14', '!@#$', '\u1F60E']
        for user_answer in user_answers:
            self.turn.check_user_input(user_answer)
        self.assertEqual(self.game.user_score, 0)

    def test_5_correct_answers_increases_difficulty_level_by_one(self):
        game = Game()

        for i in range(5):
            simulate_turn(MockUI, game)

        self.assertEqual(game.difficulty_level, 1)

    def test_4_correct_answers_1_incorrect_then_2_correct_answers_does_not_increase_difficulty(self):
        game = Game()

        for i in range(4):
            simulate_turn(MockUI, game)

        simulate_turn(DumbMockUI, game)
        simulate_turn(DumbMockUI, game)

        simulate_turn(MockUI, game)

        self.assertEqual(game.difficulty_level, 0)


class MockUI(object):
    def __init__(self, turn):
        self.correct_answer = turn.answer

    def ask_question(self, operands):
        return self.correct_answer


class DumbMockUI(object):
    def __init__(self, turn):
        self.correct_answer = turn.answer

    def ask_question(self, operands):
        return self.correct_answer - 1

    def display_answer(self, answer):
        pass


def simulate_turn(mock_ui, game):
    turn = game.Turn(game)
    turn.ui = mock_ui(turn)
    turn.play_turn()


if __name__ == '__main__':
    unittest.main()
