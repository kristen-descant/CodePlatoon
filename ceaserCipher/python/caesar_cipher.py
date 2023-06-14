def caesar_cipher(string, shift_amount):
    answerStr = ''

    for letter in string:
        ascii_value = ord(letter)

        if ascii_value not in range(65,91) and ascii_value not in range(97,123):
            answerStr += chr(ascii_value)
        elif ascii_value in range(65,91) and (ascii_value + shift_amount > 90):
            ascii_value = ascii_value + shift_amount - 26
            answerStr += chr(ascii_value)
        elif ascii_value in range(65,91) and (ascii_value + shift_amount < 65):
            ascii_value = ascii_value + shift_amount + 26
            answerStr += chr(ascii_value)
        elif ascii_value in range(97,123) and (ascii_value + shift_amount > 122):
            ascii_value = ascii_value + shift_amount - 26
            answerStr += chr(ascii_value)
        elif ascii_value in range(97,123) and (ascii_value + shift_amount < 97):
            ascii_value = ascii_value + shift_amount + 26
            answerStr += chr(ascii_value)
        else:
            ascii_value = ascii_value + shift_amount
            answerStr += chr(ascii_value)
    return answerStr


