def balikPosisi(a):
    list2 = []
    b = len(a)-1
    for i in range(0, len(a)):
        list2.append(a[b])
        b = b-1
    return list2


print(balikPosisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikPosisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikPosisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))


