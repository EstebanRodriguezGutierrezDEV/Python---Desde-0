#Create a function that takes an integer as an argument and returns
# "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if(number % 2 == 0):
        return "Even"
    else:
        return "Odd"


even_or_odd(1)
even_or_odd(24)
even_or_odd(111)
