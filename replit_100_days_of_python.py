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
