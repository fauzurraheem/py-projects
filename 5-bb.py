# convert to binary and back

def toBinary(num, base = 2):
  binary = []
  
  loop = True
  
  remender = num
  
  while loop:
    if remender < base :
      binary.append(str(remender))
      
      loop = False
    else:
      mod = remender % base
      binary.append(str(mod))
      remender = remender // base
      
  binary.reverse()
  newB = "".join(binary)
      
  print(newB)
      
      
      
toBinary(49)


def toBasex(binary, base):
    value = 0
    significant = False
    
    # Reverse the string
    rBinary = reversed(binary)
    
    # Process the binary string to convert it to the given base
    for i, bit in enumerate(rBinary):
        if bit != '0':
            significant = True
        if significant:
            value += int(bit) * (base ** i)
    
    print(value)
    print("Significant bit encountered:", significant)

# Example usage:
toBasex("110001", 2)