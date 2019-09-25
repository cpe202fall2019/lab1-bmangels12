
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
      return
   if len(int_list) < 1:
       return None
   largest = int_list[0]
   for num in int_list: 
       if num > largest:
           largest = num
   return largest

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
      return
   if len(int_list) == 0:
      return int_list
   return int_list[-1:] + reverse_rec(int_list[:-1])   


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass
   if int_list == None:
      raise ValueError
      return 
   if low == high:
      return None
   if int_list[low] == target:
      return low
   return bin_search(target, low + 1, high, int_list)
