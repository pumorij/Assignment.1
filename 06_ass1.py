# Q6
a=input("Input string: ")
length=len(a)
if(length>2):
    if(a[-3: ]=="ing"):
        a=a+"ly"
    else:
        a=a+"ing"
print(a)