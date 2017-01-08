import numpy as np
import matplotlib.pyplot as plt

def plot(pos, neg, tot, methods, organism):
    """Plots the result of an experiment.

    Args:
        pos (Decimal[]): The results for the positive test samples.
        neg (Decimal[]): The results for the negative test samples.
        tot (Decimal[]): The results for both positive and negative test samples.
        method (str): The ml method used for the experiment.
        organism (str): The organism of the experiment.

    Returns:
        None.

    """
    w=0.2
    xIndex = np.arange(len(methods))
    fig, ax = plt.subplots()
    plt.bar(xIndex, pos, width=w, alpha=0.5, align='center', color='g', label="Positive")
    plt.bar(xIndex+w, neg, width=0.2, alpha=0.5, align='center', color='r', label="Negative")
    plt.bar(xIndex+(w*2), tot, width=w, alpha=0.5, align='center', color='b', label="Positive + Negative")
    plt.title('Organism: ' + organism)
    plt.ylabel('Accurracy')
    plt.ylim([0, 1])
    ax.set_yticks([0.4,0.5,0.6,0.7,0.8,0.9,1])
    plt.xlabel('Method used')
    ax.set_xticks(xIndex + w)
    ax.set_xticklabels(methods)
    plt.legend()
    plt.show()
