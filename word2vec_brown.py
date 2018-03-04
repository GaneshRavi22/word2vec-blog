import gensim
from nltk.corpus import brown
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

sentences = []
for sentence in brown.sents():
    filtered_tokenized_text = [w.lower() for w in sentence if not w in stop_words]
    sentences.append(filtered_tokenized_text)

model = gensim.models.Word2Vec(sentences, size=30, window=4, min_count=1, workers=8)
print 'Vocabulary size is: ', len(model.wv.vocab)

# Print the top 10 most similar words to a given word from vocab
print 'Words similar to \'what\' are: ', model.wv.most_similar('what')

# Prints the odd word out from the given words from vocab
print 'Odd word out is: ', model.wv.doesnt_match('what when battle how who'.split())