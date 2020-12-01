# -*- coding: utf-8 -*-

def main(notation):
    arrNotation = notation.split()
    stack = []
    operations = ['*', "-", '+', '/']

    for i in range(len(arrNotation)):
        if arrNotation[i] in operations:
            # если встречаем оператор, то берём из стека два последних значения и выполняем операцию
            second_operand = stack.pop()
            first_operand = stack.pop()
            derived = (eval(str(first_operand) + str(arrNotation[i]) + str(second_operand)))
            stack.append(derived)
            continue
        # Записываем операнд в стек
        stack.append(arrNotation[i])

    return int(stack[0])

print(main('4 2 10 * +'))
