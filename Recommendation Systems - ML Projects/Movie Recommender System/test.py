import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
print(stemmer.stem("running"))