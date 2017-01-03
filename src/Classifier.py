from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

def train(positiveSamples, negativeSamples, method):
    samples = positiveSamples + negativeSamples
    targets = ([1] * len(positiveSamples)) + ([0] * len(negativeSamples))
    count = CountVectorizer(analyzer='char', lowercase=False).fit(samples)
    tfidf = TfidfTransformer().fit_transform(count.transform(samples))
    if method == "nb":
        return MultinomialNB().fit(tfidf, targets), count
    elif method =="svc":
        return SVC(kernel="rbf").fit(tfidf, targets), count

def predict(classifier, sequences, count):
    inputWordCount = count.transform(sequences)
    tfidf = TfidfTransformer().fit_transform(inputWordCount)
    return classifier.predict(tfidf)
