from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

original_len = 0
stop_filtered_len = 0
stop_words = set(stopwords.words('english')) 


with open("On_Liberty.txt", encoding="utf-8-sig") as f:
    tokens = word_tokenize(f.read())
    original_len = len(tokens)
    filtered = [w for w in tokens if not w.lower() in stop_words]
    stop_filtered_len = len(filtered)

print(f" Original length: {original_len}\n",
    f"Filtered length: {stop_filtered_len}\n",
    f"Ratio: {stop_filtered_len / original_len}"
)
