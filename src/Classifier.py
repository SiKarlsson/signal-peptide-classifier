from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

def train(positiveSamples, negativeSamples):
    samples = positiveSamples + negativeSamples
    targets = ([1] * len(positiveSamples)) + ([0] * len(negativeSamples))
    count = CountVectorizer(analyzer='char', lowercase=False).fit(samples)
    tfidf = TfidfTransformer().fit_transform(count.transform(samples))
    return MultinomialNB().fit(tfidf, targets), count
