import math
from decimal import Decimal, getcontext





def upToCount(n):
  terms = 1000000
  # set precision to be higher for accuracy
  getcontext().prec = n +10
  
  pi = Decimal(0)
  for i in range(terms):
    print((-1)**i,"first",i)
    print(2*i+1,"second")
    term = Decimal(-1**i)/Decimal(2*i+1)
    pi += term
  
  pi =  4* pi
  
  # Format pi to the desired number of decimal places
  pis = f"{pi:.{n}f}"
  
  print(pis)
  
  
def getInput():
  value = "d"
  
  while type(value) != type(2):
    try:
      value = int(input("Please enter a number"))
    except: 
      print("not a number, Try again")

      
  upToCount(value)
 
getInput() 
