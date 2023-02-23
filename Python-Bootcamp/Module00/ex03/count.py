# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bde-mada <bde-mada@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 12:14:26 by bde-mada          #+#    #+#              #
#    Updated: 2023/02/23 17:00:02 by bde-mada         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def text_analyzer(input = ""):
	"""This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
	if input == "":
		print("What is the text to analyze?")
		exit(-1)
	if not type(input) is str:
		print("AssertionError: argument is not a string")
		exit(-1)
	upper = 0
	lower = 0
	spaces = 0
	punctuation = 0
	length = len(input)
	for c in input:
		if c.isupper():
			upper += 1
		if c.islower():
			lower += 1
		if c == ' ':
			spaces += 1
		if c in string.punctuation:
			punctuation += 1
	print(f"The text contains {length} character(s):\n- {upper} upper letter(s)\n\
- {lower} lower letter(s)\n- {punctuation} punctuation mark(s)\n- {spaces} space(s)")
	
def main():
	args = sys.argv
	argc = len(args)
	if argc != 2:
		print(f"You inserted {argc - 1} arguments. The imput should be a single string \
between single or double quotes")
		exit(-1)
	text_analyzer(args[1])
	

if __name__ == '__main__':
    sys.exit(main())
