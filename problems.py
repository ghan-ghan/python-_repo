








''' 1. Find all of the numbers from 1-1000 that are divisible by 8 '''


num =1
count =0
while num <=1000:
    if num % 8==0:  
        count +=1
        print(num)
    num +=1
print(f"The total {count} numbers are  present  between 1-1000  which are divisible by 8. ")



''' 2. Find all of the numbers from 1-1000 that have a 6 in them '''


num =1 
count =0
while num <=1000:
    if  (num//100==6 or num%10 ==6) or (num//10 %10 ==6):
        count+=1
        print(num)
    num +=1
print(f"Sum of the numbers containing 6 between 1-1000 is {count}")



''' 3. Count the number of spaces in a string '''

string=input("Enter the words or any string : ")
count =0
for i in string:
    if i ==" ":
        count+=1
print(count)




''' 4.Remove all of the vowels in a string '''

vowels=["a","e","i","o","u","A","E","I","O","U"]
updated_string =""
string = input("Enter the string: ")
for i in range(len(string)):
    if string[i] not in vowels:
        updated_string+=(string[i])
print(updated_string)




''' 5. Find all of the words in a string that are less than 5 letters '''


string=input("enter the string: ").split()
for i in string:
    if len(i) <=5:
        print(i)



''' 6. Use a dictionary comprehension to count the length of each word in a sentence '''


words=input("Enter the words : ").split()
length= {word:len(word) for word in words}
print(length)



''' 7. For all the numbers 1-1000, use a nested 
list/dictionary comprehension to find the highest single digit any of the numbers 
is divisible by '''


highest_num = {i:max(j for j in range(2,10) if i % j == 0) for i in range(1,1001) if [j for j in range(2,10) if i % j == 0]}
print(highest_num)                   






