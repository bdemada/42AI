# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bde-mada <bde-mada@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 13:16:33 by bde-mada          #+#    #+#              #
#    Updated: 2023/02/23 18:17:22 by bde-mada         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

kata = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf'
	}

def	main():
	lenght = len(kata)
	for i in range(len(kata)):
		print(f'{list(kata.keys())[i]} was created by {list(kata.values())[i]}')

if __name__ == '__main__':
	sys.exit(main())