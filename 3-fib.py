


def fibFunc(n):
  fibList = [0,1]
  a = 0
  b = 1
  for x in range(n - 2):
    fib = a+b
    a = b
    b = fib 
    fibList.append(fib)   
  print(fibList)

def inputN():
  value = "d"
  
  while type(value) != type(2):
    try:
      value = int(input("Please enter a number"))
    except: 
      print("not a number, Try again")
      
  fibFunc(value)
  
inputN()