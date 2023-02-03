# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bde-mada <bde-mada@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 13:16:33 by bde-mada          #+#    #+#              #
#    Updated: 2023/02/03 15:51:24 by bde-mada         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf'
    }

def main():
    print('{0[0]} was created by {0[1]}'.format(kata))

if __name__ == '__main__':
    sys.exit(main())