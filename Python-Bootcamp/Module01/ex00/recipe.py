# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bde-mada <bde-mada@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 10:53:31 by bde-mada          #+#    #+#              #
#    Updated: 2023/02/03 10:57:03 by bde-mada         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class recipe:
    name str
    cooking_lvl int
    cooking_time int
    ingredients int
    description str
    recipe_type str (starter, lunch, dessert)

only description can be empty
in case of error, print the errors
implement __str__
