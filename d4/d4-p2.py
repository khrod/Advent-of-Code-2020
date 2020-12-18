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
ecl_valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

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

    for field in fields:
        pair = field.split(':')
        field_name = pair[0]
        field_value = pair[1]
        if field_name == 'byr':
            # four digits; at least 1920 and at most 2002.
            if not (1920 <= int(field_value) <= 2002):
                valid = False
        elif field_name == 'iyr':
            # four digits; at least 2010 and at most 2020.
            if not (2010 <= int(field_value) <= 2020):
                valid = False
        elif field_name == 'eyr':
            # four digits; at least 2020 and at most 2030.
            if not (2020 <= int(field_value) <= 2030):
                valid = False
        elif field_name == 'hgt':
            # a number followed by either cm or in:
            # If cm, the number must be at least 150 and at most 193.
            # If in, the number must be at least 59 and at most 76.
            height = 0
            if field_value.endswith('cm'):
                height = int(field_value.split('cm')[0])
                if not (150 <= height <= 193):
                    valid = False
            elif field_value.endswith('in'):
                height = int(field_value.split('in')[0])
                if not (59 <= height <= 76):
                    valid = False
            else:
                valid = False
        elif field_name == 'hcl':
            # a # followed by exactly six characters 0-9 or a-f.
            if field_value.startswith('#'):
                hair_color = field_value[1:]
                if not (len(hair_color) == 6 and hair_color.isalnum()):
                    valid = False
            else:
                valid = False
        elif field_name == 'ecl':
            # exactly one of: amb blu brn gry grn hzl oth.
            if field_value not in ecl_valid:
                valid = False
        elif field_name == 'pid':
            # a nine-digit number, including leading zeroes.
            if not (len(field_value) == 9 and field_value.isnumeric()):
                valid = False

    if valid:
        c += 1

print(c)
