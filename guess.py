import random
number = random.randint(1, 100)
chances = 6
print("Welcome to guessing game. Guess the number between 1 and 100", number)
while(chances>0):
    statement = int(input("Guess number: "))
    if(statement == number):
        print("Congratulations you won!!!")
        break
    elif(statement < number):
        chances = chances - 1
        print("Too low,", chances, "chances left")
        
    else:
        chances = chances - 1
        print("Too high,", chances, "chances left")
        
if(chances == 0):
    print("The number is", number)