from random import randint

def get_random_characters(count : int = 1) -> str:
    """A simple function that returns a string of random characters of length (count)"""
    return "".join(chr(randint(33, 126)) for i in range(count))