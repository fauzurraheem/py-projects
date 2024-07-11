

class Number():
  def __init__(self,num) -> None:
    self.num = num
    self.current = num
    
  def add(self) -> int:
    value = 0
    for i,each in enumerate(self.current):
      value += int(each) ** 2
    self.current = str(value)
    return value
  
  def __str__(self) -> str:
    return f"current value {self.current}"
  
  
def initiate(value, max):
  num = Number(value)
  
  loop = True
  count = 0
  
  while loop:
    if count == int(max) : 
      print(f"stooped at {count} steps")
      print(f"{value } is not an happy number")
      loop = False
      count = count + 1
    else:
      cvalue = num.add()
      print(num)
      count = count + 1
      if cvalue == 1:
        loop = False
        print(f"{value} is a happy number")
    
  
def mainFunc():
  
  loop = True
  
  while loop:
    
    digit = input("Enter a digit: ")
    max = input("Enter a max steps: ")
    
    if digit.isdigit() and max.isdigit():
      loop = False
      initiate(digit,max)
    else:
      print("Please enter valid numbers")
      
mainFunc()