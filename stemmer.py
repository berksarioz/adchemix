# nltk helps with nlp code maintainability, but lemmatizer seems to be slow.
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
# break user input into all lowercase words without punctuation
tknzr = RegexpTokenizer(r'\w+')
str = 'ipods, and caLVin klEins'
str = str.lower()
text = tknzr.tokenize(str)
# get the plural words to singular form
lmtzr = WordNetLemmatizer()
text[:] = [lmtzr.lemmatize(word) for word in text]

# join the stemmed words to enable matching phrases longer than one word
# current code does not take multiword expressions into account
#str = ' '.join(text)
#print str

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




print dictionary