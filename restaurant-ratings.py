# your code goes here
import sys

# def rate_restaurant(file_name):
#     """ Reads file of ratings and returns ratings in alphabetical order."""

file_name = open(sys.argv[1])

restaurant_dict = {}

for line in file_name:
    line = line.rstrip()
    line = line.split(':')
    
    # rest, rating = line.rstrip().split(':')

    # for word in line:
    restaurant_dict[line[0]] = line[1]

rated_restaurants = sorted(restaurant_dict.items())

for tup in rated_restaurants:
    print tup[0] + ' has a rating of ' + tup[1]

file_name.close()