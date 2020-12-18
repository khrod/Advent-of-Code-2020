text_file = open('d4-input', 'r')

passports = text_file.read().split('\n\n')

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
fields_required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

c = 0
for passport in passports:
    lines = passport.split('\n')
    # print(lines)
    fields = []
    for line in lines:
        pairs = line.split(' ')
        fields.extend(pairs)

    # print(fields)
    field_names = [f.split(':')[0] for f in fields]
    # print(field_names)

    valid = True
    for field in fields_required:
        if field not in field_names:
            valid = False

    if valid:
        c += 1

print(c)
