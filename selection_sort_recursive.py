def selection_sort(lst, length = 0):
  if length == 0:
      length = len(lst)
  if length == 0:
      return lst
  print(lst, length)
  min_val = lst[len(lst) - length]
  min_index = len(lst) - length
  #print(min_val, min_index)
  for index,item in enumerate(lst):
      #print(index, item, min_index)
      if index > min_index:
          if lst[index] < min_val:
              #print("-->", lst[index], min_val)
              min_val = lst[index]
              min_index = index
  tmp = lst[len(lst) - length]
  lst[len(lst) - length] = min_val
  lst[min_index] = tmp
  if length-1 > 0:
      return selection_sort(lst, length-1) 
  else:
      return lst
  
lst = [29, 10, 14, 37, 13]
output = selection_sort(lst)
print(output)
