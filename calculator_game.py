def start():
    print()
    statement_generator("hello world")


def statement_generator(statement, decoration):

    sides = decoration ^ 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration ^ len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


def choose_instruction():
    print("you will be asked the to enter 2 value.")
    print("be divide, add, subtract and multiply")


def check_rounds():


    while True:
        response = input ("how many rounds do you want to play ? ")

        round_error = "please type either <enter> or an integer that is more 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print (round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


rounds_played = 0
rounds = check_rounds()
end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":

        headings = "continue mode: round {}".format(rounds_played + 1)
    else:
        headings = "round {} of {}".format(rounds_played + 1, rounds)
        print(headings)
        choose = input(choose_instruction)
        if rounds_played == rounds - 1:
            
            end_game = "yes"

    print(headings)
    choose = input("{} or 'xxx' to end:".format(choose_instruction))

    if choose == "xxx":
        break
    # rest of loop / game
    print("you choose {}".format(choose))

    rounds_played += 1

    print("thank you for playing")
    

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
                return "yes"

        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes / no")


def choose_instruction():
    print("you will be asked the to enter 2 value.")
    print("be divide, add, subtract and multiply")


played_before = yes_no("do you want to See instructions?")

if played_before == "no":
    print()
else:
    choose_instruction()


a= int(input("enter the value a: "))
b= int(input("enter the value of b: "))


print("sum=",a+b)
print("subtraction=", a-b)
print("multiplication=", a*b)
print("division=",a/b)

