

with open("sampledata.txt") as f:     

    lst = [x.strip() for x in f.readlines() if x.startswith('L') or x.startswith('M') or x.startswith('S')]
    lst.sort()
    for x in lst:
        print(x)       
    f.close()    