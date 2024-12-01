immutable_var = 1,2,'a','b'
print('Immutable tuple:', immutable_var)
# immutable_var[3]=200 значение элементов кортежа нельзя изменить,т.к. кортеж относится
# к неизменяемым типам данных
mutable_list=[1,2,'a','b','c']
mutable_list[4]='Modified'
print('Mutable list:', mutable_list)