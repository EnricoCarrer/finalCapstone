# Exercise: given a set of words, create new words by adding or removing prefixes and suffixes. 

# Part 1: Add a prefix to a word. 
# This function takes a word as parameter and adds the prefix "un" at the front of the word.

def add_prefix_un(word):
    print(f'Prefix: "un"')
    new_world = f"un{word}"
    return f'Word: {word}  -->  with the prefix: {new_world}'

print(add_prefix_un("happy"))
print ("----------------------")

# Part 2: Add prefixes to word groups.
# This function takes a list of words including a prefix and other words. Then it adds the prefix to each of the other words.

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    print(f'Prefix: "{prefix}"')
    print(f'Words: {words}')
    word_with_prefix = [f"{prefix}{word}" for word in words]
    return f'The new words with the prefix: {word_with_prefix}'
    
print (make_word_groups(['en', 'close', 'joy', 'lighten']))
print (make_word_groups(['pre', 'serve', 'dispose', 'position']))
print (make_word_groups(['auto', 'didactic', 'graph', 'mate']))
print (make_word_groups(['inter', 'twine', 'connected', 'dependent']))
print ("----------------------")

# Part 3: Remove a suffix from a word.
# This function takes a word with the suffix "ness" and return the root word by removing the suffix.
# When necessary, it also replce the last letter "i" with the letter "y". 

def remove_suffix_ness(word):
    root = word[:-4]
    return 'Word: ' + word + '  -->  Root word: ' + root if root[-1] != 'i' else 'Word: ' + word + '  -->  Root word: '+ root[:-1]+'y'
    
print(remove_suffix_ness("happiness"))
print(remove_suffix_ness("sadness"))
print ("----------------------")

# Part 4: Extract and transform a word into a verb.
# This function takes a sentence and an index as parameters. 
# The index indicates an adjective in the sentence that will be transformed into a verb.

def adjective_to_verb(sentence, index):
    list = sentence[:-1].split(" ")
    return 'Adjective: ' + list[index] + '  -->  Verb: ' + list[index] + 'en'

print (adjective_to_verb('I need to make that bright.', -1 ))
print (adjective_to_verb('It got dark as the sun set.', 2))
