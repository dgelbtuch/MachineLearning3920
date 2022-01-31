#fibonacci recursive
def fib_recursion(n):
  #base case
  if n <= 1:
    return n
  else:
    #recursive case
    return fib_recursion(n-1) + fib_recursion(n-2)

#fibonacci imperative function
def fib_imperative(n):
  a = 0
  b = 1
  while(n > 1):
    #add the a and b and update b to that new value
    c = a + b
    a = b
    b = c
    n -= 1
  return c

#function for matrix multiplacation of matrix a * matrix b
def matrix_mult(a, b):
  #c is a 2 by 2 matrix which will fill in the values of a*b
  c = [[0,0],[0,0]]
  c[0][0] = (a[0][0]*b[0][0]) + (a[0][0]*b[0][1])
  c[1][0] = (a[1][0]*b[0][0]) + (a[1][0]*b[0][1])
  c[0][1] = (a[0][1]*b[1][0]) + (a[0][1]*b[1][1])
  c[1][1] = (a[1][1]*b[1][0]) + (a[1][1]*b[1][1])
  return c

def fib_matrix(n):
  #matrices a and b which are both 2 by 2 which have the same values
  a = [[1,1],[1,0]]
  b = [[1,1],[1,0]]
  while(n > 1):
    #continuously multiply a*b while updating b
    #this is the same affect as taking b^n
    b = matrix_mult(a, b)
    n -= 1
  #the value of the fibonacci sequence will be found in b[0][1]
  return b[0][1]