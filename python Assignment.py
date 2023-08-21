#!/usr/bin/env python
# coding: utf-8

# In[ ]:


break = 5
# break is a predefined variable keyword we can not use as a new variable


# In[ ]:


birth_year = 2001
current_year = 2023
age = current_year - birth_year
print(f"me current age is {age}")


# In[ ]:


first_name = "vikramaditya "
middle_name = "singh "
last_name = "naruka"
print(first_name+middle_name+last_name)
print(f"{first_name}{middle_name}{last_name}")


# In[ ]:


name_nation 1record record1 record_one record-one record^one continue


# In[ ]:


_nation = 3
print(_nation)


# In[ ]:


1record = 5


# In[ ]:


record-one = 4


# In[ ]:


record^one = 5


# In[ ]:


record_one = 7


# In[ ]:


# You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.

l,h = map(float,input("enter the integer value").split())
area = l*h
print(f"the area of football groud is {area}" )


# In[ ]:


'''
You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. 
Find out using python, how many dollars is the shopkeeper going to give you back?

'''
chips_packet,dollar_per_chips,total_dollar= map(float,input().split())
remain_money = total_dollar - (chips_packet*dollar_per_chips)
print(f"the shopkeeper will you give the you back {remain_money} dollar")


# In[ ]:


'''
You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
Calculate and print the cost using python

'''
square_length ,per_square_feet_price = map(float,input().split())
area = square_length**2
total_cost = area*per_square_feet_price
print(f"the total cost of bathroom tiles is {total_cost}")


# In[ ]:


#Print binary representation of number 17

n = int(input())
binary = ''
while (n>0):
    
    if(n%2 == 0):
        binary += '0'
        n = n//2
    elif(n%2 == 1):
        n = n//2
        binary += '1'
print(binary)        


# In[ ]:


#Print binary representation of number 17

n = int(input())
print("the binary number is ",format(n,'b'))


# In[ ]:


'''
Create 3 variables to store street, city and country, now create address variable to store entire address. 
Use two ways of creating this variable, one using + operator and the other using f-string.
Now Print the address in such a way that the street, city and country prints in a separate line
'''

street ,city,countary  = map(str,input().split())
address =(street )+(city ) +(countary )
print(address)
print(f"the address is \n{street}\n{city}\n{countary}")


# In[ ]:


'''
Create a variable to store the string "Earth revolves around the sun"
Print "revolves" using slice operator
Print "sun" using negative index
'''
string = "Earth revolves around the sun"
st = string.split()
len(st)
print(st[1] , st[-1])


# In[ ]:


'''
Create two variables to store how many fruits and vegetables you eat in a day.
Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
Use python f string for this.

'''
x = 3
y = 1
print(f"I eat {x} veggies and {y} fruits daily")


# In[ ]:


'''
I have a string variable called s='maine 200 banana khaye'.
This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.
'''
s = 'maine 200 banana khaye'
s.replace('200','10')


# LIST
# 

# In[ ]:


'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,
'''
list = [2200,2350,2600,2130,2190]
print(len(list))
# In Feb, how many dollars you spent extra compare to January?
extra_feb = list[1]-list[0]
print(extra_feb)

# Find out your total expense in first quarter (first three months) of the year.
total_qtr_expense = list[0]+list[1]+list[2]
print(total_qtr_expense)

# Find out if you spent exactly 2000 dollars in any month
for i in range(len(list)):
    if(list[i] == 2000):
        print(f"{i} = {list[i]}")


# In[ ]:


'''
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

'''

heros = ['spider man','thor','hulk','iron man','caption america']
len(heros)
heros.append('black panther')
heros.pop()
heros.insert(3,'black panther')
heros[1:3] = ["doctor_strange"]
heros.sort()
print(heros)


# # IF CONDITON
# 

# In[ ]:


'''
Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
1) Write a program that asks user to enter a city name and it should tell which country the city belongs to

2) Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
For example if I enter mumbai and chennai, it will print "Both cities are in India" 
but if I enter mumbai and dhaka it should print "They don't belong to same country"
'''
# 1)
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city_name = input("enter a city name  :  ")
if(city_name == "mumbai" or city_name == "banglore" or city_name == "chennai" or city_name == "delhi"):
    print(f"this {city_name} city belongs in INDIA country")
          
elif(city_name == "lahore" or city_name == "karachi" or city_name == "islamabad"):
          print(f"this {city_name} city belongs in PAKISTAN country")
                
elif(city_name == "dhaka" or city_name =="khulna" or city_name =="rangpur"):
    print(f"this {city_name} city belongs in BANGLADESH country")
    
    
 #                                     OR

if city_name in india:
    print(f" this {city_name} is belongs in INDIA country")
elif city_name in pakistan:
     print(f" this {city_name} is belongs in PAKISTAN country")
elif city_name in bangladesh:
     print(f" this {city_name} is belongs in BANGLADESH country")
    
    


# In[ ]:


'''
2) Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
For example if I enter mumbai and chennai, it will print "Both cities are in India" 
but if I enter mumbai and dhaka it should print "They don't belong to same country"
'''
city1 ,city2 = map(str,input("enter the city names : ").split())

if city1 in india and city2 in india:
    print(f" {city1} and {city2} both are belongs cities in INDIA")
elif city1 in pakistan and city2 in pakistan:
    print(f" {city1} and {city2} both are belongs cities in PAKISTAN")
elif city1 in bangladesh and city2 in bangladesh:
    print(f" {city1} and {city2} both are belongs cities in BANGLADESH")
    
else:
    print("they don't belong same country")
    
    


# In[ ]:


'''
Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
Ask user to enter his fasting sugar level
If it is below 80 to 100 range then print that sugar is low
If it is above 100 then print that it is high otherwise print that it is normal
'''
n = int(input("enter your fasting sugar level : "))
if(80<=n<=100):
    print("your sugar level is NORMAL ")
    
elif(n>100):
    print("your sugar level is HIGH")
else:
    print("the sugar level is LOW")


# In[ ]:





# In[ ]:





# # FOR LOOP
# 

# In[ ]:


'''
After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads
'''

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
t = 0
k = 0
for i in range(len(result)):
    if(result[i] == "heads"):
        t += 1
    else:
        k += 1
print("in the result the heads are occur times is",t)  
print("int the result the tells are occur times is",k)


# In[ ]:


#Print square of all numbers between 1 to 10 except even numbers
for i in range (0,11):
    if(i%2 != 0):
        i = i**2
        print(i)


# In[ ]:


'''
Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
If expense is not found then it should print that as well.
'''
n = int(input())
expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["january","fabruary","march","april","may"]
month = 0
    
for i in range(len(expense_list)):
    if(n == expense_list[i]):
        month = i
        break
        
if (n == expense_list[i]):
    print(f"you spent {n} money in {month_list[month]}")
else:
    print("expense is not found ")


#                                   OR

month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]

expense = int(input("Enter an expense amount: "))

if expense in expense_list:
    month = expense_list.index(expense)
    print(f'You spent {expense} in {month_list[month]}.')
else:
    print(f'You didn\'t spend {expense} in any month.')


# In[ ]:


'''
Lets say you are running a 5 km race. Write a program that,

Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message

'''
n = int(input())
for i in range(n,0,-1):
    if(i>0):
        print("are you tired..?")
        t = input()
        if(t == "yes"):
            print("you didn't finish the race")
            break
        else:
            continue
            
    
    
print("congratulation ! you finish the race")


# In[ ]:


'''
Write a program that prints following shape

*
**
***
****
*****

'''


n = int(input())
for i in range(0,n):
    for j in range(0,i):
        print("*",end=" ")
    
    print("\n")    


# In[ ]:


n = int(input())
for i in range(5,0,-1):
    for j in range(0,i):
        print("*",end = " ")
        
    print("\n")    


# # FUNCTION
# 

# In[ ]:


'''
Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.
Equation of an area of a triangle is,
area = (1/2)*base*height
'''
base,height = map(int,input().split())

def area(base,height):
    areas = (1/2)*base*height
    return areas

area(base,height)
    


# In[ ]:


'''
Modify above function to take third parameter shape type. 
It can be either "triangle" or "rectangle". Based on shape type it will calculate area.
Equation of rectangle's area is,rectangle area=length*width

