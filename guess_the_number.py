import random
print("Welcome to guessing number game")


def random_num():
    number = random.randint(1,100)
    return number


random_number_to_guess = random_num()
difficulty = input("What's your difficulty level-easy or hard: ").lower()
if difficulty == "easy":
    no_of_attempts = 10
else:
    no_of_attempts = 5
print(f"You got {no_of_attempts} attempts")


def compare(value):
    if value > random_number_to_guess:
        return "Too high"
    elif value < random_number_to_guess:
        return "Too low"
    elif value == random_number_to_guess:
        return "You guessed it right, hurrayy!!!"


while no_of_attempts != 0:
    user_input = int(input("Enter the num: "))
    result = compare(user_input)
    print(result)
    if result == "Too high" or result == "Too low":
        no_of_attempts -= 1
    else:
        break
    print(f"{no_of_attempts} attempts left")
    if no_of_attempts == 0:
        print("You ran out of attempts, you lose")
print(f"The number is {random_number_to_guess}")
