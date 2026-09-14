def pythagorean_triples(a,b,c):
  """
  integer, integer, integer -> Boolean
  This function takes the integers inputted for a and b, it squares them and then adds them together. On the right-hand side
  of the function, it takes the integer inputted for c and squares it. If the values of a and b squared and added together equal
  the value of c squared, the function outputs True. If the values of a and b squared and added together are not equal to the
  value of c squared, the function outputs False.

  >>> pythagorean_triples(1,1,3)
  False
  >>> pythagorean_triples(1,0,1)
  True
  >>> pythagorean_triples(2,2,2)
  False
  """
  if (a**2)+(b**2)==(c**2):
    return True
  else:
    return False
