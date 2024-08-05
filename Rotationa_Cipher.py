
"""An implementation of the rotational cipher"""
    
def rotate(text: str, key: int) -> str:
    """The letter is shifted for as many values as the value of the key.

    :param text: str - string to shifted.
    :param key: int - Number of positions to advance the chars.
    :return: str - new created string.
    """
    
    string = ""
    key = int(key[3:])
    for char in text:
        if char.isalpha():
            if char.islower():
                string += chr((ord(char) - 97 + key) % 26 + 97)
            else:
                string += chr((ord(char) - 65 + key) % 26 + 65)
        else:
            string += char
    return string


print(rotate("Amor", "ROT14"))
