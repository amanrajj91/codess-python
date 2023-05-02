Solve a linear algebra problem. There is a test with 40 questions worth 200 marks. The test has two types of questions: 1. true or false – carries 4 marks each 2. Multiple-choice – carries 9 marks each. Find the number of true or false and multiple-choice questions

from scipy.linalg import solve

import numpy as np

coefficients = np.array([[1, 1], [4, 9]])

constants = np.array([40, 200])

solutions = solve(coefficients, constants)

x = solutions[0]

y = solutions[1]

print("Number of true or false questions (x):", x)

print("Number of multiple-choice questions (y):", y)





Also find the Eigen values and Eigen vectors of the given matrix

import numpy as np

from scipy.linalg import eig

matrix = np.array([[1, 1], [4, 9]])

eigenvalues, eigenvectors = eig(matrix)

print("Eigenvalues:")

print(eigenvalues)

print("\nEigenvectors:")

print(eigenvectors)






Verify FFT and IFFT operations on an numpy array

import numpy as np

x = np.array([1, 2, 3, 4])

x_fft = np.fft.fft(x)

x_ifft = np.fft.ifft(x_fft)

print("Original Array:")

print(x)

print("FFT Result:")

print(x_fft)

print("IFFT Result:")

print(x_ifft)

print("IFFT Result matches original array:")

print(np.allclose(x, np.real(x_ifft)))