"""TODO:
Rotating needs to be a bit better
"""

import re

#output = ""

with open("skagit-transcribed.txt", "r", encoding="utf-8") as file:
    text = file.read()

#Deal with hyphenated words
text = re.sub(r"(?<!-section end| PAGE END --)-\n\n?(\S+) ", r"\1\n", text)

#Deal with non-ASCII characters
text = re.sub(r"\u201C|\u201D", '"', text) #Quotes
text = re.sub(r"\u2018|\u2019", "'", text) #Apostrophes/single quotation marks
text = re.sub(r"\u00BB", '', text)         #»

#Characters to be deleted
text = re.sub(r"[|_]", "", text)

#Deal with misplaced characters (no matches)
##text = re.sub(r"(\b\S+)([\"])(\S+\b)", "", text)

#Characters at line beginnings
text = re.sub(r"^(?!-sec|--- PAGE)[^A-Za-z0-9\n]{1,2}", "", text, flags=re.MULTILINE)


with open("skagit-transcribed-processed.txt", "w+", encoding="utf-8") as file:
    file.write(text)