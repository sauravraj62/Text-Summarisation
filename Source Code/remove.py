# load data
filename = 'C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/words.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
# convert to lower case
tokens = [w.lower() for w in tokens]
# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
# filter out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
#print(words[:500])
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/new_word_file.txt"

with open(writepath, 'w') as f:
    for i in words:
	    f.write("%s\n" % i)
f.close()
