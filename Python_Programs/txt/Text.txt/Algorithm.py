'''
number=int(input("Enter number"))
number2=int(input("Set Start point"))
i=0
e=0
for i in range(number2,number):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i) 
'''   
'''         
number=int(input("Enter number"))

def factorial(number):
    i=1
    for m in range(2,number+1):
        i=i*m
    print(i)

factorial(number)  

'''
'''
number=int(input("Enter number") )
limit=int(input("Set limit"))

while number<limit:
    number=number+1
    for i in range(number,limit):
        e=i
      
        print((i-1)+(i-2))
        break
'''
number=int(input("Number:"))
count=0
for i in range(1,number+1):
    if(i%5==0 or i%3==0):
        print(count)
        count=count+i
    
print(count)   


   







