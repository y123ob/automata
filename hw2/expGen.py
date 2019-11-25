import random
from math import *

max_length = 100

def expGen(depth):
    #recursion_count = recursion_count + 1
    seed = random.randrange(0, 5)
    
    if(depth == 0):
        return termGen(depth)
    depth = depth - 1
    if(seed < 2):
        return expGen(floor(depth*2/3)) + "+" + termGen(floor(depth/3))
    elif(seed < 4):
        return expGen(floor(depth*2/3)) + "-" + termGen(floor(depth/3))
    else:
        return termGen(depth)

def termGen(depth):
    #recursion_count = recursion_count +1
    seed = random.randrange(0, 5)
    
    if(depth == 0):
        return formGen(depth)
    depth = depth - 1
    if(seed < 2):
        return termGen(floor(depth*2/3)) + "*" + formGen(floor(depth/3))
    elif(seed < 4):
        return termGen(floor(depth*2/3)) + "/" + formGen(floor(depth/3))
    else:
        return formGen(depth)

def formGen(depth):
    #recursion_count = recursion_count + 1
    seed = random.randrange(0, 5)
    
    if(depth == 0):
        return id()
    if(seed == 0):
        return "(" + expGen(depth-1) + ")"
    else:
        return id()

def id():
    seed = random.randrange(15)
    if(seed < 4):
        return chr(ord('a')+seed)
    elif(seed < 7):
        return chr(ord('x')+seed-4)
    else:
        return chr(ord('0')+seed-5)


def totalGen(depth):
    return expGen(depth)

if __name__ == "__main__":
    for i in range(40):
        fout = open("./testcase/ex{}.in".format(i), "w")
        fout.write(totalGen(max_length))
        fout = open("./testcase/ex{}.ans".format(i), "w")
        fout.write("Yes\n")
    for i in range(10):
        fout = open("./testcase/wex{}.ans".format(i), "w")
        fout.write("No")