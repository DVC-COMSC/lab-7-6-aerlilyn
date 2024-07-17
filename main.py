
def getInput():
    """
    ########################################
    Code Your Program here
    ########################################
    """

    while True:
        try:
            # Prompt the user to enter values
            user_input = input("Enter multiple values separated by spaces: ")
            
            # Split the input by spaces and convert them to integers
            values = list(map(int, user_input.split()))
            
            return values
        
        except ValueError:
            print("Invalid. Please try again:")


def makeReverse(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """

    reversed_numbers = []
    
    while numbers:
        num = numbers.pop()
        reversed_numbers.append(num)
    
    return reversed_numbers


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
