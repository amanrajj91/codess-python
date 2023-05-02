BASIC STRING OPERATIONS

print("STRING OPERATIONS")

str1="jacob john"

print(str1)

print("length of the string: ", len(str1))

print("uppercase: ", str1.upper())

print("lowercase: ", str1.lower())

print("slicing the string: ", str1[0:3])

print("sorting the string: ", sorted(str1))

str2="RJJ"

print("appending the string: ", str1+str2)

print("---------------------------------------\n")






BASIC LIST OPERATIONS

print("LIST OPERATIONS")

ts=['Glitch', 'Maroon', 'Anti-hero', 'Midnight Rain', 'Paris', 'Mastermind']

print(ts)

print("sorting the list: ", sorted(ts))

ts.insert(1, 'Karma')

print("inserting: ")

print(ts)

print("length: ", len(ts))

ts2=['Question']

print("appending the list: ", ts+ts2)

print("---------------------------------------\n")






TUPLE OPERATIONS

print("TUPLE OPERATIONS")

tup_1= (1523, 5113, 1873, 2593, 9123)

print(tup_1)

print("length of the tuple: ", len(tup_1))

print("slicing the tuple: ", tup_1[0:1])

print("accessing the tuple elements: ", tup_1[4])

tup_2=(0, 253)

tup_2=tup_1+tup_2

print("joining 2 tuples: ")

print(tup_2)

print("---------------------------------------\n")






DICTIONARY OPTIONS

print("DICTIONARY OPERATIONS")

my_dictionary={"First Name":"Chinmay", "Last Name":"Khanolkar ", "Height":"5.4", "DOB":"20062003"}

print(my_dictionary)

my_dictionary.update({"First Name":"Jacob", "Last Name":"John", "Height":"6.1", "DOB":"02052003"})

print(my_dictionary)






SET OPERATIONS

print("SET OPERATIONS")

set1={9, 18, 6, 5, 4}

set2={15, 18, 16, 22}

print("set1={9, 18, 6, 5, 4}")

print("set2={15, 18, 16, 22}")

print("union of 2 sets: ", set1.union(set2))

print("intersection of 2 sets: ", set1.intersection(set2))

print("---------------------------------------\n")