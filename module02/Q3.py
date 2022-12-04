f_input = int(input('Enter the temperature in Fahrenheit: '))


def to_celcius(f_input):
    return (5 / 9) * (32 - f_input)


print('Temperature: ', to_celcius(f_input), ' Celcius')
