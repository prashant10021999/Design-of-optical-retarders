def change_sign_except_first_row_and_diagonal(matrix):
    # Create a new matrix to store the transformed elements
    transformed_matrix = []

    # Iterate through each row in the original matrix
    for i, row in enumerate(matrix):
        # Create a new row to store the transformed elements of the current row
        transformed_row = []
        
        # Iterate through each element in the current row
        for j, element in enumerate(row):
            # Check if the element is on the first row or the diagonal
            if i == 0 or i == j:
                # Leave the element unchanged
                transformed_row.append(element)
            else:
                # Change the sign of the element and add it to the new row
                transformed_row.append(-element)
        
        # Add the transformed row to the new matrix
        transformed_matrix.append(transformed_row)

    return transformed_matrix

def get_user_input_matrix():
    print("Enter a 4x4 matrix:")
    matrix = []
    for i in range(4):
        row_input = input(f"Enter row {i + 1} elements separated by spaces: ")
        row_elements = [float(element) for element in row_input.split()]
        if len(row_elements) != 4:
            print("Error: Each row must have exactly 4 elements.")
            return None
        matrix.append(row_elements)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(element) for element in row))

# Get user input for the matrix
user_matrix = get_user_input_matrix()

if user_matrix:
    # Call the function to transform the matrix
    transformed_matrix = change_sign_except_first_row_and_diagonal(user_matrix)

    # Print the transformed matrix
    print("Original Matrix:")
    print_matrix(user_matrix)

    print("Transformed Matrix:")
    print_matrix(transformed_matrix)
