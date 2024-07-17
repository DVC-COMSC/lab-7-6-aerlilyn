
def getInput():
    """
    ########################################
    Code Your Program here
    ########################################
    """

    #

    user_input = input("Enter multiple values separated by commas: ")
            
    values = user_input.split(',')
    numbers = []
            
    for value in values:
        num = int(value.strip())  
        numbers.append(num)
            
    return numbers


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
