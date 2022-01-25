def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # get and keep account the unique elements of the list 
    return max(nums, key = nums.count)
    
    # Call max(iterable, key) with a list as iterable and nums.count as key to find the most common element of the list.


############ ALTERNATE SOLUTION ##############################
   """
    # Make frequency counter of num:freq
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # find the highest value (the most frequent number)

    max_value = max(counts.values())

    # now we need to see at which index the highest value is at

    for (num, freq) in counts.items():
        if freq == max_value:
            return num
    """