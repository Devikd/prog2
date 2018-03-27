def medium_num_in_list( list ):
     medium = list[0
     for a in list:
        if a > medium:
           medium = a
     return medium
print(medium_num_in_list([5,6,9,90]))
