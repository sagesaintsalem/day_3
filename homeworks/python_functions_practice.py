def return_10():
    return 10

def add(x, y):
    add_result = x + y
    return add_result

def subtract(x, y):
    subtract_result = x - y
    return subtract_result

def multiply(x, y):
    multiply_result = x * y
    return multiply_result

def divide(x, y):
    divide_result = x / y
    return divide_result

def length_of_string(string):
    string_length = len(string)
    return string_length

def join_string(string1, string2):
    joined_string = string1 +string2
    return joined_string

def add_string_as_number(x, y):
    add_result = int(x) + int(y)
    return add_result



def number_to_full_month_name(month):
    months = {
        1:"January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"October",
        11:"November",
        12:"December",
    }
    return months[month]

def number_to_short_month_name(month):
    short_months = {
        1:"Jan",
        2:"Feb",
        3:"Mar",
        4:"Apr",
        5:"May",
        6:"Jun",
        7:"Jul",
        8:"Aug",
        9:"Sep",
        10:"Oct",
        11:"Nov",
        12:"Dec",
    }
    return short_months[month]

def cube_volume(length):
    result = length ** 3
    return result

def reverse_string(string):
    result = string[::-1]
    return result

def fahrenheit_to_celsius(num):
    result = (int(num) - 32) * (5/9)
    result = round(result)
    return result
