s = 'English = 78 Science = 83 Math = 68 History = 65'
l = len(s)
sum = 0
el = 0

for i in range(l):
    if el == 0:
        if s[i].isdigit() == 1:
            el = int(s[i])
    else:
        if s[i].isdigit() == 1:
            el = el*10 + int(s[i])
            if i == l-1:
                sum += el
                el = 0
        else:
            sum += el
            el = 0
print('Sum:', sum)
