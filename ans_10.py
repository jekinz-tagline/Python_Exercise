# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
k = 1
for i in range(0,5):
    for j in range(0,i+1):
        print(k,end=" ")
        k += 1
    print()


# *****
# *   * 
# *   * 
# *   * 
# *****
for i in range(0,5):
    for j in range(0,5):
        if i == 0 or i == 4 or j == 0 or j == 4: 
            print("*",end="")
        else:
            print(" ",end="")
    print()


# *
# * *
# *  *
# *   *
# ******
for i in range(0,6):
    for j in range(0,i):
        if j == 0 or i == 5 or j == i -1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#     *
#   * * *
# * * * * * 
#   * * *
#     *
for i in range(0,3):
        print(" "*(2-i) + "*"*((2*i)+1))
for i in range(0,3):
        print(" "*(i+1) + "*"*((2*((2)-i))-1))


# ******
# **  **
# *    *
# *    *
# **  **
# ******
for i in range (0,3):
    for j in range(3-i):
        print("*", end ="") #printing half of stars for all rows
    for k in range(2*i):
        print(" ", end = "")# printing spacec for all rows
    for l in range(3-i):
        print("*", end ="") #printing other half of stars for all rows
    print()

#priting lower part of diamond

for a in range(1,4):
    for b in range(a):
        print("*", end = "")  #printing half of stars for all rows
    for c in range(2*(3-a)):
        print(" ", end = "")  # printing spacec for all rows      
    for d in range (a):
        print("*", end ="")   #printing other half of stars for all rows    
    print()