
        
  ======if========      
    
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

	===================
# if condition
mystring="hello"
myfloat=10.0
myint=5
if mystring == "hello":
    print ("value: %s" % mystring)
elif myfloat==10.0:
    print("value: %f" % myfloat)
else:
    print("value: %d" % myint)

	
	=========for ===========
	# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

	
=========== for continue pass ===============
	
	##for condition

var='python'

for i in var:
    if i=="h":
        print("letter is in if condition: %s" % i)
        continue
    elif i=="p":
        print("The pass statement is a null operation; nothing happens when it executes:: %s" % i)
        pass
    print("letter is: %s" % i)
	

==========while =========	
# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1


=============== break =============
#while condition

var=10

while var > 0:
    print ("value is :%d" % var)
    var = var - 1
    if var == 5:
        print("value is : %d" %var)
        break
    

	
==============break and continue=============	
# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)


=========else in while loop ==========	
	# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
	
	
	
===========prime no ===============
num = range(10,20)
for i in num:
    for j in range(2,i):
        if i%j==0:
            k=i/j
            print("value i= %d  is j= %d * k= %d " %(i,j,k))
            break
    else:
        print ('%d is a prime no  ' %i)