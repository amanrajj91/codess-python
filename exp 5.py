Create a database with name, add the Roll no name, age, mobile no details of these students using insert operation. Update the database for one more student. Display the database entries. Delete one entry in the database

import sqlite3

conn = sqlite3.connect('STUDENT.db')

print("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS Student (

Roll_No INTEGER,

Name TEXT,

Age INTEGER,

Mobile_No TEXT

)''')

conn.execute("INSERT INTO Student (roll_no, name, age, mobile_no) VALUES (1, 'Jacob0', 21, '3458479729')")

conn.execute("INSERT INTO Student (roll_no, name, age, mobile_no) VALUES (2, 'Jacob1', 21, '5338479729')")

conn.execute("INSERT INTO Student (roll_no, name, age, mobile_no) VALUES (3, 'Jacob2', 21, '5668479729')")

conn.execute("INSERT INTO Student (roll_no, name, age, mobile_no) VALUES (4, 'Jacob3', 21, '7848479729')")

conn.execute("INSERT INTO Student (roll_no, name, age, mobile_no) VALUES (5, 'Jacob4', 21, '8688479729')")

conn.commit()

print("Records created successfully")

cursor = conn.execute("SELECT roll_no, name, age, mobile_no from Student")

for row in cursor:

print("Roll No = ", row[0])

print("Name = ", row[1])

print("Age = ", row[2])

print("Mobile No = ", row[3], "\n\n")

conn.execute("DELETE from Student where roll_no = 5;")

conn.commit()

print("After deleting")

cursor = conn.execute("SELECT roll_no, name, age, mobile_no from Student")

for row in cursor:

print("Roll No = ", row[0])

print("Name = ", row[1])

print("Age = ", row[2])

print("Mobile No = ", row[3], "\n\n")

conn.close()






Write Python program to study define, edit arrays and perform arithmetic operations using numpy.

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])

arr2 = np.array([6, 7, 8, 9, 10])

print("Array 1: ", arr1)

print("Array 2: ", arr2)

arr1[0] = 10

arr2[3] = 15

print("Updated Array 1: ", arr1)

print("Updated Array 2: ", arr2)

sum_arr = arr1 + arr2

diff_arr = arr1 - arr2

mul_arr = arr1 * arr2

div_arr = arr1 // arr2

print("Sum of Array1 and Array2: ", sum_arr)

print("Difference Array1 and Array2: ", diff_arr)

print("Product Array1 and Array2: ", mul_arr)

print("Division Array1 and Array2: ", div_arr)







Write python program to study selection, indexing, merging, joining, and concatenation in data frames

1) (selection)
import pandas as pd

df1 = pd.DataFrame({'Name': ['Jacob', 'Chinmay', 'Manthan', 'Aaryan'],

'Age': [22, 22, 30, 28],

'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco']})

print("Selection")

print("\n1. Original data frame df1:")

print(df1)

print("\n2. Select column 'Name' in df1:")

print(df1['Name'])

print("\n3. Select row at index 1 in df1:")

print(df1.loc[1])

print("\n4. Select rows with Age > 25 in df1:")

print(df1[df1['Age'] > 25])

2) (indexing)
import pandas as pd

car_info1 = pd.DataFrame({'Brand': ['Toyota', 'Honda', 'Ford', 'Chevrolet'],

'Model': ['Camry', 'Civic', 'Mustang', 'Cruze'],

'Year': [2018, 2020, 2017, 2019]})

car_info2 = pd.DataFrame({'Brand': ['Honda', 'Chevrolet', 'Toyota', 'Nissan'],

'Color': ['Blue', 'Red', 'Black', 'White'],

'Price': [25000, 22000, 28000, 23000]})

car_info1 = car_info1.set_index('Brand')

print("car_info1 with 'Brand' column as index:")

print(car_info1)

car_info1 = car_info1.reset_index()

print("\nReset index in car_info1:")

print(car_info1)

3) (merging)
car_info1 = pd.DataFrame({'Brand': ['Toyota', 'Honda', 'Ford', 'Chevrolet'],

'Model': ['Camry', 'Civic', 'Mustang', 'Cruze'],

'Year': [2018, 2020, 2017, 2019]})

car_info2 = pd.DataFrame({'Brand': ['Honda', 'Chevrolet', 'Toyota', 'Nissan'],

'Color': ['Blue', 'Red', 'Black', 'White'],

'Price': [25000, 22000, 28000, 23000]})

print("\nOriginal car_info1 data frame:")

print(car_info1)

print("\nOriginal car_info2 data frame:")

print(car_info2)

car_merged = pd.merge(car_info1, car_info2, on='Brand')

print("\nMerged data frame:")

print(car_merged)

4) (joining)
car_info1 = pd.DataFrame({'Brand': ['Toyota', 'Honda', 'Ford', 'Chevrolet'],

'Model': ['Camry', 'Civic', 'Mustang', 'Cruze'],

'Year': [2018, 2020, 2017, 2019]})

car_info2 = pd.DataFrame({'Brand': ['Honda', 'Chevrolet', 'Toyota', 'Nissan'],

'Color': ['Blue', 'Red', 'Black', 'White'],

'Price': [25000, 22000, 28000, 23000]})

car_info1 = car_info1.set_index('Brand')

car_info2 = car_info2.set_index('Brand')

car_joined = car_info1.join(car_info2, how='inner')

#The how parameter is set to inner to specify that only the common rows between car_info1 and car_info2 should be included in the joined data frame.

#it selects only the rows where the "Brand" values exist in both car_info1 and car_info2.

print("Joined data frame:")

print(car_joined)

5) (concentration)
car_info1 = pd.DataFrame({'Brand': ['Toyota', 'Honda', 'Ford', 'Chevrolet'],

'Model': ['Camry', 'Civic', 'Mustang', 'Cruze'],

'Year': [2018, 2020, 2017, 2019]})

car_info2 = pd.DataFrame({'Brand': ['Nissan', 'Mercedes', 'BMW', 'Audi'],

'Model': ['Altima', 'C-Class', '3 Series', 'A4'],

'Year': [2016, 2019, 2018, 2020]})

car_concatenated = pd.concat([car_info1, car_info2], ignore_index=True)

#The ignore_index=True parameter is used to reset the index of the concatenated data frame.

#When ignore_index is set to True, the resulting data frame will have a new sequential index starting from 0, ignoring the original index values from car_info1 and car_info2.

print("Concatenated data frame:")

print(car_concatenated)





