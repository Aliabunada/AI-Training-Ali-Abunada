def countWords(text):
    words = text.lower().split()
    result = {}

    for word in words:
        if word.endswith(".") and word != words[-1]:
            word = word[:-1]

        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result
while True:
    inputText = input("enter the text here : ")
    if inputText == '':
        break
    try:
      print(f'{countWords(inputText)}')
    except ValueError:
            print("Invalid input. Please enter a valid integer.")

