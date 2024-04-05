numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]

options = """\nA. Length of the list
B. Display 3 numbers
C. Display sum of odd numbers
D. Number of duplicate numbers
E. Display list without duplicate numbers"""
print(options)

user_opt = input("\nSelect your choice : ")

match user_opt:
    case "A" : 
        print("\nLength of the list",len(numbers))

    case "B" : 
        print("\nFirst 3 numbers: ",numbers[0:3])
    
    case "C" :
        total = 0
        for i in numbers:
            if i%2 != 0:
                total += i
        print("\nSum of odd numbers: ",total)
    
    case "D" :
        org = len(numbers)
        dup = len(set(numbers))
        print("Number of duplicate numbers: ",(org - dup)-1)
    
    case "E" :
        without_duplicate = []
        for i in numbers:
            if i not in without_duplicate:
                without_duplicate.append(i)
        print("List without duplicate numbers: ",without_duplicate)