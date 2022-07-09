#!/usr/bin/env python
# coding: utf-8

# Section 1

# In[1]:


list_a  = [1,2,3,4,5]


# In[2]:


# Print the last 2 elements of the list dont use explicit indexing : [4,5]
print(list_a[-2:])
print(list_a[3:])


# In[3]:


# Print [1,3,5] from list_a
print(list_a[0],list_a[2],list_a[4])


# In[4]:


#insert number 6 at the end of the list and print the new list
list_a.append(6)
print(list_a)


# Section 2

# In[5]:


# Create a phone book in python with name as the key and phone number as the value . Which data structure would you use ?
def find_phonenumber(phonebook, name):
    for n, p in phonebook:
        if n == name:
            return p
    return None

phonebook = [
    ("Shiva Prasad", "944-988-8661"),
    ("Bragav Praneeth", "900-000-0000"),
]


# In[6]:


# of the phone book created at the top , print all the names. in a new line print all the values i.e phone numbers
print(phonebook)


# In[7]:


# Update the phonebook by details of a new user : John Doe , 898963656
phonebook.update("John Deo","898963656")


# Misc.

# In[8]:


# print todays date in 'dd-mm-yyyy' format ,make the nessesary imports if required
import datetime
mylist = []
today = datetime.date.today()
mylist.append(today)
print(mylist)


# Section 3

# Write a program that prints the numbers from 1 to 25 and for multiples of ‘3’ print "Mickey" instead of the number and for the multiples of ‘5’ print "Mouse". And if it is a multiple of both 3 and 5 then print "Mickey Mouse".<br>
# Eg. <br>
# 1,2,Mickey,4,Mouse ..... 

# In[9]:


#generate a list of numbers from 1 to 25

#here
for i in range(1,26):
    if i%3==0:
        print("Mickey")
    elif i%5==0:
        print("Mouse")
    elif i%3==0 & i%5==0:
        print("Mickey Mouse")
    else:
        print(i)

# Define the logic for the problem statement and print output : Mickey , Mouse or Mickey Mouse accordingly
#here


# Section 4

# Prime number is a number that is divisible only by itself and 1.<br>
# Define a function "isPrime"  , which takes a user provided integer as input and returns true if the number is prime , else returns false. if an invalid input is provided print("Invalid input passed"). Keep in mind any special/edge cases.

# In[10]:


# Define isPrime function

# To take input from the user and save it in variable called num

#pass num to isPrime function and get result

num = int(input("Enter a number: "))

flag = False

# prime numbers are greater than 1
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")


# Pandas

# In[11]:


import pandas as pd
import numpy as np

df_dict = {'CUSTID': ['98981', '897892','32323','98900','98981'],
           'CamapignID': ['C1', 'C2','C3','C1', 'C1'],
           'Units Puchased':[2,1,7,4,2]}
campaign_df = pd.DataFrame(data=df_dict)
campaign_df


# In[12]:


# Calculate the total Units purchased per campaign

total_units=campaign_df.groupby('CamapignID')['Units Puchased'].sum()
total_units


# In[13]:


# Calculate the total Units purchased , excluding those Units sold from campaign 2 (C2)
total_units[0],total_units[2]


# In[14]:


# return / find the custid with the highest units purcahsed across all campaigns aggregations not required.
campaign_df.max()


# Bucket the customers into tiers based on their Units purchased, aggregations not required .<br>
# A1 : if purchase is more than 6 Units<br>
# A2: if the purchase is between 3-5 Units , endpoints included.<br>
# Else,A3

# In[15]:


#code here
campaign_df['Buckets'] = campaign_df['Units Puchased'].apply(lambda x: 'A1' if x <= 6 else 'A3')
campaign_df.head()


# In[17]:


campaign_df.loc[(campaign_df['Units Puchased'] <= 6) , 'Buckets'] = 'A1' 
campaign_df.head()


# Section 5

# Create a Class Car , which accepts parameters like transmisson (manual/auto) , and make year (eg.2019). It should also contain a method 'get_make_yr' which'll return the make year of the car object. <br>
# Intantiate an object of class Car and print the make year using get_make_yr.
# 
# 

# In[18]:


#code here
class car:
    def __init__(self, transmisson, make_year):
        self.transmisson = 'manual'
        self.year = make_year
        
        
car = car('manual', 2022)
print(car.transmisson, car.year)


# Section 6

# Regex:
# 
# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
# 

# In[19]:


#Code here
import re
def is_allowed_specific_char(string):
    char = re.compile(r'[^a-zA-Z0-9]')
    string = char.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))


# Write a Python program that matches a word at the beginning of a string.
# 

# In[20]:


#code here
import re
def text_match(text):
        patterns = '^\w+'
        if re.search(patterns,  text):
                return 'Not match'
        else:
                return('match')

print(text_match("shiva prasad"))
print(text_match("Adithya"))

