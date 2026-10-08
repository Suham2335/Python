list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 50, 70, 80, 90]

common = []
only_list1 = []
only_list2 = []

for number in list1:
    if number in list2:
        common.append(number)
    else:
        only_list1.append(number)

for number in list2:
    if number not in list1:
        only_list2.append(number)

print("Common elements:", common)
print("Only in list1:", only_list1)
print("Only in list2:", only_list2)