def wears_jacket(temp, raining):
  """
  integer, integer -> Boolean
  This function evaluates if the integer inputted for temp. It sees if the temp value is greater
  than 60. If the value is greater than 60, then the individual might not need to where a jacket.
  But the function will return true, if the integer inputted for raining is equal to 1. If the
  temp value is lower than 60 or the integer inputted for raining is 1, the function will have an
  output of True. The only way this function will return False is if, the temp value is greater 
  than 60 and the integer inputted for raining is not 1.

  >>> wears_jacket(52,1)
  True
  >>> wears_jacket(62,2)
  False
  >>> wears_jacket(63,1)
  True
  """
  if temp<60 or raining==1:
    return True
  else:
    return False
