#ex07

# Dictionary containing names and ages
age = {'Hans': 24, 'Prag': 23, 'Bunyod': 18}

# Print the age of 'Hans'
print(age['Hans'])  # Output: 24

# Change the age of 'Prag' to 30
age['Prag'] = 30

# Print the updated age of 'Prag'
print(age['Prag'])  # Output: 30

# Delete key-value pair of 'Bunyod' from the dictionary
del age['Bunyod']

# Print the updated dictionary
print(age)  # Output: {'Hans': 24, 'Prag': 30}