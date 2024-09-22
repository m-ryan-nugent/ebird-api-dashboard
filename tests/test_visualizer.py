from unittest import TestCase, main

import pandas as pd
import matplotlib.pyplot as plt

from src.visualizer import EBirdVisualizer


class TestVisualizer(TestCase):

    def setUp(self):
        self.visualizer = EBirdVisualizer()
        self.data = {
            "American Robin": 7,
            "House Sparrow": 3,
            "Blue Jay": 5,
        }
        self.data = pd.Series(self.data)

    def test_plot_recent_observations(self):
        plot = self.visualizer.plot_recent_observations(self.data)

        self.assertIsNotNone(plot)
        self.assertEqual(plot, plt)

        fig = plt.gcf()
        ax = plt.gca()

        self.assertEqual(fig.get_size_inches().tolist(), [12, 6])

        self.assertEqual(ax.get_xlabel(), "Species")
        self.assertEqual(ax.get_ylabel(), "Number of Observations")

        self.assertEqual(len(ax.patches), len(self.data))

        x_tick_labels = [t.get_text() for t in ax.get_xticklabels()]
        self.assertTrue(all("\n" in label for label in x_tick_labels))

        plt.close()


if __name__ == "__main__":
    main()
