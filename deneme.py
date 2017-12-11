from sklearn.feature_extraction.text import CountVectorizer

document = [
'I love going out at weekends',
'Yesterday we went to theatre with some friends.',
'How many tickets do I need?',
'Weekends are awesome. I love them.']

vectorizer = CountVectorizer(analyzer='word')
X = vectorizer.fit_transform(document).toarray()
features = vectorizer.get_feature_names()
print(X)
print(features)