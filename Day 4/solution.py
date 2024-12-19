# arrange all the input into a 2d array
# each line is an array of 10 elements

rawinput = "MMMSXXMASMMSAMXMSMSAAMXSXMAAMMMSAMASMSMXXMASAMXAMMXXAMMXXAMASMSMSASXSSSAXAMASAAAMAMMMXMMMMMXMXAXMASX"

tester = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


arr = [rawinput[i : i + 10] for i in range(0, len(rawinput), 10)]

# In each list

# checkHorizontal for X followed by M


def checkNext(target, index, array):
    if index < len(array):
        if array[index] == target:
            return True
    return False


def checkNextDown(target, index, array):
    if index < len(array):
        if array[index] == target:
            return True
    return False


def checkPrev(target, index, array):
    if index > 0:
        if array[index] == target:
            return True
    return False


def checkHorizontal(line):
    for index, char in enumerate(line):
        if char == "X":
            if checkNext("M", index + 1, line):
                if checkNext("A", index + 2, line):
                    if checkNext("S", index + 3, line):
                        return True
    return False


def checkDiag(target, masterIndex, index, arr):
    if masterIndex < len(arr):
        if index < len(arr[masterIndex]):
            if arr[masterIndex][index] == target:
                return True
    return False


def checkDiagRev(target, masterIndex, index, arr):
    if masterIndex < len(arr):
        if index > 0:
            if arr[masterIndex][index] == target:
                return True
    return False


def checkReverse(line):
    for index, char in enumerate(line):
        if char == "S":
            if checkPrev("A", index - 1, line):
                if checkPrev("M", index - 2, line):
                    if checkPrev("X", index - 3, line):
                        return True
    return False


def checkDiagonal(masterIndex, arr, index):
    # check the next array at position + 1
    if checkDiag("M", masterIndex + 1, index + 1, arr):
        if checkDiag("A", masterIndex + 2, index + 2, arr):
            if checkDiag("S", masterIndex + 3, index + 3, arr):
                return True

    return False


def checkVertical(arr):
    for index, char in enumerate(arr):
        if char == "X":
            if checkNextDown("M", index + 1, arr):
                if checkNextDown("A", index + 2, arr):
                    if checkNextDown("S", index + 3, arr):
                        return True
    return False


def checkDiagonalReverse(masterIndex, arr, index):
    # check the next array at position + 1
    if checkDiagRev("M", masterIndex + 1, index - 1, arr):
        if checkDiagRev("A", masterIndex + 2, index - 2, arr):
            if checkDiagRev("S", masterIndex + 3, index - 3, arr):
                return True

    return False


COUNT = 0


def searchX(arr):
    sub_count = 0
    # check reverse and horizontal occurences
    for line in arr:
        if checkHorizontal(line):
            sub_count += 1

        if checkReverse(line):
            sub_count += 1

    return sub_count


# Check diagonal occurences
def searchZ(arr):
    sub_count = 0
    for masterIndex, line in enumerate(arr):
        for index, char in enumerate(line):
            if char == "X":
                if checkDiagonal(masterIndex, arr, index):
                    sub_count += 1
                if checkDiagonalReverse(masterIndex, arr, index):
                    sub_count += 1

                # checkDiagonalReverse(masterIndex, arr, index)
    return sub_count


COUNT += searchX(arr)
COUNT += searchZ(arr)

print(COUNT)
