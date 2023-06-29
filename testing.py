

"""Current file for work

TODO:
- Bring in dictionary, use it to add characters to the end of words
- Figure out what functions in file_analysis.py are of any use
- Investigate other issues in the OCR result
- Use LP-OCR-rotating.py
- Figure in punctuation and misspelling
- Improve word set to exclude words that basically never occur/can mess up the stuff here
- Improve character matching regex
- Figure out how to get rid of bad punctuation, or "}{[]-" characters when not needed
- https://stackoverflow.com/questions/9480013/image-processing-to-improve-tesseract-ocr-accuracy

Dependencies:
pip install english-words

"""

#Imports
import re


with open("words.txt", "r") as file:
    words = file.readlines()


#Functions
def match_words (word: str, test_word: str) -> int:
    """Compares word and test_word, returns for how many characters test_word matches word.
    word is assumed to be shorter or of equal length"""
    chars_matched = 0
    
    for letter_num in range(len(word)):
        if word[letter_num] != test_word[letter_num]:
            return chars_matched
        else:
            chars_matched += 1
    
    return chars_matched


with open(r"skagit-transcribed.txt", "r", encoding="utf-8") as file:
    full_text = file.readlines()

#Currently just for adding characters to the end of lines if the word is incomplete
for line in full_text:
    
    word = re.search(r"[^\W\d_]{3,}(?=\n?)$", line, flags=re.UNICODE)
    #If the word exists and is not a proper noun,
    if word and not word.group()[0].isupper():
        #Get the output from the regex result object
        word = word.group()
    else:
        continue

    is_word = False

    max_chars_matched = 0
    best_words = []

    for test_word in words:
        if test_word == word:
            is_word = True
            break
        
        if len(test_word) < len(word):
            continue
        
        chars_matched = match_words(word, test_word)

        if chars_matched > max_chars_matched and max_chars_matched > 2:
            best_words = [test_word]
            max_chars_matched = chars_matched
        elif chars_matched == max_chars_matched and max_chars_matched > 2:
            best_words.append(test_word)
    
    if (len(best_words) > 0):
        print(best_words)
    print(word)
