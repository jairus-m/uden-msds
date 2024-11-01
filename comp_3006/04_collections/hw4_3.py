import math

def celsiusToFahrenheit(celsius : float):
    """
    Converts temperature from Celsius to Fahrenheit.
    Args:
        celsius (float): temperature in Celsius
    Returns: 
       (float): temperature in Fahrenheit 
    """
    return (celsius * 9/5) + 32

if __name__ == '__main__':
    # declare list of 10 numbers and use map method to convert from C to F
    temps_c = list(range(-10, 36, 5))
    print(f'Temperatures in Celsius: {temps_c}')
    temps_f = list(map(celsiusToFahrenheit, temps_c))
    print('Celsius temperatures converted to Farenheight:')
    print(f'\t{temps_f}')

    # use lambda to display the values of those orignal numbers as args to the sin function
    sin_f = list(map(lambda x: math.sin(x), temps_f))
    print('Convert farenheight temperatures with sin(x) function (units are in radians):')
    print(f'\t{sin_f}')

    # use filter to display only the non-egative values of sin_f
    nonNeg_sin_f = list(filter(lambda x: x > 0, sin_f))
    print('Filter for positive values only:')
    print(f'\t{nonNeg_sin_f}')
