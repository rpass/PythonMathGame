import unittest

from game import Game


class GameTest(unittest.TestCase):
    def test_turn_answer_is_the_sum_of_the_operands(self):
        game = Game()
        turn = game.Turn()
        self.assertEqual(turn.answer, str(turn.operands[0] + turn.operands[1]))
