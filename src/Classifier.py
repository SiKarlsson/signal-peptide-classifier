from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

def train(positiveSamples, negativeSamples, method):
    samples = positiveSamples + negativeSamples
    targets = ([1] * len(positiveSamples)) + ([0] * len(negativeSamples))
    count = CountVectorizer(analyzer='char', lowercase=False).fit(samples)
    tfidf = TfidfTransformer().fit_transform(count.transform(samples))
    if method == "NB":
        return MultinomialNB().fit(tfidf, targets), count
    elif method =="SVM":
        return SVC(kernel="rbf", class_weight={0: 1, 1: 0.85}).fit(tfidf, targets), count

def predict(classifier, sequences, count):
    inputWordCount = count.transform(sequences)
    tfidf = TfidfTransformer().fit_transform(inputWordCount)
    return classifier.predict(tfidf)
