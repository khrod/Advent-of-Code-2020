text_file = open('d6-input', 'r')

groups = text_file.read().split('\n\n')

s = 0
for group in groups:
    print(group)
    answers = group.replace('\n', '')
    answers_unique = ''.join(set(answers))
    print(answers_unique)

    for c in answers_unique:
        if all([c in person for person in group.split('\n')]):
            s += 1

print(s)
