
# Generates headings (eg: ----- Heading -----))
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Displays Instructions
def instructions():
    statement_generator("Instructions", "-")

#Display instructions if requested
want_instructions = input("Press <enter> to read the instructions"
                          "or any key to continue ")

if want_instructions == "":
    instructions()

    print('''
    Enter an integer more or equal to 1 and less or equal to 200. The program will show you the factors of your provided integer.
    \n
    It will also tell you if your chosen number:
    - is a prime number (only has two factors)
    - is a square number (odd amount of factors)
    
    
    If you wish to exit the code type 'xxx'
    ''')

# Main routine goes here



print("program continues")