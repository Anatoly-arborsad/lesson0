my_dict={'Andrey':1974, 'Rinat': 1977, 'Felix':1982}
print("Dict:",my_dict)
print('Existing values:',my_dict['Felix'])
print('Not existing values:', my_dict.get('Denis'))
my_dict.update({'Radik': 1956, 'Oleg':1983})
a=my_dict.pop('Andrey')
print('Deleted value:',a)
print('Modifid dictionary:',my_dict)
my_set={1,2,3,'Яблоко',"aple",3.14, 'aple', "Яблоко",1,2,3,3.14}
print('Set:',my_set)
my_set.discard(1)
my_set.update([(7,8,9),'Слива'])
print('Modifid set:',my_set)