# from django.test import TestCase

# Create your tests here.


names= ['Aisha','Sanja','wendy','ivy','Fei','Lucy','cynthia', 'Sanja']
othernames= ('Teddy','Sam','Isaac','Troy','Fetty') #tuple
thislist = [100, 50, 65, 82, 23]  #list
teams= {'liv','city','psg','bar','manu','che','ars'}  #sets

import json
dict = {
    'months': {
    'jan' : 'JANUARY',
    'feb' : 'FEBRUARY',
    'mar' : 'MARCH',
    'apr' : 'APRIL',
    'jun' : 'JUNE',
    },
    'days' : {
    'mon' : 'MONDAY',
    'tue' : 'TUESDAY',
    'wed' : 'WEDNESDAY',
    'thu' : 'THURSDAY',
    'fri' : 'FRIDAY',
    }
}

# dict.update(name = 'Sam')
# dict['jun']= 'JUNUARY'
# dict.pop('mar')
# print(dict.values())
# print(dict.items())


# a=66
# sum=1
# while sum<1000:
#     print(sum)
#     # if sum == 793:
#     #     break
#     sum+=a
# else:
#     print('THE END')





# def ad(k):
#     while k>0: 
#         sum=k+ ad(k-1)  
#         print(sum)
#     else:
#         sum=0
#     return sum

# ad(6)



# def ad(sum,k):
#     while k<7:  
#         sum+=k
#         print(sum)     
#         k+=1

# ad(sum=0,k=1)
    
# m= lambda n : n+6
# print(m(5))

class Animal:
    def __init__(self,type,weight):
        self.type= type
        self.weight= weight

    def pn(self):
        print(self.type,self.weight)

class Chicken(Animal):
    def __init__(self, type, weight):
        super().__init__(type, weight)
        self.name= 'Sam'
        
    def __str__(self):
        return f'My Chicken is a {self.type} and has {self.weight} and name is {self.name}'

class Cow(Animal):
    def __init__(self, type, weight, name):
        Animal.__init__(self, type, weight)
        self.name = name
        
    def __str__(self):
        return f'My Chicken is a {self.type} and has {self.weight} and owmed by {self.name}'


class Cat(Animal):
    def __init__(self,name,color):
        self.name= name
        self.color= color

    def __str__(self):
        return f"My cat's name is {self.name} and is color {self.color} with {self.weight}"

class Dog(Animal):
    def __init__(self,age,no):
        self.age= age
        self.no= no

    def __str__(self):
        return f'My dog is {self.age} years old and has {self.no} puppies  with {self.weight}'

# Animal('domestic','24kg')
# # x= Cat('Sasha','red', '32kg')
# # y=Dog('44','3')
# y= Cow('domestic', '33kg', 'Milky')
# z= Chicken('domestic', '33kg')
# print(y,z)

class Nambari:
    def __iter__(self):
        self.a= 1
        return self
    
    def __next__(self):
        x= self.a
        self.a+=1
        return x
    
myc= Nambari()
itt= iter(myc)


import datetime
x= datetime.datetime.now()



import json
m= {
"employees":[
    {"firstName":"John", "lastName":"Doe"},
    {"firstName":"Anna", "lastName":"Smith"},
    {"firstName":"Peter", "lastName":"Jones"}
]
}

n= json.dumps(m,indent=4)
#json.loads


# import re
# x= 'The rain has come'
# y= re.search('ai',x)
# print(y)
# if x:
#     print('YES')
# else:
#     print('NAHs')

import os


files= open('doci/fetty.txt','w')  # write and r is for read
files.write('WE mzee mbona wafanya ushoga huo wako')
files.close()
# os.remove('f.txt')   #delete file
files= open('doci/fetty.txt','r')


# import sys
# import matplotlib
# matplotlib.use('Agg')


# from matplotlib import pyplot as plt
# import numpy as np

# xpoints= np.array([0,6])
# ypoints= np.array([0,100])

# plt.plot(xpoints,ypoints)
# plt.show()
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush



