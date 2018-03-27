def min_num_in_list( list ):
     min = list[0]
     for a in list:
        if a > min:
           min = a
     return min
print(min_num_in_list([5,6,9,90]))
