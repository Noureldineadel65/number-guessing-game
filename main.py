import random
difficulty = "easy"
attempts = 10
random_number = random.randint(1, 101)
print('''

 __   __     __  __     __    __     ______     ______     ______        ______     __  __     ______     ______     ______    
/\ "-.\ \   /\ \/\ \   /\ "-./  \   /\  == \   /\  ___\   /\  == \      /\  ___\   /\ \/\ \   /\  ___\   /\  ___\   /\  ___\   
\ \ \-.  \  \ \ \_\ \  \ \ \-./\ \  \ \  __<   \ \  __\   \ \  __<      \ \ \__ \  \ \ \_\ \  \ \  __\   \ \___  \  \ \___  \  
 \ \_\\"\_\  \ \_____\  \ \_\ \ \_\  \ \_____\  \ \_____\  \ \_\ \_\     \ \_____\  \ \_____\  \ \_____\  \/\_____\  \/\_____\ 
  \/_/ \/_/   \/_____/   \/_/  \/_/   \/_____/   \/_____/   \/_/ /_/      \/_____/   \/_____/   \/_____/   \/_____/   \/_____/ 
                                                                                                                               

''')
print("Welcome to the number guessing game.")
print("I am thinking of a number between 1 and 100.")
difficulty_choice = input("Type 'easy' or 'hard': ").lower()
if difficulty_choice == "hard":
    difficulty = "hard"
    attempts = 5
while not attempts == 0:
    print(f"You have {attempts} remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess > random_number:
        print("Too high")
    elif user_guess < random_number:
        print("Too low")
    elif user_guess == random_number:
        print("You Won!")
        break
    attempts -= 1
    if not attempts == 0:
        print("Guess Again.")
