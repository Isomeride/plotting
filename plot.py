import numpy as np
import matplotlib.pyplot as plt

def plot(data, epoch_count, best_epoch, labels):
    fig = plt.figure()
    for line, line_label in zip(data, labels):
        plt.plot(np.arange(1, epoch_count+1, 1), line, label=line_label)
    plt.axvline(best_epoch, color='red')
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.gca().set_facecolor('lightgray')
    plt.grid(b=True, which='major', color='white', linestyle='-.')
    plt.legend()
    plt.show()
