import re

def palindrome(word):
    # Create a regex to test each character.
    edgeRegex = r'\w'
    # Ensure the word is a string
    word = str(word)
    # Initialize a string variable to hold all passing chars
    newWord = ''
    # For loop to add all passing chars to newWord 
    for char in word:
        match = re.match(edgeRegex, char)
        if match:
            newWord += char
    # Variable for reversed string
    reversedword = newWord[::-1]
    # Compare the newWord and reversedWord
    if newWord.lower() == reversedword.lower():
        return True
    
    return False
