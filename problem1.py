def opposite_sign(a,b):
  """
  integer, integer -> true or false
  This function is taking in two integers. If the integer that is inputted for a is greater than the value of the integer
  that is inputted for b, then the function will return true. If the numbers do not fulfill this statement, in all other
  scenarios, the function will return the word false.
  >>> opposite_sign(2,4)
  false
  >>> opposite_sign(4,2)
  true
  """
  if a>b:
    print("true")
  else:
    print("false")
