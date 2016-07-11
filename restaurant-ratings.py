# your code goes here
import sys

# def rate_restaurant(file_name):
#     """ Reads file of ratings and returns ratings in alphabetical order."""

file_name = open(sys.argv[1])

for line in file_name:
    print line 