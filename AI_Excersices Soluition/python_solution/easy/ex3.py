newList = [] 

while True:
    inputmsg = input("enter the list till press enter : ")
    if inputmsg == '' :
            break
    try:
        num = int(inputmsg)
        newList.append(num)
    except ValueError:
            print("Invalid input. Please enter a valid integer.")


def finalList(check):
    permanent = []
    if len(check) <= 2:
        permanent = check
        return permanent
    else:
        permanent = [check[0], check[-1]]
        return permanent

print(f"the original list {newList}")
print(f"the final editted list {finalList(newList)}")