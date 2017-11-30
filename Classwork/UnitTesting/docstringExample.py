import math
def abs_square(x):
	"""Return the square root of the absolute value of a number."""
	return math.sqrt(abs(x))


print(abs_square.__doc__)
abs_square(-4)
