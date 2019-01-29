# Write your average function here:
def average(num1, num2):
  average = (num1+num2)/2
  return average

# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

#-------------------------------------------------------------

# Write your tenth_power function here:
def tenth_power(num):
  resp = num**10
  return resp
# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

#-----------------------------------------------------------

# Write your introduction function here:
def introduction(first_name, last_name):
  newname = last_name + ', ' + first_name + ' ' + last_name
  return newname
# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

#-----------------------------------------------------------

# Write your square_root function here:
def square_root(num):
  raiz = num**(1/2)
  return raiz
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

#-----------------------------------------------------------# Write your tip function here:
def tip(total, percentage):
  haha = 100/ percentage
  result = total/haha
  return result
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0
