
# 1. Read the data from the file
arr = []
with open("Day 1/data.txt") as file:
    data = file.readlines()
    for line in data:
        lineNums = [int(num) for num in line.split()]
        arr.extend(lineNums)    

# 2. Create two lists, interpolating between the values provided.
exampleArr = [3,4,4,3,2,5,1,3,3,9,3,3]
list1 = []
list2 = []

for (index, element) in enumerate(arr):
    if(index%2):
        list1.append(element)
    else:
        list2.append(element)


def solution1():    
    # 3. Sort both lists
    list1.sort()
    list2.sort()

    # 4. for each element in both lists, subtract them from each other at the same index position, adding the difference to a sum
    sum = 0
    for (index, element) in enumerate(list1):
        sum += abs(list1[index] - list2[index])

    print(sum)

def solution2():
    sum = 0

    for element in list1:
    # Check how many times a number appears in the other list.
        count = list2.count(element)
        # Multiply the number by the number of times it appears in the other list.
        # Add the result to a sum.
        sum += element * count

    print(sum)

solution2()