#day 18, guess the number game 
myNumber = 100
count = 0
while True:
  number = int(input("Guess the number, it's between 0 to 1000: "))
  if number == myNumber:
    count += 1 
    print("You guessed it right in " +  str(count)  + " tries")
    break
  else: 
    count += 1
    continue










#day 17, rock paper scissor with invalid move and tie handling uisng continue and break
from getpass import getpass as input

valid_moves = ["R", "P", "S"]

while True:
  
  p1 = input("player 1 move (R/P/S): ").upper()
  p2 = input("player 2 move (R/P/S): ").upper()
  
  if p1 not in valid_moves or p2 not in valid_moves:
    print("Invalid move. Moves must be R, P, or S.")
    continue
  elif p1 == p2:
     print("Tie, let's try again")
     continue
  elif p1 == "R":
    if p2 == "P":
      print("Player 2 wins")
      break
    else:
      print("Player 1 wins")
      break
  elif p1 == "P":
    if p2 == "S": 
      print("Player 2 wins")
      break
    else: 
      print("player 1 wins")
      break
  elif p1 == "S":
    if p2 == "R":
      print("player 2 wins")
      break
    else:
     print("player 1 wins")
     break

















#day 16, infinite loop whith while with break statement 
while True:
  print("This program is running")
  goAgain = input("Go again?: ")
  if goAgain == "no":
    break
print("Aww, I was having a good time 😭")






# day 15 , while loop
cnt = 0
while cnt < 10:
  print(cnt)
  cnt = cnt + 1












# day14, rock paper scissors
from getpass import getpass as input

p1 = input("player 1 move (R/P/S): ").upper()
p2 = input("player 2 move (R/P/S): ").upper()

valid_moves = ["R", "P", "S"]

if p1 not in valid_moves or p2 not in valid_moves:
  print("Invalid move")
elif p1 == p2:
  print("Tie, let's try again")
elif p1 == "R":
  if p2 == "P":
    print("Player 2 wins")
  else:
    print("Player 1 wins")
elif p1 == "P":
  if p2 == "S": 
    print("Player 2 wins")
  else: 
    print("player 1 wins")
elif p1 == "S":
  if p2 == "R":
   print("player 2 wins")
  else:
    print("player 1 wins")
  













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
