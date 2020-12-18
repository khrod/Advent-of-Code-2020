text_file = open('d3-input', 'r')

lines = text_file.read().split('\n')

ll = len(lines[0])

i = 0
c = 0
for line in lines:
    # print(line)
    # print(ll)
    # print(i)
    if i > (ll - 1):
        i -= ll
    # print(i)
    # print('--')
    if line[i] == '#':
        c += 1

    i += 3

print(c)