"""Given an input number "n" guess what number the user is thinking
of, between 1 and "n" inclusive

"""

import sys
import math
import logging

def prompt_for_max_value():
    """Prompt the user for the maximum number to guess.

    Takes in the number via the input() function.
    Returns an integer.

    """

    max_number = None

    while max_number is None:
        try:
            max_number = input("Enter the maximum allowed guess: ")
        except EOFError:
            logging.debug("User quit the game via control-d")
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

    Rather than looping, using recursion seemed like a natural fit to
    the problem. Since we won't make more than 1 + log2(n) guesses we
    won't recurse very deep.

    This function prompts the user asking if the current guess is low
    (l), high (h) or correct (c).

    """

    assert steps < round(1+ math.log2(max_value)), "Took too many guesses"

    # Known issue: the player may answer 'h' for 1, or 'l' for
    # max_value. In either case they get the stack trace below.
    if (lower < -1) or (upper < -1) or (upper < lower):
        raise Exception("Oops bad math; did you give a mistaken answer?")

    middle = lower + round((upper - lower) / 2)

    logging.debug("step %s: lower: %s, middle: %s, upper: %s" % (
        steps, lower, middle, upper))

    if upper == lower:
        # There can be only one
        logging.debug("Answer is {}".format(upper))
        return (upper, steps)

    answer = None
    while answer not in ('l', 'h', 'c'):
        try:
            answer = input("{}? ".format(middle))
        except EOFError:
            logging.debug("User quit the game via control-d")
            sys.exit(0)

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
        else:
            print("I don't know what '{}' means".format(answer))
            print("Please answer with one of: l, h, c")


if __name__ == '__main__':

    # Log for debugging purposes
    logging.basicConfig(
        filename='guessnumber.log',
        level=logging.DEBUG,
        format='%(levelname)s:%(asctime)s:%(message)s')

    print("In this game, you think of a number from 1 through n and\n"
          "I will try to guess what it is.  After each guess, enter h if my\n"
          "guess is too high, l if too low, or c if correct.")

    max_value = prompt_for_max_value()
    game_results = []
    still_playing = True

    while still_playing:
        (answer, steps) = guess_answer_recursively(1, max_value)
        print("Your number is {}".format(answer))
        print("It took me {} guesses".format(steps))
        game_results.append(steps)
        print("I averaged {:2.2f} guesses per game for {} game(s).".format(
            sum(game_results) / len(game_results),
            len(game_results)))
        if input("Play again? [y/N] ") != 'y':
            still_playing = False
