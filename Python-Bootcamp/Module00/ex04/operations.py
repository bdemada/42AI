# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bde-mada <bde-mada@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 12:16:40 by bde-mada          #+#    #+#              #
#    Updated: 2023/02/03 13:14:50 by bde-mada         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def is_intstring(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def calculate(a, b):
    print(f'Sum:         {a + b}')
    print(f'Difference:  {a - b}')
    print(f'Product:     {a * b}')
    if (b == 0):
        print("ERROR (division by zero)")
        print("ERROR (modulo by zero)")
        exit()
    print(f'Quotient:    {a / b}')
    print(f'Remainder:   {a % b}')

def main():
    argv = sys.argv
    argc = len(argv)
    if (argc > 3):
        print("Incorrect argument number!")
        exit()
    elif (argc == 2):
        print("Usage: python3 operations.py <number1> <number2> \
\nExample:\n\t python operations.py 10 3")
        exit()
    if (is_intstring(argv[1]) == False or
            is_intstring(argv[2]) == False):
        print("AssertionError: only integers")
        exit()
    a = int(argv[1])
    b = int(argv[2])
    calculate(a, b)

if __name__ == '__main__':
    sys.exit(main())