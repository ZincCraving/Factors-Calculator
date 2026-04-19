
# Generates headings (eg: ----- Heading -----))
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Displays Instructions
def instructions():
    statement_generator("Instructions", "-")

#Display instructions if requested
want_instructions = input("Press <enter> to read the instructions"
                          "or any key to continue")

if want_instructions == "":
    instructions()

    print('''
    - Enter an integer more or equal to 1 and less or equal to 200
    - If you wish to exit the code type 'xxx'
    ''')

# Main routine goes here



print("program continues")