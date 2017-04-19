import unittest

from game import Game


class GameTest(unittest.TestCase):
    def test_turn_answer_is_the_sum_of_the_operands(self):
        game = Game()
        turn = game.Turn(game)
        self.assertEqual(turn.answer, turn.operands[0] + turn.operands[1])


class CommandLineInterfaceTest(unittest.TestCase):
    def test_operand_formatter_formats_positive_integers_correctly(self):
        game = Game()
        operand = 30
        self.assertEqual(game.user_interface.format_operand(operand), "   30")

    def test_operand_formatter_formats_negative_integers_correctly(self):
        game = Game()
        operand = -70
        self.assertEqual(game.user_interface.format_operand(operand), "  -70")

    def test_operand_formatter_formats_larger_than_expected_numbers_correctly(self):
        game = Game()
        operand = 1234567
        self.assertEqual(game.user_interface.format_operand(operand), str(operand))
