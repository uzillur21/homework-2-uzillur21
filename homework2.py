# PPHA 30535
# Spring 2022
# Homework 2

# UMAMA ZILLUR
# UZILLUR21

# Due date: Sunday April 17th before midnight
# Write your answers in the space between the questions, and commit/push only 
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put 
# thought into your work.

#############

# Question 1: Write a function that takes two numbers as arguments, then
# sums them together.  If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small".  Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

# create a list of tuples 
start_list = [(10, 0), (100, 4), (0, 0), (-15, -100), (5, 4)]


# function which takes two integers and checks whether their sum is greater than, 
# equal to or smaller than 10
def sum_size (a, b):
    answer = a+b
    if answer > 10:
        return "big"
    elif answer == 10: 
       return "just right"
    elif answer < 10:
       return "small"

# create an empty list 
end_list = []
# loop through each tuple from our list and apply function and store results 
# in a new list
for i, tuple in enumerate(start_list):
    a = tuple[0]
    b = tuple[1]
    end_list.append(sum_size(a,b))
print(end_list)
    
# https://www.guru99.com/python-enumerate-function.html            

# Question 2: The following code is fully-functional, but uses a global
# variable and a local variable.  Re-write it to work the same, but using an
# argument and a local variable.  Use no more than two lines of comments to
# explain why this new way is preferable to the old way.


def my_func(a=10):
    b = 30
    return a + b
x = my_func()
print(x)

# Use of global variables makes our function unreliable. Global variable changes can  
# make errors hard to detect. It will not break our function but will give different outputs.  

# Question 3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*).  It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else warn the user 
# and exit.  Your function should also have a keyword argument named 
# "special_chars" that defaults to True.  If the function is called with the 
# keyword argument set to False instead, then the random values chosen should
# not include special characters.  Create a second similar keyword argument 
# for numbers. Use one of the two libraries below.
#import random
#from numpy import random

import random

# random password generator from upper-case and lower-case letters, numbers, 
# and special characters of length 8 to 16
def set_password(numbers = True, special_chars = True, length=0):
   
    # create variables to store letters, numbers and special characters
    num = "1234567890"
    chars_lower = "abcdefghijklmnopqrstuvwxyz"
    chars_upper = "ABCDEFGHIJKLMNOQRSTUVWXYZ"
    special_chars_1 = "#$%^&*!@"
    

    # if user inputs length between 8 and 17, password is generated
    if length in range (8,17):
        # check user input and include or remove special characters and numbers 
        # from sample of characters generator will choose from 
        if special_chars == True and numbers == True:
            all = chars_lower+chars_upper+num+special_chars_1
        elif special_chars == False and  numbers == True:
            all = chars_lower+chars_upper+num
        elif special_chars == True and  numbers == False:
            all = chars_lower+chars_upper+special_chars_1
        elif special_chars == False and  numbers == False:
            all = chars_lower+chars_upper
        # random sample of characters of length chosen by user
        temp = random.sample(all,length)
        # remove space and join all characters
        password = "".join(temp)
        print (password)
        exit
    # if user input is not within range, give warning and exit 
    elif length < 8 or length > 16:
        length = input("Warning: Password length not valid") 
        #print("Warning: Password length not valid")
        exit
      
# generate a random password of 10 characters with numbers but no special characters       
set_password(numbers = True, special_chars=False, length = 10)

# https://medium.com/analytics-vidhya/create-a-random-password-generator-using-python-2fea485e9da9
# https://www.makeuseof.com/how-to-create-random-password-in-python/
# https://docs.python.org/3/library/random.html
  
# Question 4: Create a class that requires four arguments when an instance
# is created: one for the person's name, one for which COVID vaccine they
# have had, one for how many doses they've had, and one for whether they've
# ever had COVID.  Then create instances for four people:
#
# Aaron, Moderna, 1, False
# Ashu, Pfizer, 2, False
# Alison, none, 0, True
# Asma, Pfizer, 1, True
#
# Write two methods for this class, and one function:
# The first method named "get_record", which prints out a one-sentence summary
# of a specified person's records (e.g. Ashu has two doses of Phizer and...)
#
# The second method named "same_shot", which takes as an argument another person's
# record instance, and then prints whether or not the two people have the
# same kind of vaccine or not.
#
# A function named "all_data", which takes any number of these instances and 
# returns a simple list of all of their data 
# (e.g. [name, vaccine, doses, covid], [...])

 
class VaccineCheck():
    
    
    # takes four arguments on patient name, vaccine and covid info
    def __init__(self, name, vaccine, dose, covid):
        self.name = name 
        self.vaccine = vaccine 
        self.dose = dose 
        self.covid = covid
        # print all arguments 
        self.print = self.name +','+ self.vaccine +','+ self.dose + ',' + self.covid
      
     
    # create summary on individual records    
    def get_record(self):
        covidmsg = str() 
        # check to see if individual had covid and assign appropriate message
        if self.covid == "True" :
            covidmsg = ("has had covid")
        elif self.covid == "False":
            covidmsg = ("has not had covid")
        # take user input values from class object to construct summary
        print(f'{self.name} has {self.dose} dose(s) of {self.vaccine} and ' + covidmsg +'.')
    
    # check if individual has the same vaccine as another person   
    def same_shot(self, other):
        if self.vaccine == other.vaccine :
            print("They have both taken the same vaccine.")
        elif self.vaccine != other.vaccine:
            print("They have not taken the same vaccine.")
    
    # takes multiple objects and create a list of all their data 
    def all_data(*args):
        # create an empty list 
        data_list = []
        person = args
        # loop through the number of objects input by user
        for i in range(len(args)):
            temp = [person[i].name, person[i].vaccine, person[i].dose, person[i].covid]
            # add to our list
            data_list.append(temp) 
        return data_list
        exit

Aaron = VaccineCheck("Aaron", "Moderna", "1", "False")
Aaron.print
Asma = VaccineCheck("Asma", "Pfizer", "1", "True")
Ashu = VaccineCheck("Ashu", "Pfizer", "2", "False")
Alison = VaccineCheck("Alison", "none", "0", "True")    

# use get record method to get Aaron's record
Aaron.get_record()

# use same shot method to check if Aaron and Asma had same vaccine
Aaron.same_shot(Asma)

# use all data function to get data on three individuals 
y = all_data(Aaron, Asma, Alison)  
print(y)  

# use all data function to get data on all four individuals 
y = all_data(Aaron, Asma, Alison, Ashu)  
print(y)  

# https://www.bogotobogo.com/python/python_classes_instances.php
# https://docs.python.org/3/tutorial/classes.html
# https://www.geeksforgeeks.org/args-kwargs-python/#:~:text=The%20special%20syntax%20*args%20in,used%20with%20the%20word%20args.


 