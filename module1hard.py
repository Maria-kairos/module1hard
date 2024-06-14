grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Khendrik', 'Aaron'}
students = sorted(students)
print('Список студентов в алфавитном порядке: ', students)
arefm = []
for a in range(4):
    b = sum(grades[a])/len(grades[a])
    arefm.append(b)
kniga = dict(zip(students, arefm))
print('Список средних баллов учеников в реестре: ', kniga)