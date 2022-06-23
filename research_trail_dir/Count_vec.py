from sklearn.feature_extraction.text import CountVectorizer

corpus=[
    'apple ball cat',
    'ball cat dog elephant',
    'very very unizque'
]

max_features=100
ngrams=2 #trigram

vectorizer= CountVectorizer(max_features=max_features,ngram_range=(1,ngrams))
X=vectorizer.fit_transform(corpus)
print(X.toarray())
print(vectorizer.get_feature_names_out())
