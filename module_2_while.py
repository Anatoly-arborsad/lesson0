my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
for i in range(len(my_list)):
    if my_list [i] > 0:
        print (my_list[i])
    elif my_list[i] == 0: # без этих двух
        continue          # строк тоже работает              
    elif my_list[i]<0:
        break

