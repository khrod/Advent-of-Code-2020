text_file = open('d5-input', 'r')

lines = text_file.read().split('\n')

max_seat_id = 0
for line in lines:
    row_input = line[:7]
    col_input = line[7:]

    row_bin = row_input.replace('F', '0').replace('B', '1')
    col_bin = col_input.replace('L', '0').replace('R', '1')

    row_dec = int(row_bin, 2)
    col_dec = int(col_bin, 2)

    seat_id = row_dec * 8 + col_dec

    if seat_id > max_seat_id:
        max_seat_id = seat_id

print(max_seat_id)
