# // Python Bootcamp Day 1 Assignment
# // Question:

# // Imagine a fun game where you're challenged to guess a secret number. The computer selects a number between 1 and 100, and your task is to figure it out. With each guess, you'll receive hints to guide you.

# // What You’ll Build:

# // The Secret Number:
# // The game begins with the computer randomly selecting a number between 1 and 100. This is the secret number you'll be trying to guess.

# // Making Guesses:
# // You'll be prompted to guess a number between 1 and 100. If your input is outside that range or not a number, the game will remind you to try again.

# // Hints and Feedback:
# // If your guess is too low: "Too low! Try again."
# // If your guess is too high: "Too high! Try again."
# // If you guess correctly, you'll receive a congratulatory message along with the number of attempts.

# // Keep Guessing:
# // The game continues until you guess the correct number, so take your time and think carefully.

# // Ending the Game:
# // Once you've guessed the number, the game will end and let you know how many attempts it took.

# // Fun Extras:
# // To make it even better, handle any mix-ups in input (like letters instead of numbers) gracefully so you can focus on having fun.

import random

a = random.randint(1,100)
print(a)


s = 0

while(True):
    i = int(input("Enter a number between 1-100: "))
    if(i>a):
        print("your number is greater.")
        print("write 0 to exit")
        s+=1
    elif(i<a):
        print("Your number is smaller than that number")
        print("write 0 to exit")
        s+=1
    elif(i==0):
        print("bye bye cutieeeeee")
        break
    else:
        print("yeah you got the number")
        s+=1
        break
    
print(f"your score is {s}")