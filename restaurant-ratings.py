# your code goes here
import sys

# def rate_restaurant(file_name):
#     """ Reads file of ratings and returns ratings in alphabetical order."""

file_name = open(sys.argv[1])

restaurant_dict = {}

user_rest = raw_input("Tell me a restaurant you have been to recently: ").capitalize()
user_rate = int(raw_input("How would you rate the restaurant from 1 to 5: "))

def ordered_rest(user_rest, user_rate):
    """Print list of restaurants and their ratings.

    Reads a file with restaurant name:rating and adds info to the empty 
    restaurant_dict dictionary with restaurant name as key and rating as value
    then adds user's input to the dictionary. Sorts dictionary in alphabetical
    order then prints list of restaurant and rating."""

    for line in file_name:
        # line = line.rstrip()
        # line = line.split(':')
        
        restaurant, rating = line.rstrip().split(':')

        # for word in line:
        restaurant_dict[restaurant] = rating

    restaurant_dict[user_rest] = user_rate  

    rated_restaurants = sorted(restaurant_dict.items())

    for rest, rate in rated_restaurants:
        print rest + ' has a rating of ' + str(rate)

 

ordered_rest(user_rest, user_rate)

file_name.close()