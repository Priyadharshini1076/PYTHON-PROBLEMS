#level-1
#1.write prgm to print name ,age and college name
'''name=input("Enter your name:")
age=int(input("Enter your age:"))
college=input("Enter your college name:")

print("name: ",name)
print("Age: ",age)
print("college name:",college)'''

#2.Take two no from user ans sum,diff,prod,div of num
'''num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
add=num1+num2
diff=num1-num2
mul=num1*num2
div=num1/num2
print("Addition: ",add)
print("Difference: ",diff)
print("multiple: ",mul)
print("division: ",div) '''

#3.Take number from user and check whether it is odd or even
'''number=int(input("Enter number:"))
if number%2==0:
    print(f"{number} is Even")
else:
    print(f"{number} is odd")'''

#4.squre and cube of given number
'''number=int(input("Enter number:"))
sqrt=number*number
cube=sqrt*number
print("squar of number:",sqrt)
print("cube of number:",cube)'''

#LEVEL-2
#6.find positive,negative,zero
'''number=int(input("Enter number:"))
if number>0:
    print(f"{number} is positive")
elif number<0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")'''

#7.take input from user and assing grade
'''mark=int(input('enter your mark'))
if mark>=90:
    print("GRADE: A")
elif mark>=75:
    print("GRADE: B")
elif mark>=50:
    print("GRADE: C")
elif mark>=45:
    print("GRADE: D")
else:
    print("fail")'''

#8.Find large number
'''num1=123
num2=345
num3=678
if num1>num2 and num1>num2:
    print("greater number:",num1)
elif num2>num1 and num2>num3:
    print("greater number:",num2)
else:
    print("greater number:",num3)'''

#9.Leap year
'''year=int(input("Enter year:"))
if (year%400==0 and year&100==0) or year%4==0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")'''
         
#10.discount calculate
'''amount=int(input("Enter amount:"))
discount=amount*0.10
if amount>1000:
    print("Actual amount:",amount)
    amount-=discount
    print("discounted amount:",discount)
    print("total amount:",amount)
else:
    print("discount not allowed!")'''

#LEVEL-3
#11.print num 1 to 10 using for
'''for i in range(1,11):
    print(i)'''

#12.multiplication table
'''table=int(input("Enter table no:"))
for i in range(1,11):
    result=i*table
    print(f"{i}X{table}={result}")'''

#13.sum of natural number
'''limit=int(input("Enter limit"))
sum=0
for i in range (1,limit+1):
    sum=sum+i
print("sum of numbers:",sum)'''

#14.print even number in range
'''limit=int(input("Enter limit:"))
for i in range(1,limit+1):
    if i%2==0:
       print(i)'''

#15.factorial of number
'''num=int(input("Enter number:"))
fact=1
for i in range(1,num+1):
    fact*=i
print("factprial of number:",fact)'''

#LEVEL--4
#16.add item into list and perform sum and avg
'''lists=[]
sum=0
avg=0
for i in range(1,6):
    list_item=int(input(f"Enter item {i}"))
    lists.append(list_item)
    sum+=list_item
    avg=sum/len(lists)

print("Sum is: ",sum)
print("avg is: ",avg)'''

#17.find large and small number in list
'''lists=[23,56,32,78,45]
large=max(lists)
small=min(lists)
print("largest element is : ",large)
print("smallest element is : ",small)'''

#18.reverse string without build in functions
'''str=input("Enter String:")
reverse=str[::-1]
print("Original String:",str)
print("Reversed string:",reverse)'''

#19.count vowels and consonants in a string
'''str=input("entre a string").lower()
vowel=0
const=0
for i in range(0,len(str)):
    ch=str[i]
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        vowel+=1
    else:
        const+=1
    
print("vowels :",vowels)
print("consonants :",const)'''


#20.palindrom
'''str=input("Enter String:")
reverse=str[::-1]
if str==reverse:
    print("palindrome")
else:
    print("Not a prindrome")'''

#21.function:prime number
'''number=int(input("Enter a number:"))
def isPrime(number):
    if number<=1:
        return False
    for i in range(2,number):
        if number%i == 0:
            return False
        return True
if isPrime(number)==True:
    print("Prime number")
else:
    print("Not a Prime Number")'''

