import nltk
from nltk.corpus import wordnet

nltk.download('words')

# Get a list of all English words
all_words = set(word.lower() for word in nltk.corpus.words.words())

# Categorize a word as a noun, verb, adjective, or adverb
def get_word_category(word):
    synsets = wordnet.synsets(word)
    if synsets:
        pos = synsets[0].pos()
        if pos == 'n':
            return 'Noun'
        elif pos == 'v':
            return 'Verb'
        elif pos == 'a':
            return 'Adjective'
        elif pos == 'r':
            return 'Adverb'
    return 'Unknown'

# Example usage
word_to_check = "run"
if word_to_check.lower() in all_words:
    category = get_word_category(word_to_check)
    print(f"{word_to_check} is a {category}.")
else:
    print(f"{word_to_check} is not a valid English word.")
