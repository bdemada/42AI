# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bde-mada <bde-mada@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/23 18:25:53 by bde-mada          #+#    #+#              #
#    Updated: 2023/02/24 09:47:39 by bde-mada         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def print_recipe_names(cookbook):
    for pos in range(len(list(cookbook.keys()))):
        print(f"Recipe {pos + 1}: {list(cookbook.keys())[pos]}")


def print_recipe_details(cookbook, recipe):
    for pos in range(len(list(cookbook.keys()))):
        if list(cookbook.keys())[pos] == recipe:
            print(f'Ingredients:')
            print(f'Meal: {cookbook[recipe]["meal"]}')
            print(f'Meal: {cookbook[recipe]["prep_time"]} min')


    
def main():
    cookbook = {'Sandwich' : dict(ingredients = ['ham', 'bread', 'cheese', 'tomatoes'], meal = 'lunch', prep_time = 10),
                    'Cake' : dict(ingredients = ['flour', 'sugar', 'eggs'], meal = 'dessert', prep_time = 60),
                    'Salad' : dict(ingredients = ['avocado', 'arugula', 'tomatoes', 'spinach'], meal = 'lunch', prep_time = 15)}
    print("Welcome to the Python Cookbook !")
    print("List of the available options:")
    print("   1: Add a recipe\n   2: Delete a recipe\n   3: Print a recipe")
    print("   4: Print the cookbook\n   5: Quit\n\nPlease select an option:")
    print(cookbook)
    print_recipe_names(cookbook)
    print_recipe_details(cookbook, 'Sandwich')


if __name__ == '__main__':
    sys.exit(main())

