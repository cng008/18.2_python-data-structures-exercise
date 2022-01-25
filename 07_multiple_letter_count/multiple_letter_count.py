def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    return {ltr: phrase.count(ltr) for ltr in phrase}

    # turn phrase into list, 
    # iterate through list and make keys, 
    # return # times ltr occurs in phrase as value
    
############ ALTERNATE SOLUTION ##############################
    """
    counter = {}

    for ltr in phrase:
        counter[ltr] = counter.get(ltr, 0) + 1

    return counter
    """