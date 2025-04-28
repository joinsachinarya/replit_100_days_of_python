# day13, marks grading
skill  = input("what are you learning: ")
maxpoints = int(input("What is max no. of points: "))
points = int(input("What are your points: "))

if points > maxpoints:
  print("Get the fuck outta here")
elif  points == maxpoints: 
  print("You are a master")
elif (maxpoints - (maxpoints//5)) <= points < maxpoints:
  print("Yove done a good job, your grade is A+🔥")
elif (maxpoints - (maxpoints * 2//5))<= points < (maxpoints - (maxpoints//5)):
  print("You have done a good job, your grade is A")
elif (maxpoints - (maxpoints * 3//5)) <= points < (maxpoints - (maxpoints * 2//5)): 
  print("You have done a good job, your grade is B")
elif (maxpoints - (maxpoints * 4//5)) <= points < (maxpoints - (maxpoints * 3//5)):
  print("You have done a good job, your grade is C")
else:
  print("Failed")










# day 12, debugging 
print("100 Days of Code QUIZ")
print()
input("How many can you answer correctly? ")
ans1 = input("What language are we writing in?")
if ans1 == "python":
  print("Correct")
else:
  print("Nope🙈")
ans2 = int(input("Which lesson number is this?"))
if ans2>12:
  print("We're not quite that far yet")
elif ans2==12:
  print("That's right!")
else:
  print("We've gone well past that!")








# day11, leap year
isLeapYear = input("Is this a leap year?: ")
if isLeapYear == "yes": 
  print(60*60*24*366);
else:
  print(60*60*24*365)





# day10 , math operators
num1 = int(input("Enter first number: ")) #20
num2 = int(input("Enter second number: ")) #3

print("Sum:", num1 + num2) #23
print("Sub:", num1 - num2) #17
print("Mult:", num1 * num2) #60
print("Div:", num1 / num2) # 6.666666666666667
print("Power:", num1**num2) # 8000
print("Modulo:", num1 % num2) # 2
print("Whole number div:", num1 // num2) # 6
# total 7 operators
