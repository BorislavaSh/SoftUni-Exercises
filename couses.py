courses = {}

while True:
    data = input()
    if data == 'end':
        break
    course, student = data.split(' : ')
    if course not in courses:
        courses[course] = list()
        courses[course].append(student)
    else:
        courses[course].append(student)

for cName, sNames in sorted(courses.items(), key=lambda x: len(x[1]), reverse=True):
    registered_students = len(sNames)
    sNames.sort(key=lambda x: x[0])
    print(f'{cName}: {registered_students}')
    for student in sNames:
        print(f'-- {student}')