import random

number = random.randint(1, 20)
tries = 0

print("🎲 Guess the Number Game!")
print("I am a number between 1 and 20.")

while True:
    guess = int(input("Who am I: "))
    tries += 1

    if guess < number:
        print("You think I'm an ant,that is too low ⬇️")
    elif guess > number:
        print("I'm not a skyscraper, that is way too high ⬆️")
    else:
        print(f"🎉 Correct, genius! You guessed it in {tries} tries.")
        break