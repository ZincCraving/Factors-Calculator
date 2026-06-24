
# Generates headings (eg: ----- Heading -----))
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")
# Displays Instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
                                Enter an integer more or equal to 1 and less or equal to 200. The program will show you the factors of your provided integer.
                                \n
                                It will also tell you if your chosen number:
                                - is a prime number (only has two factors)
                                - is a square number (odd amount of factors)


                                If you wish to exit the code type 'xxx'
                                ''')
    print("program continues")

# asks the user for an integer between 1 & 200
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

# Works out factors and returns sorted list
def factor(var_to_factor):

    factors_list = []

    for possible_factor in range(1, 201):
        factor_checker = to_factor % possible_factor

        if factor_checker == 0:

            factors_list.append(possible_factor)

    # sorts list and returns it
    factors_list.sort()
    return factors_list

# Main Routine Goes Here

statement_generator( "The Ultimate Factor Finder", "-")

# Display instructions if requested
want_instruction = input("\nPress <enter> to read the instructions "
                          "or enter any key to continue: ")

if want_instruction == "":
    instructions()

while True:

    comment = ""

    to_factor = num_check("\nEnter an integer (or xxx to quit): ")

    if to_factor == "xxx":
            break

    # get factors for integers that are 2 or more
    elif to_factor != 1:
        all_factors = factor(to_factor)

    # Set up comment for unity
    else:
        all_factors = ""
        comment = "One is UNITY! (It only has one factor, itself)"

    # comments for squares/primes


    # Prime numbers only have two factors
    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number"



    # check if the list has an odd number of factors
    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square"

    # Set up headings
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."

        # output factors and comment
    print()
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)



print("Thank you for using the factors calculator")