#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("hello  world")
print("regex")


# In[ ]:


print("yash","aman",sep = "--")


# In[ ]:


'''
variable = is a cntainer
python = int,float ,boolean,string, complex,list,tuple,dictionary ,set ,frozenset

numbers ,string ,boolean : are immutable

comment are used for document the texts

'''


# In[ ]:


add = """ my name 
is 
lakhan"""
print(add)


# In[ ]:


'''
stirng formatting
'''


# In[ ]:


age = 88
name = "tushar"
company = "regex"
print("my age is",age,"my name is",name)


# In[ ]:


age = 88
name = "tushar"
company = "regex"
print(f"my {age} is and my {name} is and my company is {company}")


# In[ ]:


# call by object reference is work in python
'''
agar kisi new memory address me changes ho rhe hai == immmutabe
agar same memory me change ho rha hai == mutable'''


# In[ ]:


#immutable
name = "tushar"
print(name,id(name))

name = "goyal"
print(name,id(name))


# In[ ]:


#mutable
name = "tushar"

new = "tushar"
print(name,id(name))
print(new,id(new))


# In[ ]:


#indexing

state = "RAJASTHAN"
state[0]
state[-1]
state[-3]


# In[ ]:


# slicing
#slicing  var[ start : stop : [step=1] ]
#stop is exclusive
state = "RAJASTHAN"
state[5:8]


# In[ ]:


state = "RAJASTHAN"
#state[4:0:-1]
state[0:4:-1]


# In[ ]:


state = "RAJASTHAN"
state[0:6:2]


# In[ ]:


state = "RAJASTHAN"
state[-1:-4:-1]


# In[ ]:


state = "RAJASTHAN"
state[-5:-2:-1]


# In[ ]:


state = "RAJASTHAN"
state[::-1]


# In[ ]:


state = "RAJASTHAN"
state[-1::-1]


# '''
# comment vs docstring
# procedural vs oops
# learn about identifier vs keyword
# c vs python
# learn about namespace
# operators and conditional operator
# 
# session link https://bit.ly/3DzhJYb
# '''
# print(__doc__)

# In[ ]:


''' 
Takes in a number n, returns the square of n
'''
print(__doc__)


# In[ ]:


num_list = []
n = 5
for i in range(n):
    num = int(input("enter the value"))
    num_list.append(num)
    print("output:",num_list)


# In[ ]:


num_list = [int(input("enter a input"))for _ in range(5)]
print(num_list)


# In[ ]:


input_string = input("enter multiple inputs with spaces")
input_list = input_string.split()
numbers = [int(num) for num in input_list]
numbers


# ;n = int(input()).split()

# In[ ]:


num


# In[ ]:


x,y,z = list(map(int, input("Enter multiple values: ").split()))


# In[ ]:


print((x+y+z)/3)


# In[ ]:


n = list(map(str,input("enter the string char").split()))
len(n)


# In[ ]:


maxi = list(map(int,input("enter the int values ").split()))
maxno = max(maxi)
minno = min(maxi)

print(f"the maximum value is {maxno}")
print(f"the minimum value is {minno}")


# In[ ]:


values = list(map(int,input("enter the numbers :").split()))
print(values)
even = values[0: :2]
print(even)
odd =  values[1: :2]
print(odd)
for i in range(len(even)):
    even[i] = even[i]**2
print(f"the square of even index numbers is : {even}") 

for i in range(len(odd)):
    odd[i] = odd[i]**3
print(f"the quabe of odd ined numbes is : {odd}")    


# In[ ]:


a = list(map(int,input("enter the integer value :").split()))
print(a)
prime = []
for i in range(len(a)):
    if(a[i] == 3 or a[i] == 5 or a[i] == 7 or a[i] == 2):
        prime.append(a[i])
    elif(a[i]%2 == 0 or a[i]%3 == 0 or a[i]%5 == 0 or a[i]%7 == 0):
        continue
    else:
        prime.append(a[i])
        
        
        
