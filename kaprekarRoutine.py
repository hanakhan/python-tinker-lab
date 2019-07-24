"""
The number 6147 is a special number and is known as Kaprekar's constant. If the digits are sorted in increasing order
and subtracted from the digits sorted in decreasing order, you will get 6147 (7641-1467). This is true for any 4 digit number, including ones with leading zeros. If this process is repeated, eventually the difference between the two numbers will result in Kaprekar's constant. This is known as Kaprekar's routine. If the 4 digits are the same, i.e. 2222, then the difference will return a 0.

This program will execute Kaprekar's routine on a user input 4 digit number and return the number of steps thisn number takes before reaching either 6147 or 0.

See the jupyter notebook version for a more tutorial-style breakdown.
"""


def kaprekarCount(num):
    """
    Returns the number of steps needed for the input number to reach the Kaprekar constant of 6174 or zero
    :param num: Input number
    :return: Number of steps
    """
    count = 0
    kaprekar_constant = 6174
    while True:
        difference = calculate_difference(num)
        count += 1
        if difference == 0 or difference == kaprekar_constant:
            break

        # Casting the difference into a string in order to reuse this value as a new input for the Kaprekar routine
        num = str(difference)
    return count


def calculate_difference(num):
    """
    Subtracts the number with increasing digits from the number with decreasing digits. T
    :param num: Input number
    :return: The difference as an integer
    """
    int_difference = get_decreasing_int(num) - get_increasing_int(num)
    return int_difference


def get_decreasing_int(num):
    """
    Converts the input into a decreasing ordered integer
    :param num: Input number as string
    :return: Re-ordered integer with decreasing order
    """
    decreasing_list = _convert_input_to_ordered_list(num, ascending=False)
    decreasing_int = int(_merge_list_to_value(decreasing_list))
    return decreasing_int


def get_increasing_int(num):
    """
    Converts the input into am increasing ordered integer
    :param num: Input number as string
    :return: Re-ordered integer with increasing order
    """
    increasing_list = _convert_input_to_ordered_list(num)
    increasing_int = int(_merge_list_to_value(increasing_list))
    return increasing_int


def _convert_input_to_ordered_list(str_input, ascending=True):
    """
    Takes the user input string and converts it into a list of ordered string numbers in ascending order unless set to False.
    This is stored as a string in order to retain any trailing or leading zeros.
    :param str_input: The user input number, in the form of a string
    :return: Ordered list of numbers stored as strings
    """
    # Converting integer into a list of integers
    digits_list = [digit for digit in str_input]

    # Sorting the list in a particular order
    if ascending:
        ordered_list = sorted([digit for digit in digits_list])
    else:
        ordered_list = sorted([digit for digit in digits_list], reverse=True)

    return ordered_list


def _merge_list_to_value(list):
    """
    Takes a list of digits (strings) and converts it into a single joined string value
    :param list: List of integers
    :return: Single value digit in the form of a string
    """
    merged_value = (''.join(list))
    return merged_value


# Run code
while True:
    user_input = input('Please enter a 4 digit integer: ')

    if user_input == '':
        break

    # Ensure an integer was entered
    try:
        int(user_input)
    except ValueError:
        print('This is not an integer. Try again.')
        continue

    input_length = len(user_input)
    if input_length > 4:
        print('You have entered more than 4 digits. Try again.')
        continue
    elif input_length < 4:
        # Pad the number with leading zeros to make 4 digits
        user_input = '{:0>4}'.format(user_input)

    # Start the Kaprekar Routine
    count = kaprekarCount(user_input)
    print('The number of steps needed to reach the Kaprekar constant or 0: ', count)
