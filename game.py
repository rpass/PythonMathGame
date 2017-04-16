import random

while True:
    operand_1 = random.randint(-100, 100)
    operand_2 = random.randint(-100, 100)
    input('%d + %d' % (operand_1, operand_2))
    print('= %d\n' % (operand_1 + operand_2))

