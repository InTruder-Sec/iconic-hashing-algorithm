def encode(string):
    upper_case = [["A", "01"], ["B", "02"], ["C", "03"], ["D", "04"], ["E", "05"], ["F", "06"], ["G", "07"], ["H", "08"], ["I", "09"], ["J", "11"], ["K", "22"], ["L", "33"], ["M", "44"], ["N", "55"], ["O", "66"], ["P", "77"], ["Q", "88"], ["R", "99"], ["S", "12"], ["T", "13"], ["U", "14"], ["V", "15"], ["W", "16"], ["X", "17"], ["Y", "18"], ["Z", "19"]]
    lower_case = [["a", "23"], ["b", "24"], ["c", "25"], ["d", "26"], ["e", "27"], ["f", "28"], ["g", "29"], ["h", "34"], ["i", "35"], ["j", "36"], ["k", "37"], ["l", "38"], ["m", "39"], ["n", "45"], ["o", "46"], ["p", "47"], ["q", "48"], ["r", "49"], ["s", "56"], ["t", "57"], ["u", "58"], ["v", "59"], ["w", "67"], ["x", "68"], ["y", "69"], ["z", "78"]]
    number = [["1", "601"], ["2", "602"], ["3", "603"], ["4", "604"], ["5", "605"], ["6", "606"], ["7", "607"], ["8", "608"], ["9", "609"], ["0", "610"], [" ", "00"]]
    symbols = [["~", "1000"], ["`", "1001"], ["!", "1002"], ["#", "1003"], ["$", "1004"], ["%", "1005"], ["^", "1006"], ["&", "1007"], ["*", "1008"], ["(", "1009"], [")", "1010"], ["-", "1011"], ["_", "1012"], ["=", "1013"], ["+", "1014"], ["{", "1015"], ["}", "1016"], ["[", "1017"], ["]", "1018"], [":", "1019"], [";", "1020"], ['"', "1021"], ["'", "1022"], ["|", "1023"], ["\\", "1024"], ["<", "1025"], ["@", "1026"]]

    global cipher
    cipher = ""
    for char in string:
        for i in range(len(upper_case)):
            if char == upper_case[i][0]:
                cipher += str(upper_case[i][1])
            if char == lower_case[i][0]:
                cipher += str(lower_case[i][1])
        for t in range(len(number)):
                if char == number[t][0]:
                    cipher += number[t][1]
        for o in range(len(symbols)):
                if char == symbols[o][0]:
                    cipher += symbols[o][1]
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

