#add import

#Part 1.3
import question_a #import code

num = int(input("Please type in a number:\n")) #get a num value via user input

question_a.use_local_variable(num) #here the num variable is initialized to 10 within the function use_local_variable but isn't kept as teh value for num on the global scale.

print("The value you gave is", num, ".") #print final value of num and show its unaffected by the function called