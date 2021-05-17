n = input().split(" ")
first_set_n = int(n[0])
second_set_n = int(n[1])
first_set = set()
second_set = set()

for i in range(first_set_n):
    number_1 = int(input())
    first_set.add(number_1)

for i in range(second_set_n):
    number_2 = int(input())
    second_set.add(number_2)

result = first_set.intersection(second_set)

for number in result:
    print(number)