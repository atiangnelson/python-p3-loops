#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i=10
    while i>0:
        print(i)
        i -= 1
        print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    return[integer**2 for integer in int_list]
    


# def fizzbuzz_printer():
#     # code goes here!
#     #x = 1
#     #while x<=100:
#     for x in range (1,101):
#         print(fizzbuzz(x))
#        # x += 1
        
    
def fizzbuzz():
    # code goes here!
    num =1
    while num <= 100:
        if num % 3 == 0 and num % 5 == 0:
            print ("FizzBuzz")
        elif num % 3 == 0:
            print ("Fizz")
        elif num % 5 == 0:
            print ("Buzz")
        else:
            print (num)
        num += 1
  
         
