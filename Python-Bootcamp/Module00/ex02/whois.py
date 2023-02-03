# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bde-mada <bde-mada@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 11:49:37 by bde-mada          #+#    #+#              #
#    Updated: 2023/02/03 13:08:55 by bde-mada         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def is_intstring(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def main():
    args = sys.argv
    argc = len(args)
    if(argc != 2):
        print("AssertionError: more than one argument are provided")
    elif(is_intstring(args[1]) == False):
        print("AssertionError: argument is not an integer")
    elif(int(args[1]) == 0):
        print("I'm zero")
    elif(int(args[1]) % 2 == 0):
        print("I'm even")
    else:
        print("I'm odd")

if __name__ == '__main__':
    sys.exit(main())