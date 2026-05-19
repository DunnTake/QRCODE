# POLYNOMIAL DIVISION

# GIVEN A POLYNOMIAL AND A SECOND POLYNOMIAL, DIVIDE THE
# FIRST POLYNOMIAL WITH THE SECOND, FIND THE RESULTING
# EQUATION AND THE REMAINDER

# INPUT:
#   p1: power of the first equation (p1 < 0)
#   c1: coefficients of the first equation, each is separated by a space (len(c1) = len(p1) + 1)
#   p2: power of the second equation (p2 < 0)
#   c2: coefficients of the first equation, each is separated by a space (len(c2) = len(p2) + 1)

# OUTPUT:
#   e: the resulting equation from the division
#   r: the remainder


# EXAMPLE:
#   INPUT:
#       p1 = 5
#       c1 = 18 27 -4 9 2 -8
#       results in the first equation 18x⁵ + 27x⁴ -4x³ + 9x² + 2x -8
#       
#       p2 = 2
#       c2 = 7 12 4
#       results in the second equation 7x² + 12x + 4
#
#   OUTPUT:
#       e = 18/7 x³ - 27/49 x² - 376/343 x + 8355/2401
#       r = - 84930/2401 x - 52628/2401

from fractions import Fraction