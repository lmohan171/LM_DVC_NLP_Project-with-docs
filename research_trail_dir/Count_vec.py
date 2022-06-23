from sklearn.feature_extraction.text import CountVectorizer

corpus=[
    'apple ball cat',
    'ball cat dog elephant',
    'very very unizque'
]

vectorizer= CountVectorizer()
X=vectorizer.fit_Transform(corpus)
print(X.toarray())
print(vectorizer.get_feature_name_out())
