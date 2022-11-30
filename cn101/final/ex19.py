def isSorted(l):
    if len(l) == 1 or len(l) == 0:
        return True
    elif len(l) >= 2 and l == sorted(l):
        for n in l:
            if l.count(n) > 1:
                return False
    else:
        return False
    return True
print(isSorted([4,6,6]))