
def insertion_sort(lst):
  for i in range(1,len(lst)):
      item = lst[i]
      j = i - 1
      while item < lst[j] and j >= 0:
          lst[j+1] = lst[j]
          j -= 1
      lst[j+1] = item
  return lst
      

lst = [29, 10, 14, 37, 13]
print(lst)
output = insertion_sort(lst)
print(output)
