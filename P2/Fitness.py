



def oneMax(l):
    return sum(l)


def to_4n(l,n = 4):
    return [l[i:i+n] for i in range(0, len(l), n)]

def trapFour(l):
    total = 0
    splitlist = [l[i:i+4] for i in range(0, len(l), 4)]
    for i in splitlist:
        #print(i,end="")
        if sum(i) == 0:
            total += 3
            #print(3)
        if sum(i) == 1:
            total += 2
            #print(2)
        if sum(i) == 2:
            total += 1
            #print(1)
        if sum(i) == 3:
            total += 0
            #print(0)
        if sum(i) == 4:
            total += 4
            #print(4)
    return total


FITNESS_LIST = [oneMax,trapFour]