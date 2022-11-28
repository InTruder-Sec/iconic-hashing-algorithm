"""
||=========================================||
||                                         ||
||         Iconic Hashing Algorithm        ||
||  Author: Deep Dhakate (InTruder)        ||
||  Version: 1.0.1                         ||
||=========================================||
"""


def encode(string):  # Converts each characters to its ascii characters
    cipher = ""
    for char in string:
        ascii = str(ord(char))
        cipher += ascii
    print("Cipher Text: ", cipher)
    finalhash = padding(cipher)
    return finalhash


def key_gen(new_cipher):  # Generate keys for encrypting
    sum = 0
    for i in range(len(new_cipher)):
        sum += int(new_cipher[i])
    key = 0
    for char in str(sum):
        key += int(char)
    return key


def key_gen2(new_cipher):
    length = int(len(new_cipher))
    if length % 2 == 0:
        key2 = new_cipher[int(length/2)]
    else:
        key2 = new_cipher[(length+1)/2]
    return key2


def key_gen3(new_cipher):
    length = len(new_cipher)
    key3 = new_cipher[0]+new_cipher[length - 1]
    return key3


# PADDING
def padding(cipher):  # Changes cipher text into padded text
    length = len(cipher)
    if length < 64:
        t = 1
        for i in range(length, 64):  # Addes base 10 no if length of cipher text is less than 64
            if t < 10:
                cipher += str(t)
                t = t + 1
            if t >= 10:
                t = 1
    if length > 64:
        l = 1
        for i in range(32):
            # If length is greater than 64 it addes base 10 no to nearest 32 divisible no
            if len(cipher) % 32 != 0:
                if l >= 10:
                    l = 1
                cipher += str(l)
                l = l+1
            if len(cipher) % 32 == 0:
                break

    cipher_array = []
    for char in cipher:
        cipher_array.append(char)
    split = []
    div = len(cipher)//32
    n = 0
    for m in range(div):
        t = ""
        for i in range(n, 32 + n):  # Divides cipher text into 32 parts and stores in array
            t = t + str(cipher_array[i])
        n += 32
        split.append(t)
    leng = len(split)
    temp = split[0]
    split[0] = split[leng - 1]
    split[leng - 1] = temp
    n_cipher = ""
    for i in range(len(split)):
        n_cipher += split[i]
    cipher_array = []
    for char in n_cipher:
        cipher_array.append(char)
    # Generate keys
    key = key_gen(cipher_array)
    key2 = key_gen2(cipher_array)
    key3 = key_gen3(cipher_array)
    finalhash = hash(key, key2, key3, cipher_array)
    return finalhash


def format(hash):  # Change the hash into length of 38
    l = 1
    for i in range(32):
        if len(hash) % 32 != 0:
            if l >= 10:
                l = 1
            hash += str(l)
            l = l+1
        if len(hash) % 32 == 0:
            break
    split = []
    a = ""
    for i in range(len(hash)):
        if (i+1) % 32 == 0:
            a = a + hash[i]
            split.append(a)
            a = ""
        else:
            a = a + hash[i]

    t = ""
    for i in range(32):
        sum = 0
        for m in range(len(split)):
            k = split[m][i]
            sum = int(sum) + int(k)

        if(i % 2 == 0):
            no = hex(sum).lstrip("0x").rstrip("L")
        else:
            no = sum % 10
        t = t + str(no)
    return t


def hash(key, key2, key3, cipher_array):  # Hashes the cipher text with keys
    form = ""
    hash = ""
    for i in range(len(cipher_array)):
        temp = (int(cipher_array[i])+int(key)) % 11
        form += str(temp)
        temp = 0

    for i in range(len(form)):
        if i % 2 == 0:
            var = (int(form[i])+(int(key3)*int(key2))) % 11
            # var = hex(var)
            hash += str(var)
        else:
            var = (int(form[i])+(int(key3)*int(key2))) % 11
            hash += str(var)
    finalhash = format(hash)

    finalhash = format(hash)
    return finalhash


def main():
    print("Iconic Hashing Algorithm")
    print("Version: 1.0.1")
    string = input("Enter a string to hash: ")
    finalhash = encode(string)
    print(finalhash)


if __name__ == "__main__":
    main()
