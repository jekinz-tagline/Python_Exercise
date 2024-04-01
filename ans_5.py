# this is my own way
numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
possible_pair = []

input_n = int(input("Enter n :- "))
numbers = set(numbers)

for element_1 in numbers:
    for element_2 in numbers:
        if element_1 + element_2 == input_n:
            possible_pair.append([element_1,element_2])

for pair in possible_pair:
    if pair in possible_pair:
        possible_pair.remove(pair)

if len(possible_pair) == 0:
    print("No match found..!!")
else:
   print(possible_pair)

# this is suggested by darshan sir
from itertools import combinations

nums = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
all_possible_pair = list(combinations(nums,2))
final_arr = []
input_n = int(input("Enter n :- "))

for pair in set(all_possible_pair):
    if (pair[0] + pair[1] == input_n) and (pair not in final_arr):
        final_arr.append(pair)

for j in final_arr:
    if (j[0],j[1]) and (j[1],j[0]) in final_arr:
        final_arr.remove(j)

if len(final_arr) == 0:
    print("No match found..!!")
else:
   print(final_arr)