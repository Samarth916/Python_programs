#1.area perimeter of circle,
r=int(input("Enter the radius "))
c=2*3.14*r
a=3.14*r*r
print("Area is "+str(a))
print("Perimeter is "+str(c))

#2.avg percentage of marks
t=int(input("Enter the total marks "))
s1=int(input("Enter the marks of subject1 "))
s2=int(input("Enter the marks of subject2 "))
s3=int(input("Enter the marks of subject3 "))
s4=int(input("Enter the marks of subject4 "))
s5=int(input("Enter the marks of subject5 "))
avg=(s1+s2+s3+s4+s5)/5
p=((s1+s2+s3+s4+s5)/t)*100
print("The average is "+str(avg))
print("The percentage is "+str(p))

#3.whether its a triangle or not
a=int(input("Enter the sides "))
b=int(input())
c=int(input())
if ((a+b)>c) and ((b+c)>a) and ((a+c)>b):
    print("Triangle is valid ")
    s=(a+b+c)/2
    
    import math
    
    ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("the area is  "+str(ar))
else:
    print("The triangle is invalid")

#4.height in ft,inches to cms
f=int(input("Enter the height in ft "))
i=int(input("Enter the height in inches "))
h=((f*12)+i)*2.54
print("The height is"+str(h))

#5.print individual digits and sum of them
a=int(input("Enter the 4 digits "))
sum=0
for digit in str(a):
    print(digit)
    sum=sum+int(digit)
    
print("The sum is "+str(sum))

#6.salary of camera salesman
sold=int(input("Enter the numbers of cameras sold "))
price=int(input("Enter the price of the cameras "))
salary=25000+(sold*200)
total=sold*price
commission=total*0.12
totalsal=salary+commission
print(commission)
print("The total salary is "+str(totalsal))

#7.character replacing by its next character
a=int(input('Enter the value of a '))
b=int(input('Enter the value of b '))
c=int(input('Enter the value of c '))
d=(b*b-4*a*c)**0.5
x1=(-b-d)/(2*a)
x2=(-b+d)/(2*a)
print('x1 = '+str(x1))
print('x2 = '+str(x2))

#8.print in uppercase along with ascii value
a=input('Enter the string of characters ')
b=a.upper()
for i in str(b):
    print(chr(ord(i))+":"+str(ord(i)))

#9.integers b/w (100-200) whose sum of digits is even
for i in range(100,200):
    sum=0
    for digit in str(i):
        sum=sum+int(digit)
      
    if (sum%2)==0:
        print(i)
                
#10.If entered no is fib or not
i=int(input('Enter the number '))

import math
def Square(x):
    s = int(math.sqrt(x))
    return s*s == x
def Fib(n):
     return Square(5*n*n + 4) or Square(5*n*n - 4)     
if(Fib(i)==True):
    print(i, " is a fibonacci number ")
else:
    print(i, " is not a fibonacci number ")




#11
h= float(input('Enter height of traingle: '))
b= float(input('Enter base of traingle : '))
a=(0.5*b*h)
print('The area of the triangle is' +str(a))

#12
x = int(input('enter the speed in KM: '))
miles = x * 0.621371
print('after converting kms to miles')
print(miles)

#13
a = float(input('enter the value of a: '))
b = float(input('enter the value of b: '))
c = float(input('enter the value of c: '))
d = (b*b) - (4*a*c)
x1 = (-b - (d ** 0.5))/(2*a)
x2 = (-b + (d ** 0.5))/(2*a)
print(x1,x2)

#14
n= float(input('Enter a number: '))
Sqrt = num ** 0.5
print(sqrt)

#15
a = int(input("enter num 1: "))
b = int(input("enter num 2: "))
print(a + b)

#16
print('using temp variable')
x = input('Enter value of x: ')
y = input('Enter value of y: ')
temp = x
x = y
y = temp
print('The value of x after swapping: '+ str(x))
print('The value of y after swapping: '+ str(y))

print('without temp variable')
x = input('Enter value of x: ')
y = input('Enter value of y: ')
x, y = y, x
print("x =", x)
print("y =", y)

print('Using addition and subtraction')
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))
x = x + y
y = x - y
x = x - y
print("x =",x)
print("y =", y)

print('Using multiplication and division')
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))
x = x * y
y = x // y
x = x // y
print("x =",x)
print("y =", y)

print('using XOR method')
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))
x = x ^ y
y = x ^ y
x = x ^ y
print("x =",x)
print("y =", y)

#17
a=int(input('enter a number'))
if a%2==0:
    print('number is even')
else:
    print('number is odd')
print('done')


#18
a=int(input('Enter a number:'))
if a<0:
    print('number is negative')
elif a>0:
    print('number is positive')
else:
    print('number is zero')

#19
a=int(input('Enter a number:'))
if a!=0:
    if a<0:
        print('number is negative')
    if a>0:
        print('number is positive')
else:
    print('number is a zero')


#20
a=int(input('Enter the numbers'))
b=int(input())
c=int(input())
if a>b:
    if c>a:
        print('str(c)+ is greater')
    else:
        print('str(a)+ is greater')
if b>c:
    if a>b:
        print('str(a) is greater')
    else:
        print('str(b)+ is greater')
if a>c:
    if b>a:
        print('str(b) is greater')
    else:
        print('str(a) is greater')

#21
i=1
while i<=100:
    if i%2 != 0:
        print(i)
    i=i+1

#22
for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')

#23
i=0
j=0
for i in range(0,5):

    for j in range(i+1,5):
        print(j,end=' ')
    print()

#24
i=0
j=0
for i in range(0,5):
    for j in range(0,5):
        print('#',end=' ')
    print()

#25
i=0
j=0
for i in range(0,5):
    for j in range(0,i+1):
        print('#',end=' ')
    print()


#csum
lst=[]
n=int(input("enter the no of elements"))
for i in range(0,n):
    el = int(input())
    lst.append(el)
print(lst)
sum=[]
sum.append(lst[0])
for i in range(1,n):
    s=lst[i-1]+lst[i]
    sum.append(s)
print(sum)

#duplicate
lst = []
n=int(input("enter the no of elements :"))
for i in range(0,n):
    el = int(input())
    lst.append(el)
print(lst)
def has_duplicate(lst):
    for i in range(0,n-1):
        s=lst.count(lst[i])
        if(s>1):
            print("True")
            break
has_duplicate(lst)

#midlst
lst = []
n=int(input("enter the no of elements :"))
for i in range(0,n):
    el = int(input( ))
    lst.append(el)
print(lst)
lst.pop(0)
lst.pop(n-2)
print(lst)

#sort
lst = []
n=int(input("enter the no of elements :"))
for i in range(0,n):
    el = int(input())
    lst.append(el)
print(lst)
def sort(lst):
    new=sorted(lst)
    if (new==lst):
        print("True")
    else:
        print("False")
sort(lst)

#nested list sum
def nested_list(t):
    total = 0
    for i in t:
       total = total + sum(i)
    return total

t = [[1,2],[3],[4,5,6]]
res = nested_list(t)
print(res)
