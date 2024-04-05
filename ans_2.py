names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']
name_lengths = []

# print all names of given list
print("\nNames: ",names)

# store and print list of each name's length
for name in names:
    name_lengths.append(len(name))
print("\nName length: ",name_lengths)

# make dictonary and store same length name's list
my_dict = {}
for name in names:
    length = len(name)
    if length not in my_dict:
        my_dict[length] = [name]
    else:
        my_dict[length].append(name)

# store list which are having same length of name
same_length_name = []
for keys in my_dict:
    same_length_name.append(my_dict[keys])

# print 3 most frequent names
same_length_name.sort(key=lambda item: (len(item),item[0]),reverse=True)
print("\nThe three most frequent name lenghts are: ")
for i in range(3):
    print(f"{len(same_length_name[i])} names of length {len(same_length_name[i][0])}: ",same_length_name[i])

# print 3 least frequent names
same_length_name.sort(key=lambda item: (len(item),item[0]))
print("\nThe three least frequent name lenghts are: ")
for i in range(3):
    print(f"{len(same_length_name[i])} names of length {len(same_length_name[i][0])}: ",same_length_name[i])