def ord_encode(string):
    cipher = ""
    for char in string:
        ascii = str(ord(char))
        cipher += ascii
    print("Cipher Text: ", cipher)
    padding(cipher)
    

def key_gen(new_cipher):
    sum = 0
    for i in range(len(new_cipher)):
        sum += int(new_cipher[i])
    global key
    key = 0
    for char in str(sum):
        key += int(char)
    return
def key_gen2(new_cipher):
    length = int(len(new_cipher))
    global key2 
    if length%2==0:
        key2 = new_cipher[int(length/2)]
    else:
        key2 = new_cipher[(length+1)/2]
    return key2
def key_gen3(new_cipher):
    length = len(new_cipher)
    global key3
    key3 = new_cipher[0]+new_cipher[length - 1]
    return

def padding(cipher):
    length = len(cipher)
    if length < 64:
        t = 1
        for i in range(length, 64):
            if t<10:
                cipher += str(t)
                t = t + 1
            if t>=10:
                t=1
    if length > 64:
        l =1
        for i in range(32):
            if len(cipher)%32!=0:
                if l >= 10:
                    l = 1
                cipher += str(l)
                l = l+1
            if len(cipher)%32==0:
                break

    cipher_array = []
    for char in cipher:
        cipher_array.append(char)
    split = []
    div = len(cipher)//32
    n = 0
    for m in range(div):
        t = ""
        for i in range(n, 32 + n):
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
    key_gen(cipher_array)
    key_gen2(cipher_array)  
    key_gen3(cipher_array)  
    hash(key, key2, key3, cipher_array)

def format(hash):
    l = 1
    for i in range(38):
        if len(hash)%38!=0:
            if l >= 10:
                l = 1
            hash += str(l)
            l = l+1
        if len(hash)%38==0:
                    break
    split = []
    a = ""
    for i in range(len(hash)):
        if (i+1)%38==0:
            a = a + hash[i]
            split.append(a)
            a = ""
        else:
            a = a + hash[i]

    t = ""
    for i in range(38):
        sum = 0
        for m in range(len(split)):
            k = split[m][i]
            sum = int(sum) + int(k)
        no = sum%10
        t = t + str(no)
    print(t)


def hash(key, key2, key3, cipher_array):
    form = ""
    hash = ""
    for i in range(len(cipher_array)):
        temp = (int(cipher_array[i])+int(key))%11
        form += str(temp)
        temp = 0
    for i in range(len(form)):
        var = (int(form[i])+(int(key3)*int(key2)))%11
        hash += str(var)
    format(hash)


def main():
    string = input("Enter a string to hash: ")
    encode(string)

if __name__ == "__main__":
    main()

