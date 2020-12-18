text_file = open('d1-input', 'r')

lines = text_file.read().split('\n')

print(lines)

for i in lines:
    for j in lines:
        for k in lines:
            s = int(i) + int(j) + int(k)
            if s == 2020:
                print(i, j, k)
                print(int(i)*int(j)*int(k))
                break

print('nothing')