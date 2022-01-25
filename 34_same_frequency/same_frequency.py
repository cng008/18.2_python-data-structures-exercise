def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    first = str(num1)
    second = str(num2)

    if [i for i in first if i not in second]:
        return False
    return True



############ ALTERNATE SOLUTION ##############################
    # return sorted(str(num1)) == sorted(str(num2))

############
    # return freq_counter(str(num1)) == freq_counter(str(num2))

    # def freq_counter(coll):
    # """Returns frequency counter mapping of coll."""

    # counts = {}

    # for x in coll:
    #     counts[x] = counts.get(x, 0) + 1

    # return counts