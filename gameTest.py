import unittest

from game import Game, format_operand


class GameTest(unittest.TestCase):
    def test_turn_answer_is_the_sum_of_the_operands(self):
        game = Game()
        turn = game.Turn()
        self.assertEqual(turn.answer, turn.operands[0] + turn.operands[1])


class FormatTesting(unittest.TestCase):
    def test_operand_formats_positive_integers_correctly(self):
        operand = 30
        self.assertEqual(format_operand(operand), "   30")

    def test_operand_formats_negative_integers_correctly(self):
        operand = -70
        self.assertEqual(format_operand(operand), "  -70")

    def test_operand_formats_larger_than_expected_numbers_correctly(self):
        operand = 1234567
        self.assertEqual(format_operand(operand), str(operand))
