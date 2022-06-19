import re


def encypt(message):
    encrypted = ""
    for letter in message:
        big = False

        if(ord(letter) >= 65 and ord(letter) <= 90):
            big = True

        if(big):
            encrypted += chr(65 + (ord(letter) + 13 - 65) % 26)
        else:
            encrypted += chr(97 + (ord(letter) + 13 - 97) % 26)

    return encrypted


def decrypt(message):
    decrypted = ""

    for letter in message:
        big = False
        if(ord(letter) >= 65 and ord(letter) <= 90):
            big = True

        if(big):
            a = ord(letter) - 13
            if(a < 65):
                decrypted += chr(a + 90 - 64)
            else:
                decrypted += chr(a)
        else:
            a = ord(letter) - 13
            if(a < 97):
                decrypted += chr(a + 122 - 96)
            else:
                decrypted += chr(a)

    return decrypted


def check_alphabet(message):
    m = re.search('[^(a-z)?(A-Z)?]', message)
    return False if m else True


if __name__ == "__main__":
    input_data = input("Enter message: ")
    if(check_alphabet(input_data)):
        encypted = encypt(input_data)
        decrypted = decrypt(encypted)
        print(input_data)
        print(encypted)
        print(decrypted)
    else:
        print("Wrong alphabet!")
