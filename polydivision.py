# POLYNOMIAL DIVISION

# GIVEN A POLYNOMIAL AND A SECOND POLYNOMIAL, DIVIDE THE
# FIRST POLYNOMIAL WITH THE SECOND, FIND THE RESULTING
# EQUATION AND THE REMAINDER

# INPUT:
#   c1: coefficients of the first equation, each is separated by a space (len(c1) > 0)
#   c2: coefficients of the first equation, each is separated by a space (len(c2) > 0)

# OUTPUT:
#   equation: the resulting coefficients from the division
#   remainder: the remainder coefficients


# EXAMPLE:
#   INPUT:
#       c1 = 18 27 -4 9 2 -8
#       results in the first equation 18x⁵ + 27x⁴ -4x³ + 9x² + 2x -8
#       
#       c2 = 7 12 4
#       results in the second equation 7x² + 12x + 4
#
#   OUTPUT:
#       equation = 18/7 x³ - 27/49 x² - 376/343 x + 8355/2401
#       r = - 84930/2401 x - 52628/2401
#
#   Due to the fractions library being used in this file, fractions like 18/7 is displayed as Fraction(18,7)

from fractions import Fraction
import sys

# ===== INPUT =====

c1 = input("First equation coefficients: ")
c1 = c1.split(" ")
for i, num in enumerate(c1):
    c1[i] = int(c1[i])
print("Equation 1 coefficients:", c1)

c2 = input("Second equation coefficients: ")
c2 = c2.split(" ")
for i, num in enumerate(c2):
    c2[i] = int(c2[i])
print("Equation 2 coefficients:", c2)

if len(c2) >= len(c1):
    print("Divisor equation power cannot be higher than Dividend")
    sys.exit()

# ===== CALC =====
equation = []
l1 = len(c1)
l2 = len(c2)
powerdiff = l1 - l2

for i in range(powerdiff + 1):
    if c1[i] != 0:
        coef = Fraction(c1[i],c2[0])
        equation.append(coef)
        for g in range(l2):
            c1[i + g] -= coef * c2[g]

remainder = c1
while remainder[0] == 0:
    remainder.pop(0)
    if len(remainder) == 0:
        break

print("remainder:",remainder)
print("resulting equation:",equation)

        
