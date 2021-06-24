#----------------------------------------------------------------
# Code Review:      fizz_buzz
# Last Release:     24.06.2021
# Author:           Massimo Brozzi (mbrozzi@gmail.com)
#----------------------------------------------------------------

#----------------------------------------------------------------
# system and standard python imports
#----------------------------------------------------------------

import sys

#----------------------------------------------------------------
# Function:         fizz_buzz
# Description:      Function implementing the FizzBuzz algorithm
# Input parameters: [integer] num => integer number to evaluate 
# Output:           [string] "FizzBuzz" => number is multiple of 3 and 5
#                   [string] "Fizz" => number is multiple of 3 but not of 5
#                   [string] "FizzBuzz" => number is multiple of 5 but not of 3
#                   [integer] The number passed as input otherwise
# Last Release:     24.06.2021
# Author:           Massimo Brozzi (mbrozzi@gmail.com)
#----------------------------------------------------------------

def fizz_buzz(
    num=None,  # integer number to evaluate 
):     
    result = "Error in parameter passed to function"

    if num is not None:
        # Initializes result to number passed as parameter
        result = num
        
        # Tests if both 3 and 5 conditions are met

        check_3 = not num % 3
        check_5 = not num % 5
        
        if check_3 and check_5:
            result = 'FizzBuzz'

        # Tests if 3 condition is met
        elif check_3:
            result = 'Fizz'

        # Tests if 5 condition is met
        elif check_5:
            result = 'Buzz'

    return result


#----------------------------------------------------------------
# Function:         main
# Description:      This is the first function call when running the program
# Input parameters: None
# Output:           None
# Last Release:     24.06.2021
# Author:           Massimo Brozzi (mbrozzi@gmail.com)
#----------------------------------------------------------------

if __name__ == '__main__':
    # Extracts the list of numbers from parameters passed on the command line
    numbers = sys.argv[1:]

    # If list as element, evaluates the fizz_buzz on all of them

    if numbers:
        for num in numbers:
            # Verify that parameter is valid
            if num and num.isdigit():
                n = int(num)
                res = fizz_buzz(n)
            else:
                res = "ERROR (not a valid number / format)"

            print("Number [{}] => {}".format(num, res))
    
    # Exits the program
    exit()

#----------------------------------------------------------------
# End of the file
#----------------------------------------------------------------