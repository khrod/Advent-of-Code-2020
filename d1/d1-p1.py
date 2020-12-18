text_file = open('d1-input', 'r')

lines = text_file.read().split('\n')

print(lines)

for i in lines:
    for j in lines:
        s = int(i) + int(j)
        if int(i) != int(j) and s == 2020:
            print(i, j)
            print(int(i)*int(j))
            break
