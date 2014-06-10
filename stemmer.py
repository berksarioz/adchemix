# This code takes a string input and outputs values according to rules.txt
# for each word in the input.
# NLTK helps with NLP code maintainability, but lemmatizer seems to work slow.
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
str = 'Apple iPod 3GB'
# break user input into all lowercase words without punctuation
str = str.lower()
tknzr = RegexpTokenizer(r'\w+')
text = tknzr.tokenize(str)
# get the plural words to simpler form(stemming)
lmtzr = WordNetLemmatizer()
text[:] = [lmtzr.lemmatize(word) for word in text]

# join the stemmed words to enable matching phrases longer than one word
# current code does not take multiword expressions into account
#str = ' '.join(text)
#print str

# map all the keywords known to their respective values from rules.txt
dictionary = {}
f = open('rules.txt', 'r')
for line in f:
    line_arr = line.split(':')
    val = line_arr[0]
    keys = line_arr[1]
    keywords = keys.split(', ')
    #keywords = sorted(keywords, key=len) # sort according to string length
    values = [val] * len(keywords)
    dictionary.update(dict(zip(keywords, values)))

# now print all the values for each word in the input
default = ''
for key in text:
	print key + ' : ' + dictionary.get(key, default)