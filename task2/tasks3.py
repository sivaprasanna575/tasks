u = [1, 2, 3, 3, 5, 5, 9, 2, 2]
a = []
for num in u:
    if len(a) != 0:
        if a[-1] != num:
            a.append(num)
    else:
        a.append(num)
print (a)
