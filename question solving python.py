#practice qoestion 1
num1=int(input("num1:"))
num2=int(input("num2:"))
sum=num1 + num2
print(sum)
#question2
length=int(input("length of side:")) 
print("area of square",length*length,)
 # question 3
a=float(input("enter your first no.:"))
b=float(input("enter your second no.:"))
print("average",(a+b)/2,)
#question 4
a=int(input("a:"))
b=int(input("b:"))
# ye bhi kar sakte ya: print("True") if a==b or a>b else print("False")
print(a>=b)
#question5
name=input("name:")
print(len(name))

#question 6
str= "Value of rupees is very less in compare to dollar$"
print(str.count("$"))
#question7
num=int(input("num:"))
print("even") if num%2==0 else print("odd")
#question 8
num3=int(input("num3:"))
num4=int(input("num4:"))
num5=int(input("num5:"))
if(num3>num4 and num3>num5):
    print("greatest no. is",num3)
if(num4>num3 and num4>num5):
    print("greatest no is",num4,) 
else:
    print("greatest no. is",num5,)  

    #question 9
x=int(input("x:"))
print ("yes, it is divisible by 7") if x%7==0 else print("no, the no. is not divisible by 7")

#question 10

movie1=input("movie1:")
movie2=input("movie2:")
movie3=input("movie3:")
list=[movie1,movie2,movie3]
print(list)

#question 11

list2=[1,2,3,2,1]
list3=list2.copy()
list3.reverse()

print("yes,it is a palindrome") if list3==list2 else print("no,it is not a palindrome")
 #question12
tup=("C","D","A","A","B","B","A")
print(tup.count("A"))

#QUESTION 13
list=["C","D","A","A","B","B","A"]
list.sort()
print(list)




