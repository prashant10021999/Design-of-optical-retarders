import numpy as np

def compute_J(I):
    J = np.zeros((4, 4))
    for i in range(4):
        J[i, 0] = np.sqrt((I[i, 2] - I[i, 4])**2 + (I[i, 3] - I[i, 5])**2 + (I[i, 1] - I[i, 0])**2)
        J[i, 1] = I[i, 2] - I[i, 4]
        J[i, 2] = I[i, 3] - I[i, 5]
        J[i, 3] = I[i, 1] - I[i, 0]
    return J

def main():
    I = np.zeros((4, 6))
    
    # Taking user input for elements of matrix I (comma-separated values for each row)
    print("Enter the elements of matrix I (4x6):")
    for i in range(4):
        row_values = input(f"Row {i+1} (comma-separated values): ")
        row_values = [float(val) for val in row_values.split(',')]
        if len(row_values) != 6:
            print("Invalid input! Please enter 6 comma-separated values for each row.")
            return
        I[i, :] = row_values

    # Computing matrix J
    J = compute_J(I)

    # Matrix W
    W = np.array([[1, 0, 0, 1],
                  [1, 0, 0, -1],
                  [-1, 0, 2, -1],
                  [-1, 2, 0, -1]])

    Io = float(input("Enter the value of Io: "))

    # Computing matrix M
    M = np.dot(W, J) / (4 * Io)

    # Displaying the results
    print("\nMatrix M:")
    print(M)
    print("\nMatrix I:")
    print(I)
    

if __name__ == "__main__":
    main()
