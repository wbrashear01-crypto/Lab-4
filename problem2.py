def divisible_by_m(n,m):
  """
 integer, integer -> true or false
 This function is dividing the integer inputted for m by the integer inputted for n. If there is a remainder that is not
 equal to 0, then the function will have an output of False. If the remainder between the two integers is 0, the function
 will have an output of True.
 
  >>> divisible_by_m(3,2)
  False
  >>> divisible_by_m(0,4)
  True
  >>> divisible_by_m(-6, 2)
  True
  >>> divisible_by_m(-9,3)
  True
  >>> divisible_by_m(10,4)
  False
  >>> divisible_by_m(0,2000)
  True
  """
  if n%m==0:
    return True
  else:
    return False
