"""
Pyramid
From the brief:
Please write a web service that takes in a string and 
returns a boolean to indicate whether a word is a pyramid word.  
A word is a ‘pyramid’ word if you can arrange the letters in 
increasing frequency, starting with 1 and continuing without gaps 
and without duplicates.
Examples:
banana is a pyramid word because you have 1 'b', 2 'n's, and 3 'a's.
bandana is not a pyramid word because you have 1 'b' and 1 'd'.
"""


def is_pyramid(text):
    """is_pyramid - determines if text is pyramid form
       ::param:: text - the text to analyze
       ::return:: True if pyramid form, False if not
    """
    result = False

    # print(text, isinstance(text, str), (text or isinstance(text, str)))

    if isinstance(text, str) and text != "":
        letters = {}
        for char in text:
            if not letters.get(char):
                letters[char] = 1
            else:
                letters[char] = letters[char] + 1

        items = sorted(letters.values())
        result = items == list(range(1, len(items) + 1))

    return result
