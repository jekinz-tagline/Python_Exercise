# Replacing the wrong term of AP
AP = [2, 5, 8, 11, 15, 17]
diff = 0
AP_first_term = AP[0]
AP_number_of_terms = len(AP)

if AP[1] - AP[0] == AP[2] - AP[1]:
    diff = AP[1] - AP[0]

for i in range(AP_number_of_terms):
    if AP[i] != (AP_first_term + ((i+1)-1) * diff):
        AP[i] = (AP_first_term + ((i+1)-1) * diff)

print("Correct A.P. :- ",AP)


# Replacing the wrong term of GP 
GP = [2,4,8,16,33,64]
ratio = 0
GP_first_term = GP[0]
GP_number_of_terms = len(GP)

if GP[1] / GP[0] == GP[2] / GP[1]:
    ratio = (GP[1] / GP[0])

for i in range(GP_number_of_terms):
    if GP[i] != (GP_first_term * (ratio ** ((i+1)-1))):
        GP[i] = int((GP_first_term * (ratio ** ((i+1)-1))))

print("Correct G.P. :- ",GP)