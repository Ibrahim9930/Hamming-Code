import math


def findRBits(s):
    length = len(s)
    for i in range(length):
        if (2**i) >= (length+i):
            return i
    return -1

def find_parityB_pos(r):
    a=[]
    for i in range(r):
        a.append(2**(i))
    return a

def encode_data(r,s):
    # s=s[::-1]
    a = find_parityB_pos(r)
    j = 0
    sentData =[]
    for i in range(r+len(s)):
        if i+1 in a:
            sentData.append('p')
        else:
            sentData.append(s[j])
            j=j+1
    return sentData

def find_parities(r,sentData):
    # find the parities' positions
    positions = find_parityB_pos(r)
    # find the parities' values
    for i in positions:
        # print(" i = {}".format(i))
        # initialize the parity value
        sentData[i-1]='0'
        # Go through the data to see which are xored to the parity value
        for j in range(len(sentData)):
            # print(" j = {}".format(j))
            # The position is to be xored
            if ((j+1) & i) == i:
                t = int(sentData[i-1],2) ^ int(sentData[j],2)
                sentData[i-1]=str(t)
    data = sentData
    return data

s='01001101'
r = findRBits(s)
sd=encode_data(r,s)
data=find_parities(r,sd)
print("".join(data))



