# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   kata03.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: bde-mada <bde-mada@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2023/02/03 13:16:38 by bde-mada          #+#    #+#              #
#   Updated: 2023/02/23 23:28:12 by bde-mada         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys

kata = "The right format"


def main():
    print(format(kata, '->042'), end='')


if __name__ == '__main__':
    sys.exit(main())
