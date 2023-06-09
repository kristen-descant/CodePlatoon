def to_roman(num):
    answer = ''

    numeral_dict = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    } 

    for key, value in numeral_dict.items():
        if num >= value:
            numeral_count = num // value
            for add_numeral in range(numeral_count):
                answer += key
            num = num % value

    return answer