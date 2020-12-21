text_file = open('d6-input', 'r')

groups = text_file.read().split('\n\n')

s = 0
for group in groups:
    answers = group.replace('\n', '')
    answers_unique = ''.join(set(answers))

    s += len(answers_unique)

print(s)
