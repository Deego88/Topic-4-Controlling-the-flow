a = int(input("enter positive integer:"))
b = 2

# taking the current value and, if it is even,
# divides it by 2
while a > 1:

   if (a % b) ==0:
        a = int(a/b)
        
# but if it is odd, multiply
# it by 3 and adds
else:
        a = int((a * 3 ) + 1)
        print (a)