'''
shape = input()
width,length = map(int,input().split())

def area(width,length,shape):
    if(shape == "rectangle"):
        areas = width*length
        return  areas
    elif(shape == "triangle"):
        areas = (1/2)*width*length
        return areas
    else:
        return "the shape is neither the triangle or neither rectangle shape" 
area(width,length,shape)


# In[ ]:


'''
Write a function called print_pattern that takes integer number as an argument
and prints following pattern if input number is 3,
if input is 4 then it should print
*
**
***


if input is 4 then it should print

*
**
***
****
'''

n = int(input())
def print_pattern(n):
    for i in range(0,n+1):
        for j in range(0,i):
            print("*",end = " ")
        print("\n")    
print_pattern(n)        


# # DICT and TUPLES

# In[ ]:


'''
We have following information on countries and their population (population is in crores),

Country Population
China    143
India    136
USA      32
Pakistan 21

1) Using above create a dictionary of countries and its population
2) Write a program that asks user for three type of inputs,
   a) print: if user enter print then it should print all countries with their population in this format,
     china==>143
     india==>136
     usa==>32
     pakistan==>21

b) add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then
it should print that it exist and do nothing. If it doesn't then it asks for population and add 
that new country/population in our dictionary and print it

c) remove: when user inputs remove it should ask for a country to remove. 
If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). 
Else print that country doesn't exist!

d) query: on this again ask user for which country he or she wants to query.
When user inputs that country it will print population of that country.
'''

country = {"china":143 ,"india":136 ,"usa":32 ,"pakistan":21}
n = int(input("in this dictonary :1 print 2 add 3 remove 4 query "))

if(n == 1):
    for i in country:
        print(f"{i} ==> {country[i]}")

elif(n == 2):
    t = input("give the country name ,you want to insert in dictionary : ")
    if t not in country :
        p = int(input("country population : "))
        country[t] = p
        
    else:
        print("the country is already exist")
elif(n == 3):
    de = input("which country you want to remove in dictionary : ")
    if de in country:
        country.pop(de)
    else:
        print("country doesn't exists")
        
elif(n == 4):
    choice = input("which country you want to query : ")
    print(country[choice])
    
country    


# In[ ]:


'''
You are given following list of stocks and their prices in last 3 days,

Stock   Prices
info    [600,630,620]
ril     [1430,1490,1567]
mtl     [234,180,160]

Write a program that asks user for operation. Value of operations could be,
print: When user enters print it should print following,

info ==> [600, 630, 620] ==> avg:  616.67
ril ==> [1430, 1490, 1567] ==> avg:  1495.67
mtl ==> [234, 180, 160] ==> avg:  191.33

add: When user enters 'add', it asks for stock ticker and price.
If stock already exist in your list (like info, ril etc) then it will append the price to the list. 
Otherwise it will create new entry in your dictionary. 
For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.
'''

stock  = { "info":[600,630,620] , "ril":[1430,1490,1567], "mtl":[234,180,160] }
n = input("1 print , 2 add : ")
if(n == "print"):
    for i in stock:
        k = 0
        for j in stock[i]:
            k = k+j
        t = k//len(stock)
        # print(t)
        print(f"{i} ==> {stock[i]} ==> avg: {t}") 
       #stock["info"]
elif(n == "add"):
    j = input("enter the stock name you want to insert in dictionary :  ")
    value = list(map(int,input( ).split())) 
    stock[j] = value
stock    


# In[ ]:


'''
Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area,
circumference and diameter. You should get these values in your main program by calling circle_calc function 
and then print them .
'''
r = int(input())
def circle_calc(r):
    area = (22/7)*(r**2)
    circumference = 2*(22/7)*r
    diameter = 2*r
    return "the area is :",area ," the area of circumference is : ",circumference, " and the diameter is : ",diameter
circle_calc(r)




# In[ ]:


import math

def circle_calc(radius):
    area=math.pi*(radius**2)
    circumference=2*math.pi*radius
    diameter=2*radius
    return area, circumference,diameter

if __name__=="__main__":
    r=input("Enter a radius:")
    r=float(r)
    area, c, d = circle_calc(r)
    print(f"area {area}, circumference {c}, diameter {d}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




