# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year%4==0 & year%100==0 & year%400==0:
    print("Leap year.")
else:
    print("Not leap year.")

