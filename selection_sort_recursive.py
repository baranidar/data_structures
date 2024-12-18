def selection_sort(lst, length = 0):
  print("Start",lst, length)
  if length < 1:
      return lst
  
  min_val = lst[len(lst) - length]
  min_index = len(lst) - length
  print(min_val, min_index)
  for index,item in enumerate(lst):
      print(index, item, min_index)
      if index > min_index:
          if lst[index] < min_val:
              print("-->", lst[index], min_val)
              min_val = lst[index]
              min_index = index
  tmp = lst[len(lst) - length]
  lst[len(lst) - length] = min_val
  lst[min_index] = tmp
  return selection_sort(lst, length-1)
  
      
      
