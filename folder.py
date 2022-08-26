


#first 10 even numbers:
n=2 
count=0
while count <10:
    if n%2 ==0:
        count+=1
        print(n)
    n+=1

#first 10 odd numbers: 
n=1
while n <10:
    print(n)
    n+=1

#first 10 whole  numbers:
n=1
count=0
while count <10:
    print(count)
    count+=1
    n+=1


#first 10 integers and their squares
n=1
count=0
while count <10:
    print(n,n**2)
    count +=1
    n+=1


#loop statements to print the series of increasing order :
n=10
while n <=300:
    print(n)
    n+=1


#program to find the first natural number in reverse ordre :
num = 10
while(num >= 1) :
    print(num)
    num -=1

#program to find the series in the decreasing order :
num = 105
while num >=7:
    print(num)
    num -=7

#print  to sum of the first 10 evne numbers:

num =2
count =0
sum =0
while count < 10:

    if num %2 ==0:
        count +=1
        sum +=num
        print(sum)
        num +=2
print(f"/n")

#multiplication of the numbers of the users enterd the numbers:
num=int(input("enter the numbers: "))  
i =1 
while i <=10:
    print(num, "X" ,i, "=",i*num)    
    i +=1



num1 = int(input("Enter first number  : "))
num2 = int(input("Enter second number  : "))
if num1 > num2:
    
    while(num1>num2):
        if num2 % 2 == 0:
            print(num1)
        num1 = num1 + 1
else:
    while(num1<num2):
        if num2 % 2 == 0:
            print(num2)
        num2 = num2 + 1


