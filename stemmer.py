from nltk.stem.wordnet import WordNetLemmatizer
import nltk

lmtzr = WordNetLemmatizer()
str = 'ipods and accessories'

text = nltk.word_tokenize(str)

text[:] = [lmtzr.lemmatize(word) for word in text]
print text