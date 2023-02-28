import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

plt.style.use('fivethirtyeight')


def plot_scores(scores):

    scores = pd.DataFrame(data=scores, index=[0])

    plt.figure(figsize=(15, 5))
    plt.title('Term Test 1 Review Jeopardy Scores', fontsize=26)
    ax = sns.barplot(x=scores.columns, y=scores.iloc[0])
    ax.xaxis.set_tick_params(labelsize=24)
    ax.yaxis.set_tick_params(labelsize=16)
    ax.set_ylabel('Scores', fontsize=24)
