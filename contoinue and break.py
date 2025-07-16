'''#continue
for i in range(1,11):
        if i ==5:
            continue
        else:
            print(i)


# break
for i in range(1,101):
     if i == 50:
          break
     else:
          print(i)
          print ("thank you")


nesw

for i in range (1,21):
    print (i,i )
      
'''
import random  # to generate a random number

secret_number = random.randint(1, 100)  # random number between 1 and 100
guess = None  # to store the user's guess
attempts = 0  # to count the number of guesses

print("🎮 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
