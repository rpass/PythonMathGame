import unittest

from MathGame import Game


class GameTest(unittest.TestCase):
    def test_turn_answer_is_the_sum_of_the_operands(self):
        game = Game()
        turn = game.Turn(game)
        self.assertEqual(turn.answer, turn.operands[0] + turn.operands[1])
