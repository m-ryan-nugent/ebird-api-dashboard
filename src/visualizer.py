import textwrap

import seaborn as sns
import matplotlib.pyplot as plt


class EBirdVisualizer:
    def __init__(self):
        pass

    def plot_recent_observations(self, df):
        wrapper = textwrap.TextWrapper(
            width=7, break_long_words=False, break_on_hyphens=False
        )

        plt.figure(figsize=(12, 6))
        sns.barplot(x=df.index, y=df.values)
        plt.xlabel("Species")
        plt.ylabel("Number of Observations")

        wrapped_labels = [wrapper.fill(label) for label in df.index]
        plt.xticks(ticks=range(len(df.index)), labels=wrapped_labels)

        return plt
