text_file = open('d5-input', 'r')

lines = text_file.read().split('\n')

# Not at the very front or very back
# -> seat_id > 7 and seat_id < 1016
# seat_id + 1 and seat_id - 1 are in list

seat_id_list = []
for line in lines:
    row_input = line[:7]
    col_input = line[7:]

    row_bin = row_input.replace('F', '0').replace('B', '1')
    col_bin = col_input.replace('L', '0').replace('R', '1')

    row_dec = int(row_bin, 2)
    col_dec = int(col_bin, 2)

    seat_id = row_dec * 8 + col_dec

    seat_id_list.append(seat_id)

print(seat_id_list)

for i in range(8, 1016):
    if (i not in seat_id_list) and ((i + 1) in seat_id_list) and ((i - 1) in seat_id_list):
        print(i)
