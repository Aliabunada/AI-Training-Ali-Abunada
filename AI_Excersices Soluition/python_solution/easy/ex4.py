olist = []

def checkIsOrdered(listOrder, number):
    if len(listOrder) == 0:
        return True
    elif listOrder[-1] <= number:
        return True
    else:
        return False


def checkexistNumber(numbers, number):
    print(f"The list is {numbers}")

    for x in numbers:
        if x == number:
            return True

    return False


while True:
    inputmsg = input("Enter a number (Enter to finish): ")

    if inputmsg == '':
        break

    num = int(inputmsg)

    if checkIsOrdered(olist, num):
        olist.append(num)
    else:
        print("The number must be greater than or equal to the last number.")


while True:
    number = input("Please enter the number to search: ")

    if number == '':
        break

    num = int(number)
    result = checkexistNumber(olist, num)

    print(result)
    break