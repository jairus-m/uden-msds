# Optional part: decrease the rounding to a preselected increment value i.  
# Say that a house sells for p=25,150 and i=1000. 
# What is the formula for the price? 

# Formula: ((p // i) + 1) * i

def increment_round(p: int, i: int):
    """
    Round a number up by a preselected increment value.
    Args:
        p (int) : integer
        i (int) : increment value
    Returns:
        int : rounded value
    """
    # we went over this in class!
    answer = ((p // i) + 1) * i

    return answer

if __name__ == '__main__':
    p = 25150
    i = 1000

    print(increment_round(p, i))
