def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    if day_of_week < 1 or day_of_week > 7:
        return None
    
    return day[day_of_week - 1]

############ ALTERNATE SOLUTION ##############################
    # week = {1: ‘Sunday’,
    #         2: ‘Monday’,
    #         3: ‘Tuesday’,
    #         4: ‘Wednesday’,
    #         5: ‘Thursday’,
    #         6: ‘Friday’,
    #         7: ‘Saturday’}

    # day = week.get(day_of_week, None)
    # return day