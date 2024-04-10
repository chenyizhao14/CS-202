def selection_sort(list):
    for i in range(len(list) - 1):
        min_spot = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_spot]:
                min_spot = j
        if i != min_spot:
            swap(list, i, min_spot) # Could also say list[i], list[min_spot] = list[min_spot], list[i]
      
# Not needed in Python, but useful in other languages      
def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
   
def insertion_sort(list):
    for i in range(1, len(list)):
        item = list[i]        
        j = i
        while j > 0 and list[j-1] > item:
            list[j] = list[j - 1]
            j -= 1
        list[j] = item
   
