#merge Dict

d1 = {'a':10, 'b':20}
d2 = {'b':5, 'c':15}

#way-1
for key in d2:
    if key in d1:
        d1[key] = d1[key] + d2[key]
    else:
        d1[key] = d2[key]

print(d1)

#============================================================

#way-2
for key in d2:
    d1[key] = d1.get(key, 0) + d2[key]