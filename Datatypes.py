
two_digit_number = input("Type a two digit number: ")

####################################

# to check which datatype is it if you are not getting desired result then write 
#######################################################
 print(type(two_digit_number)) # like this you can check what is the type i.e bool,float.int or string
#######################################################
# like this you can check what type it is like in this case it was string hence we changed it to string and then performed the following addition operation

########################################################

print(int (two_digit_number[0]) + int (two_digit_number[1]))

##############################################################
#some other concepts in datatypes
print(4/2) #this thing will give the result in float # in this the datatype is float 
print(4//2) #if you don't want your result to come in decimal or become a float #in this the datatype is int
print(round(2.6, 2)) #this will help you to print float upto two decimals only place where you wrote 2 is the place where you have to write upto which you want decimal.
score = 0 
#user scores a point
score += 1  #this is gonna work as score = score + 1
print(score) 

#now while using string or while printing the strings and number both at same time we have to use the + sign everytime like for example
score = 0 
print("your score is "+ str(score))

#so to overcome this problem we can use [F-STRINGS] 
print(f"your score is {score}") # The f here denotes f- string like this you have to just mention the integers in the curly braces {} and don't forget to write the f in the starting you can use f string to print both string and integer without typecasting and using the + sign
