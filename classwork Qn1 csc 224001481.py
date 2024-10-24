strings = ['mango', 'orange', 'pineapple']#initialising strings
dict_of_str = {}#creating a dictionary
for n in range(len(strings)):
    dict_of_str[strings[n]] = len(strings[n])#initialising the dictionary

print(dict_of_str) #printing the dictionary