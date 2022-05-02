



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


def interleavedTrap4(l):#TODO:make interleavedtrapN
    #print(len(l)//4)
    it = 0 
    sections = []
    for i in range(len(l)//4):
        sec = []
        for j in range(0,len(l),len(l)//4):
            sec.append(l[j + it])
        #print(sec)
        it += 1
        sections.append(sec)
    #print(sections)
    total = 0
    for i in sections:
        #print(i,end="")
        if sum(i) == 0:
            total += 3
            #print(i)
            #print(3)
        if sum(i) == 1:
            total += 2
            #print(i)
            #print(2)
        if sum(i) == 2:
            total += 1
            #print(i)
            #print(1)
        if sum(i) == 3:
            total += 0
            #print(i)
            #print(0)
        if sum(i) == 4:
            total += 4
            #print(i)
            #print(4)
    return total

if __name__ == "__main__":
    l0 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    l1 = [0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0]
    l2 = [0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1]
    l3 = [0,0,0,0]

    tlist = [1,1,1,0,1,1,0,0,0,0,1,0,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1,0,0,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,1,1,0,1,0,0,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,0]

    print(interleavedTrap4(l0))
    print(interleavedTrap4(l2))
    print(interleavedTrap4(tlist))


FITNESS_LIST = [oneMax,trapFour,interleavedTrap4]