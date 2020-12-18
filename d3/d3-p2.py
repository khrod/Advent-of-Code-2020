import numpy as np

text_file = open('d3-input', 'r')

lines = text_file.read().split('\n')

ll = len(lines[0])

# Right 1, down 1.
# Right 3, down 1.
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
lc = []
for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    i = 0
    c = 0
    for line in lines[::d]:
        # print(line)
        # print(ll)
        # print(i)
        if i > (ll - 1):
            i -= ll
        # print(i)
        # print('--')
        if line[i] == '#':
            c += 1

        i += r

    print(c)
    lc.append(c)

print(lc)

print(np.prod(lc))