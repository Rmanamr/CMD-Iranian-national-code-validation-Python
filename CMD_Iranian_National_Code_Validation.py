"""Python CMD program for validating Iranian national codes.
using Python version 3.11.4
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""

def main():
     """
     main function for interacting with the user
     """
     while(True):
     # while loop to keep the program running

        print("Please enter the Iranian national code that you want to be validated :")
        input_Number = int(input())
        # reading the next integer number

        result = Iranian_National_Code_Validator(input_Number)
        # passing the input_Number to the Iranian_National_Code_Validator function to validate it
        # and storing the result in result variable

        print("The" ,input_Number)
        if(result):
            print("is a valid Iranian national code.")
        else:
            print("is not a valid Iranian national code.")
        print("**************************************************************************")


def Iranian_National_Code_Digits_lenght_Checker(number):
    """
    function for checking the number of Iranian national code digits.
    @param number: an Iranian national code
    @type number: integer
    @return: Iranian_National_Code
    @rtype: integer, boolean
    @examples: 
     >>> Iranian_National_Code_Digits_lenght_Checker(890729689)
         0890729689
     >>> Iranian_National_Code_Digits+lenght_Checker(19863837)
         0019863837  
     >>> Iranian_National_Code_Digits_lenght_Checker(3005059)
         False
     >>> Iranian_National_Code_Digits_lenght_Checker(8543823984925178)
         False
    """ 
    Iranian_National_Code = str(number)
    lenght = len(Iranian_National_Code)

    if lenght < 8:
        return False
    elif lenght > 10:
        return False
    elif lenght == 9:
        Iranian_National_Code = "0" + Iranian_National_Code
    elif lenght == 8:
        Iranian_National_Code = "00" + Iranian_National_Code
    # people with 0 or 00 at the begining of their Iranian national code may not insert the 0s, or we might have a problem accepting it
    # so we should make sure that the Iranian national code has 10 digits(including the first 0 or 00) or it is not a valid code.

    return int(Iranian_National_Code)
    

def integer_To_Digits_Splitter(number):
    """
    function for splitting the digits of integer numbers.
    @param number: a number
    @type number: integer
    @return: array_Of_Digits
    @rtype: array of integers
    @examples: 
     >>> integer_To_Digits_Splitter(0)
         [0]
     >>> integer_To_Digits_Splitter(123)
         [3, 2, 1]   
    """
    string_Number = (str(number))
    # converting number to string to be able to use len() function

    number_Of_Digits = len(string_Number)
    # usung len() function to calculate number of digits

    array_Of_Digits = []
    # initializing an empty array to store digits in

    for i in range(number_Of_Digits):
        a = number//10
        reminder = number - a*10
        number = a
        array_Of_Digits.append(reminder)
        # appending the last digit to array_Of_Digits

    return array_Of_Digits


def Iranian_National_Code_Validator(number):
    """
    function for validating the Iranian national codes.
    @param number: an Iranian national code
    @type number: integer
    @return: boolean
    @rtype: boolean
    @examples: 
     >>> Iranian_National_Code_Validator(1272032205)
         True
     >>> Iranian_National_Code_Validator(19863837)
         True 
    >>> Iranian_National_Code_Validator(234620) 
         False
    >>> Iranian_National_Code_Validator(650469345749220) 
         False
    """
    if Iranian_National_Code_Digits_lenght_Checker(number) == False:
        return False
    # if after adding 0 or 00 to number, it is less than 10 digist, so it's an invalid Iranian national code.
    
    result = integer_To_Digits_Splitter(number)
    sum = 0
    for i in range(1, len(result)):
        sum += (i+1) * result[i]
    # we mulitple each digit by it's value except for the most right digit.
    # scince array indexes start with 0, we should add 1 to each index,

    remind = sum%11

    if remind>=2:
        remind = 11 - remind

    if remind == result[0]:
        return True
    else:
        return False
    # algorithm for checking the control digit of Iranian national code.
    

if __name__ == '__main__':
    main()
    # run the main function after executing this file