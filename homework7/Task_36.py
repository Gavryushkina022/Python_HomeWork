num_rows = 6
num_columns = 6

print_operation_table = lambda x, y: (x + y) * 5

def create_matrix():
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(print_operation_table(i, j), end=" ")
        print(" ")


create_matrix()
