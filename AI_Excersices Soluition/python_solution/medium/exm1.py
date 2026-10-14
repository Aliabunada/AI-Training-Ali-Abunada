print("Welcome to my program!")

biglist = []

def checkZeroFunction(lst):
    resultList = []

    for i in range(len(lst)):
        n1 = lst[i]

        for j in range(i + 1, len(lst)):
            n2 = lst[j]

            for k in range(j + 1, len(lst)):
                n3 = lst[k]

                result = n1 + n2 + n3

                if result == 0:
                    triplet = sorted([n1, n2, n3])

                    if triplet not in resultList:
                        resultList.append(triplet)

    return resultList


while True:
    inp = input("Enter a number (Enter to finish): ")

    if inp == "":
        break

    try:
        num = int(inp)
        biglist.append(num)

    except ValueError:
        print("Invalid input. Please enter an integer.")


result = checkZeroFunction(biglist)

if len(result) == 0:
    print("No triplets found.")
else:
    print(f"The result is {result}")