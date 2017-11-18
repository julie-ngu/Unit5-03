# Created by: Julie Nguyen
# Created on: Nov 2017
# Created for: ICS3U
# This program makes an array of 10 random numbers from 1 to 10 and then finds the smallest value of these 
# numbers

from numpy import random

def find_min_value(array = []):
    # finds min value in array
    
    min_number = array[0]
    
    for single_number in array:
        if min_number > single_number:
            min_number = single_number
            
    return min_number

# input
counter = 0
random_numbers = []

while counter < 10:
    single_number = random.randint(1, 10 + 1)
    print(single_number)
    random_numbers.append(single_number)
    counter = counter + 1

# process
smallest_value = find_min_value(random_numbers)

# output
print("\nThe minimum value of the array is " + str(smallest_value) + ".\n")
