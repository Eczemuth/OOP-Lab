import math
import re
import time
def item1():
    [print(i,end = ",") for i in range(2000,3201) if i % 7 == 0 and i % 5 != 0]
    print("\b")
    # for i in range(2000,3201):
    #     if (i % 7 == 0 and i % 5 != 0):
    #         print(i,end = ",")
    # else:
    #     print("\b")

def item2():
    s = input(">> ")
    print("Lowercase :",len(re.findall("[a-z]",s)))
    print("Uppercase :",len(re.findall("[A-Z]",s)))

def item3():
    cost = 0
    hIn,minIn,hOut,minOut = [int(x) for x in input().split()]
    parkMin = (hOut * 60 + minOut) - (hIn * 60 + minIn)
    if parkMin > 360:
        cost = 200
    elif parkMin > 180:
        cost = math.ceil((parkMin - 180)/60) * 20 + 30
    elif parkMin > 15:
        cost = math.ceil(parkMin/60) * 10

    print(cost)

def item4():
    n = input()
    print(int(n) + int(n * 2) + int(n * 3) + int(n * 4))

def item5():
    for num1 in range(999,99,-1):
        for num2 in range(999,99,-1):
            s = num1 * num2
            if str(s) == str(s)[::-1]:
                print(num1,num2,s)
                return

def item6()
    n = int(input())
    print("".join([" " * (n - i - 1) + "*" * (i + 1) + "\n" for i in range(n)]))

item6()