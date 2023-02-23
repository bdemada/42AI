# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bde-mada <bde-mada@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/23 18:25:53 by bde-mada          #+#    #+#              #
#    Updated: 2023/02/23 23:53:10 by bde-mada         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def print_recipe_names(cookbook):
    i = 1


def main():
    cookbook = {'Sandwich' : dict(ingredients = ['ham', 'bread', 'cheese', 'tomatoes'], meal = 'lunch', prep_time = 10),
                    'Cake' : dict(ingredients = ['flour', 'sugar', 'eggs'], meal = 'dessert', prep_time = 60),
                    'Salad' : dict(ingredients = ['avocado', 'arugula', 'tomatoes', 'spinach'], meal = 'lunch', prep_time = 15)}
    print("Welcome to the Python Cookbook !")
    print("List of the available options:")
    print("   1: Add a recipe\n   2: Delete a recipe\n   3: Print a recipe")
    print("   4: Print the cookbook\n   5: Quit\n\nPlease select an option:")


if __name__ == '__main__':
    sys.exit(main())

