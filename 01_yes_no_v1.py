# functions go here
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "yes"

        else:
            print("PLease enter yes or no")


# main routine goes here
while True:
    want_instructions = yes_no("Do you want to read the instructions? ")

    if want_instructions == "yes" or want_instructions == "y":
        print("instructions go here")

    print("program continues...")
    print()
