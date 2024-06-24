#add import
#Part 2.3

import question_b
xy = 0
km = input("\nHow far did the car drive? (in kilometers)\n") #get user input of distance
mins = input("\nHow long did it take the car to go that far? (in minutes)\n") #get user input for time

result = question_b.get_miles_per_hour(km,mins)#calculate mph via previously defined function

#check if inputs are - and if so, tell user they inputted bad values
if(int(km) < 0 or int(mins) < 0): # only < as 0 is a fine value for distance but, the car may not have moved
    print("\nInvalid Arguments\n") #values are bad

else:
    print("\nThe car went an average of", result, "mph over the", km, "kilometer interval\n") #values are good so print results


#if 0 is entered for min then divide by zero happens and this wasn't apart of the est requirements/question