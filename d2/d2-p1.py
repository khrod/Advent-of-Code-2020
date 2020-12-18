text_file = open('d2-input', 'r')

lines = text_file.read().split('\n')

print(lines[0].split(' '))

c = 0

for line in lines:
    pp = line.split(' ')
    r = pp[0]
    l = pp[1][0]
    p = pp[2]

    lc = p.count(l)
    lr = int(r.split('-')[0])
    ur = int(r.split('-')[1])
    # print(lc,lr,ur)

    if lr <= lc <= ur:
        c += 1

print(c)