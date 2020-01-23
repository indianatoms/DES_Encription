import random

plainText = "supersec"
key = "secret_k"

#change human readible key to bianary key
def changeToBinary(x):
    keybin = ""
    #check the lenght
    if len(x) < 8:
        print("Choose another Key")
        return 0
    if len(x) > 8:
        x = x[0:7]
        print("You Key has been cut to eight characters: " + x)
    for char in x:
        #print(char)
        # ord prints the ascii value
        #print(ord(char))
        #print(bin(ord(char)))
        #print(len(bin(ord(char))))
        #to ascii to binary
        x = bin(ord(char))
        #print(x)
        if(len(x) < 9):
            #print("too short")
            x = x.replace('b', '0')
        else:
            x = x.replace('b', '')
        #print(x)
        keybin = keybin + x
    # print(keybin.replace('b',''))
    return keybin

#permautate the given key to certain long with the list provided
def permutation64toN(key64,howLong,my_list):
    key56 = ""
    #my_list = list(range(0, len(key64)))  # list of integers from 1 to key64.len

    # adjust this boundaries to fit your needs
    #random.shuffle(my_list)
  #  print(len(my_list))
    for i in range(0, howLong):
        key56 = key56 + key64[my_list[i]-1]
    #print(key56)
    return key56

#shift one left
def shiftleft(halfKey):
    shifted = ''.join(halfKey[1:] + halfKey[0])
    return shifted

# print(changeToBinary(key))
key64 = changeToBinary(key)
key64="0001001100110100010101110111100110011011101111001101111111110001"
print("prient 64 bit key")
print(key64)
#print(key56)

#initial key permutation
my_list1 = [
                  57, 49, 41, 33, 25, 17,  9,
                   1, 58, 50, 42, 34, 26, 18,
                  10,  2, 59, 51, 43, 35, 27,
                  19, 11,  3, 60, 52, 44, 36,
                  63, 55, 47, 39, 31, 23, 15,
                   7, 62, 54, 46, 38, 30, 22,
                  14,  6, 61, 53, 45, 37, 29,
                  21, 13,  5, 28, 20, 12,  4
            ]
key56 = permutation64toN(key64,56,my_list1)
#print("Print 56 bit KEY")
#print(key56)


#print(key64)
#print(len(key64))

#get first and second half
firstHalfKey56 = key56[0:28]
secondHalfKey56 = key56[28:56]
#print(firstHalfKey56)
#print(secondHalfKey56)

#sub-key permutation
my_list3 = [14, 17, 11, 24,  1,  5,  3, 28,
            15,  6, 21, 10, 23, 19, 12,  4,
            26,  8, 16,  7, 27, 20, 13,  2,
            41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56,
            34, 53, 46, 42, 50, 36, 29, 32]

#perform the shifting and permutation according to the parameters
def get16Subkeys(firsthalf,secondhalf,my_list3):
    my_list = list(range(0, 48))
    listOfKeys = list()
    key48 = ""
    for i in range(0,16):
       # print(i)
        key48 = ""
        if i == 0 or i == 1 or i == 8 or i == 15 :
            firsthalf = shiftleft(firsthalf)
            secondhalf = shiftleft(secondhalf)
        else:
            firsthalf = shiftleft(shiftleft(firsthalf))
            secondhalf = shiftleft(shiftleft(secondhalf))
        key56 = firsthalf + secondhalf
        key48 = permutation64toN(key56,48,my_list3)
        listOfKeys.append(key48)
    return listOfKeys

#16 SUB-KEYS
listOfKeys = get16Subkeys(firstHalfKey56,secondHalfKey56,my_list3)
#print("16-SubKeys")
for x in listOfKeys:
    print(x)

# SBOXES
S_BOX = [

    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]

#plain TEXT to bianary
plainText = changeToBinary(plainText)
plainText = "0000000100100011010001010110011110001001101010111100110111101111"
#PC-1
#initial message permutation
my_list2 = [58, 50, 42, 34, 26, 18, 10, 2,
           60, 52, 44, 36, 28, 20, 12, 4,
           62, 54, 46, 38, 30, 22, 14, 6,
           64, 56, 48, 40, 32, 24, 16, 8,
           57, 49, 41, 33, 25, 17, 9, 1,
           59, 51, 43, 35, 27, 19, 11, 3,
           61, 53, 45, 37, 29, 21, 13, 5,
           63, 55, 47, 39, 31, 23, 15, 7]

print("Plain Text = " + plainText)

permuteatedPlainText = permutation64toN(plainText,64,my_list2)
print("Permutated PlainText")
print(permuteatedPlainText)

L0 = permuteatedPlainText[0:32]
print(L0)
R0 = permuteatedPlainText[32:64]
print(R0)

my_list4 = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]


def xor(a, b):
    y = int(a, 2) ^ int(b, 2)
    y = '{0:0{1}b}'.format(y, len(a))
    return y

#perform the F-FUNCTION
for loop in range(0,16):


    ER0=permutation64toN(R0,48,my_list4)
    print("E(R0)")
    print(ER0)

    #print(listOfKeys[1])

    KxorER = xor(ER0,listOfKeys[loop])
    print(KxorER)

    #so far so GOOD =========================

    #get values form SBOXES
    S_BOX_VALUES = list()

#GET VALUES FROM SBOXES
    def getValuesFromSBoxes(KxorER):
        x=0
        product = ""
        for i in range(0,8):
            print("====THE=NEW=SIX===")
            print(KxorER[x:x+6])
            print(KxorER[x]+KxorER[x+5])
            print(KxorER[x+1:x+5])

            SBOX_ROW = int(KxorER[x]+KxorER[x+5],2)
            SBOX_COLUMN = int(KxorER[x+1:x+5],2)
            print("Row: " + str(SBOX_ROW))
            print("Column: " + str(SBOX_COLUMN))
            S1 = S_BOX[i][SBOX_ROW][SBOX_COLUMN]
            S_BOX_VALUES.append(S1)
            x = x + 6
            print("S" + str(i) + " value: " + str(S1))
            y = '{0:0{1}b}'.format(S1,4)
            print(y)
            product = product + y
        return product

    SBoxes = getValuesFromSBoxes(KxorER)

    #print(len(SBoxes))
    print(loop)
    print("Outut form xboxes")
    print(SBoxes)

    P_BOX =  [ 16,  7, 20, 21,
                  29, 12, 28, 17,
                   1, 15, 23, 26,
                   5, 18, 31, 10,
                   2,  8, 24, 14,
                  32, 27,  3,  9,
                  19, 13, 30,  6,
                  22, 11,  4, 25 ]

    PBoxes = permutation64toN(SBoxes,32,P_BOX)
    print("AFTER P_BOX")
    print(PBoxes)
    #print(R0)
    NewL0 = R0
    NewR0 = xor(L0,PBoxes)
    L0 = NewL0
    R0 = NewR0
    print("After: " + str(loop))
    print(L0)
    print(R0)

Cipher = R0+L0
print(Cipher)

IPminus1 = [40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41,  9, 49, 17, 57, 25]

#apply last permutation
Cipher = permutation64toN(Cipher,64,IPminus1)
print("Final Cipher")
print(Cipher)
print(hex(int(Cipher,2)))
