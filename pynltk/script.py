import nltk

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import pos_tag
from nltk.chunk import RegexpParser
from nltk import ne_chunk

# ---------------------------------------------
# Sample Text
# ---------------------------------------------

text = """
Microsoft was founded by Bill Gates and Paul Allen.
The company is headquartered in Redmond, Washington.
John is studying Natural Language Processing using Python.
"""

print("="*70)
print("Original Text")
print("="*70)
print(text)

# =====================================================
# A. TOKENIZATION
# =====================================================

print("\nA. TOKENIZATION")
print("-"*60)

tokens = word_tokenize(text)

print(tokens)

# =====================================================
# B. STOP WORD REMOVAL
# =====================================================

print("\nB. STOP WORD REMOVAL")
print("-"*60)

stop_words = set(stopwords.words("english"))

filtered_words = [word for word in tokens
                  if word.lower() not in stop_words
                  and word.isalpha()]

print(filtered_words)

# =====================================================
# C. STEMMING
# =====================================================

print("\nC. STEMMING")
print("-"*60)

stemmer = PorterStemmer()

stemmed_words = [stemmer.stem(word) for word in filtered_words]

print(stemmed_words)

# =====================================================
# D. PART OF SPEECH TAGGING
# =====================================================

print("\nD. PART OF SPEECH TAGGING")
print("-"*60)

pos_tags = pos_tag(tokens)

for tag in pos_tags:
    print(tag)

# =====================================================
# E. CHUNKING
# =====================================================

print("\nE. CHUNKING")
print("-"*60)

grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>+}
"""

chunk_parser = RegexpParser(grammar)

chunk_tree = chunk_parser.parse(pos_tags)

print(chunk_tree)

# Uncomment to display graphical tree
# chunk_tree.draw()

# =====================================================
# F. NAMED ENTITY RECOGNITION
# =====================================================

print("\nF. NAMED ENTITY RECOGNITION (NER)")
print("-"*60)

ner_tree = ne_chunk(pos_tags)

print(ner_tree)

# Uncomment to display graphical tree
# ner_tree.draw()

'''| Task                           | Description                                                                           | NLTK Function       |
| ------------------------------ | ------------------------------------------------------------------------------------- | ------------------- |
| Tokenization                   | Splits text into individual words or punctuation tokens.                              | `word_tokenize()`   |
| Stop Word Removal              | Removes common words (e.g., "is", "the", "and") that usually do not add much meaning. | `stopwords.words()` |
| Stemming                       | Reduces words to their root form (e.g., *running → run*, *studying → studi*).         | `PorterStemmer()`   |
| POS Tagging                    | Assigns grammatical tags such as noun, verb, adjective, etc.                          | `pos_tag()`         |
| Chunking                       | Groups tagged words into meaningful phrases like noun phrases (NP).                   | `RegexpParser()`    |
| Named Entity Recognition (NER) | Identifies entities such as persons, organizations, and locations.                    | `ne_chunk()`        |
'''