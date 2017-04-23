class CommandLineInterface(object):
    @staticmethod
    def display_welcome():
        print("/ Hello, welcome to the math game \\")
        print("--------- Don't be fooled ---------")
        print("~~~~~~~~~~~~ ! Begin ! ~~~~~~~~~~~~")
        print()
        input(" Ready? \n")

    @staticmethod
    def format_operand(operand):
        padding_spaces = " " * (5 - len(str(operand)))
        return padding_spaces + str(operand)

    def prepare_question(self, operands):
        return "\n%s\n%s +\n ----\n" % (self.format_operand(operands[0]),
                                        self.format_operand(operands[1]))

    def ask_question(self, operands):
        question = self.prepare_question(operands)
        user_answer = input(question)
        return user_answer

    def display_answer(self, answer):
        print("%s" % self.format_operand(answer))

    @staticmethod
    def display_endgame(user_score, number_of_turns):
        print("Score: %d / %d" % (user_score, number_of_turns))
        print("Thank you for playing!")

    @staticmethod
    def display_out_of_time_message():
        print("Sorry! You are out of time.\nGoodbye")
