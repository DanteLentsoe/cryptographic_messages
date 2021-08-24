def Encrpty(sentence):

    result = []

    # Encrypting Message
    for letter in sentence:
        crpted_letters = ord(letter)
        result.append(crpted_letters)

    print("Encrypted Message ")

    for value in result:
        print(value, end="")
        print(" ", end="")

    # Decrypting Message Function
    Decrpt(result)


def Decrpt(result):

    numbers_to_letter = []
    result_decrypted = []
    # Decrypting Message
    for letter in result:
        words = int(letter)
        numbers_to_letter.append(words)

    print("'\n'")
    print("Decrypted Message ")

    for value in numbers_to_letter:
        word_convert = chr(value)
        print(word_convert, end=" ")
        print(" ", end="")
        #resolvedWords = chr(result)


def Main():
    userWords = input("Enter sentence to be encrpted ")
    Encrpty(userWords)

    # Resolve encryption
    Decrpt(userWords)


if __name__ == "__main__":

    Main()
