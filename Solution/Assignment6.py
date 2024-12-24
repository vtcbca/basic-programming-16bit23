def pattern_list_comprehension(rows):
    [print("* " * i) for i in range(1, rows + 1)]

rows = int(input("Enter the number of rows: "))
pattern_list_comprehension(rows)
