grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={'Johnny','Bilbo','Steve','Khendrik','Aaron'}
students=list(students)
print(students)
students.sort()
print(students)
grades=[sum(grades[i])/len(grades[i]) for i in range(len(grades))]
print(grades)
# первый метод
sredni_bal=dict(zip(students,grades))
print(sredni_bal)
# второй метод
sredni_bal={}
for i in range(len(students)):
    sredni_bal[students[i]]=grades[i]
print(sredni_bal)