
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


def instruction():
    print()
    print("choose a times times table that you want to do 12 and under ")
    print()
    print("then answer the question given")
    print()
    return""

yes_no_list = ["yes","no"]

for item in range(0, 6):
    # Ask user if they have played before.
    show_instructions = choice_checker("Do you want to see the instructions?",
                                       yes_no_list,
                                       "Please answer yes or no")

    if show_instructions == "yes":
        instruction()


    print("Let's get started...")