#22.function:factorial
'''num=int(input("Enter a number:"))
def isFactorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    print("facorial of number:",fact)
isFactorial(num)'''


#23.function:fibonaaci series
'''limit=int(input("Enter limit:"))
def isFibonaaci(limit):
    a=0
    b=1
    lists=[0,1]
    for i in range(2,limit):
        c=a+b
        a=b
        b=c
        res=lists.append(c)
    print(lists)
isFibonaaci(limit)'''

#24.function:sum of natural number
'''limit=int(input("Enter limit:"))
def isNatural(limit):
    sum=0
    for i in range(1,limit+1):
        sum+=i
    print("Sum of N numbers:",sum)
isNatural(limit)'''

#25.Sum of digit
'''num=int(input("Enter number:"))
def isSumDigit(num):
    sum=0
    while num>0:
        n=num%10
        sum+=n
        num//=10
    print(sum)
isSumDigit(num)'''

#DAY-2
#swap no without 3rd var
'''a=int(input("Enter a:"))
b=int(input("Enter b:"))
print("Before swap")
print("a= ",a)
print("b= ",b)
a=a+b
b=a-b
a=a-b
print("After swap")
print("a= ",a)
print("b= ",b)'''

#largest of 3 num
'''a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a>b and a>c:
    print("Largest of given three number is: ",a)
elif b>a and b>c:
    print("Largest of given three number is: ",b)
else:
    print("Largest of given three number is: ",c)'''


#prime number
'''num=int(input("Enter number:"))
def isPrime(num):
    while num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
        return True
if isPrime(num)==True:
    print("Prime number")
else:
    print("Not a Prime Number")
isPrime(num)'''

#fibonaaci series
'''num=int(input("Enter number:"))
a=0
b=1
lists=[0,1]
for i in range(2,num):
    c=a+b
    a=b
    b=c
    lists.append(c)
print(lists)'''

#factorial
'''num=int(input("Enter number:"))
fact=1
for i in range(1,num+1):
    fact*=i
print("Factorial of a number is:",fact)'''

#count vowels
'''str=input("Enter string:").lower()
vowel=0
for i in str:
    if(i=='a' or i=='e' or i=='o' or i=='i' or i=='u'):
        vowel+=1
print("vowels :",vowel)'''

#check a palindrom
'''str=input("Enter string:").lower()
rev=str[::-1]
if str==rev:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not a palindrome")'''


#sum of digits
'''num=int(input("Enter number:"))
sum=0
while num>0:
    n=num%10
    sum+=n
    num//=10
print("Sum of digit is:",sum)'''

#second large element in a list
'''lists=[4,6,7,8,3]
lists.sort()
large=lists[-2]
print(large)'''

#range of prime numbers
'''limit=int(input("Enter limit:"))
res=[]
for i in range(1,limit+1):
    if i%2!=0:
     res.append(i)
print(res)'''
    

#amstrong Number
'''num=int(input("Enter number:"))
l=[]
ams=0
n1=num
while n1>0:
    n=n1%10
    l.append(n)
    n1//=10
for i in l:
    cube=i**3
    ams+=cube
if ams==num:
    print(f"{num} is a amstrong number")
else:
    print(f"{num} not a amstrong number")'''

#sum and avg of a list
'''lists=[10,20,30,40]
sum=0
avg=0
for i in lists:
    sum+=i
print("sum of list is:",sum)
avg=sum/len(lists)
print("avereage of list is:",avg)'''

#count even and odd in a list
'''lists=[2,5,7,8,10]
even=0
odd=0
for i in lists:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("odd : ",odd)
print("even : ",even)'''


#reverse a integer
'''num=int(input("Enter a number:"))
rev=[]
while num>0:
    n=num%10
    rev.append(n)
    num//=10
print("reversed integer:",rev)'''

#remove duplicate in a list
lists=[1,2,2,3,4,4,5]
result=[]
for i in lists:
    if i not in result:
            result.append(i)
print("removed duplicate:",result)










































































