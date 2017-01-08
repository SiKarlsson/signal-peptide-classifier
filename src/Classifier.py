from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

def train(positiveSamples, negativeSamples, method):
    """Fits a model to the training samples.

    Args:
        positiveSamples (str[]): The samples containing signal peptides.
        negativeSamples (str[]): The samples not containing signal peptides.
        method (str): Which ml method to use. Either 'SVM' or 'NB'

    Returns:
        The trained model.

    """
    samples = positiveSamples + negativeSamples
    targets = ([1] * len(positiveSamples)) + ([0] * len(negativeSamples))
    count = CountVectorizer(analyzer='char', lowercase=False).fit(samples)
    tfidf = TfidfTransformer().fit_transform(count.transform(samples))
    if method == "NB":
        return MultinomialNB().fit(tfidf, targets), count
    elif method =="SVM":
        return SVC(kernel="rbf", class_weight={0: 1, 1: 0.85}).fit(tfidf, targets), count

def predict(classifier, sequences, count):
    """Predicts if the given sequences contains signal peptides or not.

    Args:
        classifier (Classifier): The trained model.
        sequences (str[]): The sequences to predict.
        count (CountVectorizer): The frequency of amino acids from the trained model

    Returns:
        A prediction for each sequence in the sequence list.

    """
    inputWordCount = count.transform(sequences)
    tfidf = TfidfTransformer().fit_transform(inputWordCount)
    return classifier.predict(tfidf)
