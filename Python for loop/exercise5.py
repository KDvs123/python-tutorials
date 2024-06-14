#Write a program that prints following shape

# *
# **
# ***
# ****
# *****

for i in range (0,6):
    for j in range(i):
        print("*",end=" ")
    print(" ")


# sample answer

# for i in range(1,6):
    # s = ''
    # for j in range(i):
        # s += '*'
    # print(s)