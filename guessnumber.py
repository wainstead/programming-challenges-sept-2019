"""Given an input number "n" guess what number the user is thinking
of, between 1 and "n" inclusive

required data structures:
list of guesses per game

"""


import sys
import math
import logging

def prompt_for_max_value():
    """Prompt the user for the maximum number to guess.

    Returns an integer.

    """

    max_number = None

    while max_number is None:
        try:
            max_number = input("Enter the maximum allowed guess: ")
        except EOFError:
            # Player typed control-d; exit gracefully
            sys.exit(0)

        try:
            max_number = int(max_number)
        except ValueError:
            print("'{}' does not look like an integer. "
                  "Please enter a number.".format(max_number))
            max_number = None
            continue

        if max_number > sys.maxsize:
            print("Sorry, cannot handle numbers larger than %d" % sys.maxsize)
            print("Please enter a smaller number")
            max_number = None

        return max_number


def guess_answer_recursively(lower, upper, steps=1):
    """Use a binary search algorithm to determine the user's number.

    Rather than looping, using recursion was a natural fit to the
    problem.

    This function prompts the user asking if the current guess is low
    (l), high (h) or correct (c).

    """

    assert steps < round(1+ math.log2(max_value)), "Ran out of runway"

    if (lower < -1) or (upper < -1) or (upper < lower):
        raise Exception("Oops bad math; did you give a mistaken answer?")

    middle = lower + round((upper - lower) / 2)

    logging.debug("step %s: lower: %s, middle: %s, upper: %s" % (
        steps, lower, middle, upper))

    if upper == lower:
        # There can be only one
        logging.debug("Answer is {}".format(upper))
        return (upper, steps)

    answer = input("{}? ".format(middle))

    if answer == 'l':
        # Our guess is too low
        steps += 1
        return guess_answer_recursively(middle + 1, upper, steps)
    elif answer == 'h':
        # Our guess was too high
        steps += 1
        return guess_answer_recursively(lower, middle - 1, steps)
    elif answer == 'c':
        logging.debug("Your number is {}".format(middle))
        return (middle, steps)


if __name__ == '__main__':

    logging.basicConfig(
        filename='guessnumber.log',
        level=logging.DEBUG,
        format='%(levelname)s:%(asctime)s:%(message)s')

    max_value = prompt_for_max_value()
    (answer, steps) = guess_answer_recursively(1, max_value)
    print("Your number is {}".format(answer))
    print("That took {} steps to solve".format(steps))
