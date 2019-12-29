Data="0 1 0 0 1 0 0 1 0 1 0 1"
receivedData = Data.split()

print(receivedData)
def find_parityB_pos(r):
    a=[]
    for i in range(r):
        a.append(2**(i))
    return a

def check_and_correct():
    # Initialize data used
    r = 4
    a = find_parityB_pos(r)
    # ----Error detection----

    # Flag to see if an error was detected
    errorDetected = False
    # The position of the error bit
    errorBitIndex = 0
    # Go through all the parity (check) bits
    for pos in a:
        t = 0
        for i in range(len(receivedData)):
            if ((i+1) & pos) == pos:
                t = t ^ int(receivedData[i],2)
        if t == 1:
            print("position is {}".format(pos))
            errorDetected = True
            errorBitIndex = errorBitIndex + pos

    # ----Error correction----

    if errorDetected:
        print("Error detected")
        temp = int(receivedData[errorBitIndex-1]) ^ 1
        receivedData[errorBitIndex-1] = str(temp)

check_and_correct()
print(receivedData)

