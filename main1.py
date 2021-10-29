slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8


def options(slotsA, slotsB, dur):
    for i in slotsA:
        for j in slotsB:
            ls1 = []
            ls2 = []
            ls4 = []
            ls3 = []
            s = 0
            a = range(i[0], i[1]+1)
            b = range(j[0], j[1]+1)
            for f in a:
                ls1.append(f)
            for d in b:
                ls2.append(d)
            for el in ls1:
                for el1 in ls2:
                    if el == el1:
                        ls3.append(el)
                        s += 1
                if s > dur:
                    ls4.append(min(ls3))
                    ls4.append(max(ls3))
                    return ls4


print(options(slotsA, slotsB, dur))
