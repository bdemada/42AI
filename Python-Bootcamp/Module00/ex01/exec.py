# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bde-mada <bde-mada@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 11:02:47 by bde-mada          #+#    #+#              #
#    Updated: 2023/02/03 11:50:47 by bde-mada         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
    args = sys.argv
    argc = len(args) - 1
    to_print = ""
    for n in range(argc, 0 , -1):
        revargs = args[n]
        revargs = revargs[::-1].swapcase()
        to_print += revargs
        if (n > 1):
            to_print += " "
    print(to_print)

if __name__ == '__main__':
    sys.exit(main())