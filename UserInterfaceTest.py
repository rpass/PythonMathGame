import unittest

from UserInterface import CommandLineInterface


class CommandLineInterfaceTest(unittest.TestCase):
    def setUp(self):
        self.cli = CommandLineInterface()

    def test_operand_formatter_formats_positive_integers_correctly(self):
        operand = 30
        self.assertEqual(self.cli.format_operand(operand), "   30")

    def test_operand_formatter_formats_negative_integers_correctly(self):
        operand = -70
        self.assertEqual(self.cli.format_operand(operand), "  -70")

    def test_operand_formatter_formats_larger_than_expected_numbers_correctly(self):
        operand = 1234567
        self.assertEqual(self.cli.format_operand(operand), str(operand))
