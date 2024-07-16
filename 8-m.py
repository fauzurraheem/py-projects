# def final(arr1, arr2):
#   newlist =[]
#   newlist.extend(arr1)
  
#   l = []
#   l.extend(arr2)
  
#   print(l, "l", newlist, "n")
  
#   if len(arr1)  < 1:
#     print(arr1,arr2  ," no arr1")
#     return newlist.extend(arr2)
#   for i,x in enumerate(l):      
#       print(i,x, "bg")
#       if newlist[i] != newlist[len(newlist) - 1]:
#         if l[i] > newlist[i] and  l[i] < newlist[i+1]:
#           newlist.insert(i+1, x)
#       elif l[i] > newlist[0] :
#         newlist.insert(1,x)
#       else:
#         newlist.insert(len(newlist) - 1, x)
  
#   print(newlist,"newlist")
#   return newlist



# def divide(arr1,arr2):
#   r1  =[]
#   if len(arr1) <= 1 and len(arr2) <= 1:
#     print(arr1,arr2)
#     r1.extend(final(arr1,arr2))
#     print(r1)
#     return r1
    
#   first = arr1[:len(arr1)//2]
#   second = arr1[len(arr1)//2:]
  
#   print(first, second, "arr1")
  
  
#   first2 = arr2[:len(arr2)//2]
#   second2 = arr2[len(arr2)//2:]
  
#   print ( first2,second2, "arr2")
  
#   r1.extend(final(divide(first,second),divide(first2,second2)))
  
  
#   print(r1, "r1")
#   return r1
  
  
# divide([7,4,8,8],[3,9,7,5])

    


def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  
  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]
  
  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)
  
  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0
  
  
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
      
  result.extend(left[i:])
  result.extend(right[j:])

  return result



unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)



# / =========================================Bubble sort===================================


my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Sorted array:", my_array)