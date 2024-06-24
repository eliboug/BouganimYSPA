import math

# This is Leibniz's formula for pi

# change this to adjust how many iterations of the formula to include
term_count = 1000

isPositive = True
final_term = 0
for k in range(term_count):
    if isPositive:
        final_term += 1 / (2 * k + 1)
        isPositive = False
    else:
        final_term -= 1 / (2 * k + 1)
        isPositive = True

# displaying the value I found
print(final_term)

# displaying the known value of pi/4
print(math.pi / 4)


