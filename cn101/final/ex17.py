def myStats():
    data = [(8, 2, 6, 4), (5, 6, 7, 8)]
    list_result = []
    for tup in data:
        Range = max(tup) - min(tup)
        Mean = sum(tup) / len(tup)
        list_result.append((Range,Mean))
    print(list_result)
    
myStats()