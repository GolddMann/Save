if __name__ == "__main__":
    data = "Hello world!"
    rot = 150
    ciphered = ""
    for letter in data:
        ciphered += chr((ord(letter) + rot) % 256)

    print(data)  # Hello world
    print(ciphered)  # Jgnnq"yqtnf#

    unciphered = ""
    for letter in ciphered:
        a = ord(letter) - rot
        if(a < 0):
            a += 256
        unciphered += chr(a)

    print(unciphered)  # Hello world
