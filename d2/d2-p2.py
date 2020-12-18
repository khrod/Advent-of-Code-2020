text_file = open('d2-input', 'r')

lines = text_file.read().split('\n')

print(lines[0].split(' '))

c = 0

for line in lines:
    pp = line.split(' ')
    pos = pp[0]
    l = pp[1][0]
    p = pp[2]

    lc = p.count(l)
    fp = int(pos.split('-')[0])
    sp = int(pos.split('-')[1])
    # print(p, fp, sp)

    if (p[fp-1] == l) ^ (p[sp-1] == l):
        c += 1

print(c)