import spacy
from os import environ
from nltk import data
from nltk import tokenize
from nltk.corpus import words
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

class MyTokenizer:
    def tokenize(self, text : str) -> list:
        return text.split()

tokenizer_list = [tkn for tkn in dir(tokenize) if tkn[0].isupper()]
print(len(tokenizer_list), tokenizer_list, "", sep='\n')
t_num = 0

def test_tokenizer(tokenizer, *args):
    global t_num
    t = tokenizer(*args)
    tokens = t.tokenize(book_text)
    print(f"{t_num}: {tokenizer}")
    print(f"Number of tokens: {len(tokens)}")
    print(f"Lexical diversity: {(len(tokens) / len(book_text)) * 100:.2f}%\n")
    t_num += 1

def test_tokenizer_special(tokenizer, book_text, *args):
    global t_num
    t = tokenizer(*args)
    tokens = t.tokenize(book_text)
    print(f"{t_num} {tokenizer}")
    print(f"Number of tokens: {len(tokens):.2f}\n")
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
    test_tokenizer_special(
        tokenize.MWETokenizer,
        wordpunkt_tokens,
        [("putt", "off"), ("add", "up")], ' '
    )

    # Text-tiling tokenizer
    test_tokenizer(tokenize.TextTilingTokenizer)


    # Punkt sentance tokenizer
    test_tokenizer(tokenize.PunktSentenceTokenizer)
    # test_tokenizer(data.load, "tokenizers/punkt/english.pickle")

    # Toktok tokenizer
    sentances = np.array(tokenize.sent_tokenize(book_text))
    newline_sep_sentances = ""
    for s in sentances:
        newline_sep_sentances += s + "\n"
    test_tokenizer_special(tokenize.ToktokTokenizer,newline_sep_sentances)

    # Tweet tokenizer
    test_tokenizer(tokenize.TweetTokenizer)

    # Treebank word tokenizer
    test_tokenizer(tokenize.TreebankWordTokenizer)

    # NLTK word tokenizer
    test_tokenizer(tokenize.NLTKWordTokenizer)

    # My tokenizer
    test_tokenizer(MyTokenizer)

print("Done")
