import spacy
from nltk import tokenize
from nltk.corpus import words
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


tokenizer_list = [tkn for tkn in dir(tokenize) if tkn[0].isupper()]
# print(len(tokenizer_list), tokenizer_list, sep='\n')
t_num = 0

def test_tokenizer(tokenizer, *args):
    global t_num
    t = tokenizer(*args)
    tokens = t.tokenize(book_text)
    print(f"{t_num} {tokenizer}")
    print(f"Number of tokens: {len(tokens)}")
    t_num += 1

def test_tokenizer_special(tokenizer, book_text, *args):
    global t_num
    t = tokenizer(*args)
    tokens = t.tokenize(book_text)
    print(f"{t_num} {tokenizer}")
    print(f"Number of tokens: {len(tokens)}")
    t_num += 1

with open("On_Liberty.txt", encoding="utf-8-sig") as f:
    book_text = f.read()
    # Regexpt tokenizer
    test_tokenizer(tokenize.RegexpTokenizer, r"\s*[A-Z]") # Matches start of a sentance
    
    # Whitespace tokenizer
    test_tokenizer(tokenize.WhitespaceTokenizer)

    # Blankline tokenizer
    test_tokenizer(tokenize.BlanklineTokenizer)

    # WordPunct tokenizer
    test_tokenizer(tokenize.WordPunctTokenizer)

    # SExpr tokenizer
    test_tokenizer(tokenize.SExprTokenizer)

    # Space tokenizer
    test_tokenizer(tokenize.SpaceTokenizer)

    # Tab tokenizer
    test_tokenizer(tokenize.TabTokenizer)

    # Line tokenizer
    test_tokenizer(tokenize.LineTokenizer)

    # Syllable tokenizer
    test_tokenizer(tokenize.SyllableTokenizer)

    # Legality tokenizer
    test_tokenizer(tokenize.LegalitySyllableTokenizer, words.words(), "aeiouy")

    # Syllable tokenizer
    test_tokenizer(tokenize.SyllableTokenizer)

    # MWE tokenizer
    wp_tokenizer = tokenize.WordPunctTokenizer()
    wordpunkt_tokens = wp_tokenizer.tokenize(book_text)
    t = tokenize.MWETokenizer(separator=' ')
    t.add_mwe(("putt", "off"))
    t.add_mwe(("add", "up"))
    test_tokenizer_special(t, wordpunkt_tokens)




print("Done")
