from time import time
from random import randint, random


def show_help():
    print("do you want to see the instruction")


    while True:
        response = input("how many rounds do you want to play ? ")
           
        round_error = "please type either <enter> or an integer that is more 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response

def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

                # output error if item nt in list

        print(error)
        print()
yes_no_list = ["yes","no"]
show_help = choice_checker("do you want to see the instruction?",
                                   yes_no_list,
                                   "Please answer yes or no")
if show_help == "yes":
    print("answer the random multiplication question given")


while True:

    # generates two numbers
    num1 = randint(1, 9)
    num2 = randint(1, 9)

    # calculate the correct answer
    product = num1 * num2
    start_time = time()
    
    # ask user the question
    response = input(f'what is {num1} * {num2}? ')

    if response == "xxx":
        break

    # works out how long it took user to answer the question
    elapsed_time = time() - start_time
    if not response:
        break

    try:
        ans =int(response)
        print(f'CORRECT IN {elapsed_time:.2f} seconds' if ans == product else print(F'WRONG IN {elapsed_time:.2f}'))
        print(num1*num2)

    except ValueError:
        print("please type a number or ")
        print("press'xxx' to quit")
        
    

        