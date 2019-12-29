import random

def findRBits(s):
    # Finds the number of parity bits needed
    length = len(s)
    for i in range(length):
        if ((2**i)-1) >= (length+i):
            return i
    return -1

def find_parityB_pos(r):

    a=[]
    # Go through the parities and find their position
    for i in range(r):
        a.append(2**(i))
    return a

def encode_data(s,r,positions):

    j = 0
    sentData =[]
    for i in range(r+len(s)):
        if i+1 in positions:
            # Fill the parity posotions with p
            sentData.append('p')
        else:
            sentData.append(s[j])
            j = j+1
    return sentData

def find_parities(r,sentData,positions):

    # find the parities' values
    for i in positions:
        # initialize the parity value
        sentData[i-1]='0'
        # Go through the data to see which are xored to the parity value
        for j in range(len(sentData)):
            # The position is to be xored
            if ((j+1) & i) == i:
                t = int(sentData[i-1] , 2) ^ int(sentData[j],2)
                sentData[i-1]=str(t)
    data = sentData
    return data

def check_and_correct(receivedData,r,positions):
    # ----Error detection----

    # Flag to see if an error was detected
    errorDetected = False
    # The position of the error bit
    errorBitIndex = 0
    # Go through all the parity (check) bits
    for pos in positions:
        t = 0
        for i in range(len(receivedData)):
            if ((i+1) & pos) == pos:
                t = t ^ int(receivedData[i],2)
        if t == 1:
            errorDetected = True
            errorBitIndex = errorBitIndex + pos

    # ----Error correction----

    if errorDetected:
        print("Error detected")
        temp = int(receivedData[errorBitIndex-1]) ^ 1
        receivedData[errorBitIndex-1] = str(temp)

def checkIfBinary(s):
    for i in s:
        if i == '0' or i == '1':
            pass
        else:
            return False
    return True

def get_input():

    wrongInput = True
    print("Please enter the data stream you wish to transmit")
    stream = input()
    if stream.isdigit() and checkIfBinary(stream):
        return stream
    while True:
        print("Please enter a valid binary stream consisting of 0s and 1s")
        stream = input()
        if stream.isdigit() and checkIfBinary(stream):
            return stream

if __name__ == '__main__':

    # ___ Transmit___
    stream = get_input()
    rb = findRBits(stream)
    m = len(stream)
    positions = find_parityB_pos(rb)
    data = stream[::-1]
    sentData = encode_data(data,rb,positions)
    find_parities(rb,sentData,positions)
    sentDataS = "".join(sentData)
    sentDataS = sentDataS[::-1]
    print("Data transmitted is {}".format(sentDataS))
    print("The number of parity bits is {}".format(rb))
    print("Single error correction percentage is {}%".format((rb / m) * 100))
    print("Double error correction percentage is {}%".format(((rb + 1) / m) * 100))

    # ___Receive___
    errorBit = random.randint(0,len(sentData)-1)
    print("Sent the data with error in bit {}".format(errorBit))
    receivedData = sentData
    errorBitValue = int(receivedData[errorBit])^1
    receivedData[errorBit] = str (errorBitValue)
    rDataS = "".join(receivedData)
    rDataS = rDataS[::-1]
    print("Received data is {}".format(rDataS))
    check_and_correct(receivedData,rb,positions)
    rDataS = "".join(receivedData)
    rDataS = rDataS[::-1]
    print("Corrected data is {}".format(rDataS))

