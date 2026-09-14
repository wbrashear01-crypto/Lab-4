def is_triangle(a,b,c):
  """
  positive integer, positive integer, positive integer -> Boolean
  This function is adding the positive integer values for a and b together. Then it is seeing if the sum of a and b is greater than c. If the sum of a and
  b is greater than c, then the function will return True. Because the sum of a and b being greater than c means that the side lengths do in fact create a
  triangle. If the sum of a and b are less than c, the function will return false, because then the side lengths, a and b do not create a triangle with the
  side length for c. For context each of the positive integers that are inputted for a,b and c are representative of potential side lengths of a triangle.

  >>> is_triangle(1,1,3)
  False
  >>> is_triangle(2,4,3)
  True
  >>> is_triangle(1,2,3)
  False
  """
  if a+b>c:
    return True
  else:
    return False


