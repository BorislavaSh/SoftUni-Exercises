def raw_input(count):
    data = []
    for _ in range(count):
        lines = input()
        data.append(lines)
    return data


def get_intersections(text_list):
    inter_set = []
    for el in text_list:
        f_range, s_range = el.split("-")
        f_start, f_end = f_range.split(",")
        f_start, f_end = int(f_start), int(f_end)
        first_set = set()
        for num in range(f_start, f_end + 1):
            first_set.add(num)
        s_start, s_end = s_range.split(",")
        s_start, s_end = int(s_start), int(s_end)
        second_set = set()
        for s_num in range(s_start, s_end + 1):
            second_set.add(s_num)
        intersection = first_set.intersection(second_set)
        inter_set.append(intersection)
    return inter_set


def longest_intersection(ll):
    long_set = set()
    for a_set in ll:
        if len(a_set) > len(long_set):
            long_set = a_set.copy()
    return long_set


count = int(input())
text = raw_input(count)
intersections = get_intersections(text)
longest_inter = list(longest_intersection(intersections))
print(f"Longest intersection is {longest_inter} with length {len(longest_inter)}")