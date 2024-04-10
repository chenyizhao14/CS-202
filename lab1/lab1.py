
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError()

   if not int_list:
      return None

   max = int_list[0]
   for val in int_list[1:]:
      if val > max:
         max = val

   return max

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError()

   if not int_list:
      return []

   return [int_list[-1]] + reverse_rec(int_list[:-1])

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list is None:
      raise ValueError()

   if not int_list:
      return None

   if (target > int_list[len(int_list) - 1]) or (target < int_list[0]):
      return None

   if high < low:
      return None

   mid = (high + low)//2 #finds the middle number
   if target == int_list[mid]:
      return mid

   if target < int_list[mid]:
      return bin_search(target, low, mid - 1, int_list)
   else:
      return bin_search(target, mid + 1, high, int_list)

# Signature: Maybe_List -> None
# Purpose: Reverse the original input list 
def reverse_list_mutate(int_list):
   '''Reverses a list, modifies the input list, returns None
   If list is None, raises ValueError'''
   if int_list is None:
      raise ValueError()

   if not int_list:
      return None

   for i in range(len(int_list)//2):
      x = int_list[i]
      int_list[i] = int_list[-i - 1]
      int_list[-i - 1] = x

   return None