print(prime)      
            
    
        


# In[ ]:


n = int(input())
list = []
for i in range(n):
    z = input()
    if((z[:1] ) == (z[-1::])):
        list.append(z)
        
    else:
        break
print(list)        
        


# In[ ]:


z = "razr"
print(z[::1])
print(z[-1::-1])


# In[ ]:


g = list(map(str,input("enter the value : ").split()))
ll = []
for i in range(len(g)):
    z = g[i]
    if((z[:1] ) == (z[-1::])):
        ll.append(z)
        
print(ll)        
        
    


# In[ ]:


n = list(map(str,input("enter the integer :").split()))
palindrome = []
for i in range(len(n)):
    p = n[i]
    if(p == p[-1::-1]):
        palindrome.append(p)
        
print(palindrome)        


# In[ ]:


print(12//10)


# In[7]:


n = list(map(int,input("enter the integer value :").split()))
palindrome = []
for i in range(len(n)):
    z = n[i]
    k = 0
    while(z != 0):
        k = (k)*10+z%10
        z = z//10
        #print(z,k)
               
    if(n[i] == k):
        palindrome.append(k)
print(palindrome)    
        


# In[ ]:


g = list(map(str,input("enter the string value :").split()))
ll = []
for i in range(len(g)):
    z = g[i]
    z = z[-1::-1]
    ll.append(z)
        
print(ll)        
        


# In[ ]:


for i in range(1,100,2):
    print(i)


# In[ ]:


for i in range(100):
    print(i)


# In[ ]:


for i in range(1,100,2):
    print(i)


# In[ ]:


for i in range (100,0,-1):
    print(i)


# In[ ]:


a = 'mohit'
len(a)
for i in range(0,len(a),2):
    if(i%2 == 5):
        print(i)

   # else:
    #    print(i)
    # print(a[i])


# In[ ]:


x = 'mohitiu'
t = 0
for i in range(len(x)):
    
    if(x[i]== 'a' or x[i] == 'e'or x[i] == 'i' or x[i] == 'o'or x[i] == 'u'):
        t = t+1
    
print(t)        


# In[ ]:


n = str(input())
k =int(n[0])+int(n[-1])
print(k)


# In[ ]:


n = int(input())

t  = n%10
p = len(str(n))
n = n//


# In[6]:


n = int(input())
t = n
b = 0
while(n>0):
    b = n%10
    n = n//10
t = t%10
print(t+b)


# In[2]:


#nesting loop
# printing star pattern

for i in range (0,5):
    for j in range(0,5):
        print("*",end = " ")
        
    print("\n")    


# In[3]:


for i in range (0,5):
    for j in range(0,i):
        print("*",end = " ")
        
    print("\n")    


# In[14]:


for i in range (5,0,-1):
    for j in range(0,i):
        print("*",end = " ")
        
        
        
    print("\n")    


# In[21]:


for i in range (0,5):
   
    for j in range(0,5-i):
        print(end = " ")
    for k in range(0,i+1):
        print("*",end = " ")
   
        
        
       

        
        
    print("\n")    


# In[30]:


n = 5
for i in range(0,n):
    for j in range(0,n):
        if j == 0 or j == n-1 or i == 0 or i == n-1:
            print("*",end = "")
            
        else:
            print(end = " ")
            
    print("\n")       
            
            
            


# In[58]:


for i in range(0,5):
    for j in range(0,i):
        print(" ",end = " ")
    for k in range(0,1):
        print("*",end= " ")
    for l in range(0,9-2*i):
        print(" ",end=" ")
    for m in range(0,1):
        print("*",end = " ")
              
    print("\n")          


# In[56]:


n = int(input())
for i in range(0,n):
    for j in range(0,n):
        if(i == 0 or i == n-1 or j == n//2):
            print("*",end = " ")
        else:
            print(" ",end =" ")
        
            
            
        
    print("\n")    


# In[ ]:




