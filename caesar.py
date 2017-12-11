
alphabet = "abcdefghijklmnopqrstuvwxyz"

def rotate_character(char, rot):
    rotation = (alphabet_position(char) + rot) % 26
     # allows user to enter numbers larger than 26
    if char.isupper():
        return alphabet[rotation].upper() #Keep uppercase uppercase
    else:
        return alphabet[rotation] 

def alphabet_position(letter):
    new_letter = letter.lower() # to ignore case
    return alphabet.index(new_letter) #Get each letters position in the alphabet

def rotate_string(text, rot):
    letter_str = ''
    for char in text:
        if char.isalpha():
            letter_str += rotate_character(char, rot)
        else:
            letter_str += char    
    return letter_str      