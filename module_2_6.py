from random import randint


#Первый вариант с введением числа от пользователя:
#print('Введите число от 3 до 20 :')
#n = int(input())

# Второй вариант числа меняются случайным образом:
nambers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n = randint(3,21)
print(n)
parol =[]

for i in range(len(nambers)):
    for j in range(i+1,len(nambers)):
        summ = nambers[i]+nambers[j]
        if n % summ == 0:
            parol.append([nambers[i],nambers[j]])
#print(parol)
x = sum(parol,[])
#print(x)
result = ''. join(map(str, x))
print(result)




    




















