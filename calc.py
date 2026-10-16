def square_return(num):
    return num ** 2

def square_print(num):
    print("The square of num is",num ** 2)

def area(base,height):
    '''(number, number) -> number

    Return the are of a triangle with dimensions base and height.

    >>> area(10, 5)
    25.0
    >>> area(2.5, 3)
    3.75
   '''
    
    return base * height / 2

def  convert_to_celsius(fahrenheit):
    '''(number) -> float
    
    Return the number of Celsius degrees equivalent to fahrenheit degrees.
    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0
    '''

    return (fahrenheit -32) * 5 / 9
    
def area(base,height):
    '''(number, number) -> number

    Returns the Area of a triangle with given base and height.

    >>> area(40,10)
    200.0
    >>> area(3.4,7.5)
    12.75
    '''
    return base * height / 2

def perimeter(side1,side2,side3):
    '''(number, number, number) -> number

    Returns the perimeter of a triangle with three sides given.

    >>> perimeter(10,20,30)
    60
    >>> perimeter(12,13,15)
    40
    '''

    return side1 + side2 + side3

def semiperimeter(side1,side2,side3):
    '''(number,number,number) -> float

    Returns the semiperimeter of a triangle with three sides given.
    
    >>> semiperimeter(10,20,30)
    30.0
    >>> semiperimeter(12,13,15)
    20.0
    '''

    return perimeter(side1,side2,side3) / 2

def count_letters(word):
    """ (str) -> int

    Return the number of letters in word.
    >>> count_letters('hello')
    5
    >>> count_letters('bonjour')
    7
    """ 
    return count_vowels + count_consonants
