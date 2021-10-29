slotsA = [[10,50], [60,120], [140, 210]]
slotsB = [[0,15], [60,70], [0, 1]]
dur = 8


def func(slotsA, slotsB, dur):
    for i in range(len(slotsA)):
       ls1 = []
       ls2 = []
       ls4 = []
       ls3 = []
       s = 0
       a = range((slotsA[i])[0], (slotsA[i])[1]+1)
       b = range((slotsB[i])[0], (slotsB[i])[1]+1)
       for f in a:
           ls1.append(f)
       for d in b:
           ls2.append(d)
       for el in ls1:
           for el1 in ls2:
               if el == el1:
                  ls3.append(el)
                  s+=1
           if s > dur:
             ls4.append(min(ls3))
             ls4.append(max(ls3))
             print(ls4)
             break



func(slotsA,slotsB,dur)