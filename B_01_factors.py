
# Generates headings (eg: ----- Heading -----))
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Displays Instructions
def instructions(want_instruction):
    statement_generator("Instructions", "-")


    if want_instruction == "":
        instructions()
        print('''
                                Enter an integer more or equal to 1 and less or equal to 200. The program will show you the factors of your provided integer.
                                \n
                                It will also tell you if your chosen number:
                                - is a prime number (only has two factors)
                                - is a square number (odd amount of factors)


                                If you wish to exit the code type 'xxx'
                                ''')
        print("program continues")



# Ask user for width amd loop until they
# enter a number that is more than zero
def num_check(question):

    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response


        try:
            # ask the user for a number
            response = int(response)

            # check that the number is between 1 and 200
            if 1 <= response <= 200:
                return response
            else:
                print(error)


        except ValueError:
            print(error)

# Main Routine Goes Here

statement_generator( "The Ultimate Factor Finder", "-")

# Display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions "
                          "or any key to continue")

if want_instructions == "":
    instructions()

while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
            break