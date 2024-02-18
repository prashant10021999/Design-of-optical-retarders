def calculate_I(m):
    Io = 1

    # Calculate elements of matrix I using the given relations
    I = [
        [Io * (m[0][0] - m[0][3] - m[1][0] + m[1][3]), Io * (m[0][0] + m[0][3] - m[1][0] - m[1][3]),
         Io * (m[0][0] + m[0][1] - m[1][0] + m[1][1]), Io * (m[0][0] + m[0][2] - m[1][0] - m[1][2]),
         Io * (m[0][0] - m[0][1] - m[1][0] - m[1][1]), Io * (m[0][0] - m[0][2] - m[1][0] + m[1][2])],
        [Io * (m[0][0] - m[0][3] - m[3][0] - m[3][3]), Io * (m[0][0] + m[0][3] - m[3][0] + m[3][3]),
         Io * (m[0][0] + m[0][1] - m[3][0] - m[3][1]), Io * (m[0][0] + m[0][2] - m[3][0] - m[3][2]),
         Io * (m[0][0] - m[0][1] - m[3][0] + m[3][1]), Io * (m[0][0] - m[0][2] - m[3][0] + m[3][2])],
        [Io * (m[0][0] - m[0][3] - m[2][0] + m[2][3]), Io * (m[0][0] + m[0][3] - m[2][0] - m[2][3]),
         Io * (m[0][0] + m[0][1] - m[2][0] - m[2][1]), Io * (m[0][0] + m[0][2] - m[2][0] + m[2][2]),
         Io * (m[0][0] - m[0][1] - m[2][0] + m[2][1]), Io * (m[0][0] - m[0][2] - m[2][0] - m[2][2])],
        [Io * (m[0][0] - m[0][3] + m[1][0] - m[1][3]), Io * (m[0][0] + m[0][3] + m[1][0] + m[1][3]),
         Io * (m[0][0] + m[0][1] + m[1][0] - m[1][1]), Io * (m[0][0] + m[0][2] + m[1][0] + m[1][2]),
         Io * (m[0][0] - m[0][1] + m[1][0] + m[1][1]), Io * (m[0][0] - m[0][2] + m[1][0] - m[1][2])]
    ]

    return I


def get_matrix_from_user(rows, cols, name):
    matrix = []
    print(f"Enter elements of matrix {name} ({rows}x{cols}):")

    for i in range(rows):
        row = []
        # Input one row at a time, space-separated
        elements = input(f"Enter {name}{i + 1} (space-separated values): ")
        elements = [float(e) for e in elements.split()]
        if len(elements) != cols:
            print(f"Invalid input! Please enter {cols} values separated by spaces.")
            return get_matrix_from_user(rows, cols, name)  # Ask for input again
        row = elements
        matrix.append(row)

    return matrix


def main():
    # Taking user input for matrix M (4x4)
    m = get_matrix_from_user(4, 4, 'M')

    # Calculate matrix I (4x6) using the provided relations
    I = calculate_I(m)

    # Display matrix I
    print("\nMatrix I (4x6):")
    for row in I:
        print(row)


if __name__ == "__main__":
    main()
