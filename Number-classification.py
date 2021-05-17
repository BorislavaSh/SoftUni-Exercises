nums = input().split(", ")

nums = map(int, nums)
positive_nums = []
negative_nums = []
even_nums = []
odd_nums = []

for num in nums:
    if num >= 0:
        positive_nums.append(num)
    if num < 0:
        negative_nums.append(num)
    if num % 2 == 0:
        even_nums.append(num)
    if num % 2 == 1:
        odd_nums.append(num)

for _ in positive_nums:
    print(f'Positive: {positive_nums}')