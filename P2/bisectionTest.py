import matplotlib.pyplot as plt
goal = 1842

lowerBound = 1
upperBound = 100
num = upperBound
l = []
u = []
n = []


over = False

#if upper and lower bound ar within 10% you can pick the uper bound

while True:
    if float(upperBound/lowerBound) <= 1.05:
        print("Close to goal",num,goal,str(upperBound/lowerBound))
        print("GOAL FOUD")
        plt.plot(l)
        plt.plot(u)
        plt.plot(n)
        plt.show()
        break;
    elif num < goal:
        print("goal not found UNDER",num,goal,str(upperBound/lowerBound))
        lowerBound = upperBound
        upperBound *= 2
        num = upperBound
        l.append(lowerBound)
        u.append(upperBound)
        n.append(num)
    elif num > goal:
        print("goal not found OVER",num,goal,str(upperBound/lowerBound))
        #lowerbound = same
        over = True
        upperBound = int((upperBound + lowerBound)/2)
        num = upperBound        
        l.append(lowerBound)
        u.append(upperBound)
        n.append(num)

    #else:
    #    print("GOAL FOUD")
    #    plt.plot(l)
    #    plt.plot(u)
    #    plt.plot(n)
    #    plt.show()
    #    break;

#import matplotlib.pyplot as plt
#plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
#plt.show()