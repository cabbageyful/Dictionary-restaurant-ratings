# your code goes here
import sys

# def rate_restaurant(file_name):
#     """ Reads file of ratings and returns ratings in alphabetical order."""

file_name = open(sys.argv[1])

restaurant_dict = {}

for line in file_name:
    line = line.rstrip()
    line = line.split(':')
    print line 

    for word in line:
        restaurant_dict[line[0]] = line[1]

print restaurant_dict