import random

def guess_number():
    while True:
        try:
            lower_limit = int(input("Enter the lower limit: "))
            upper_limit = int(input("Enter the upper limit: "))
            if lower_limit < upper_limit:
                break
            else:
                print("Invalid input!!")
        except ValueError:
            print("Enter the valid range: ")
        
    chances = 10
    
    number = random.randint(lower_limit , upper_limit)
    print(number)
    attempts = 0
    
    while attempts < chances:
        guess = int(input(f"Guess the number: ({lower_limit} , {upper_limit}): "))
        attempts += 1
        
        if guess < number:
            print("Too low Guess a Higher number:..... ")
        elif guess > number: 
            print("Too high Guess a lower number:.....")
        else:
            print(f"You won! in {attempts} attempts.....")
            return
        
        print(f"Chances left: {chances - attempts}")
    print(f"Game Over! the number is {number}......")

guess_number()    