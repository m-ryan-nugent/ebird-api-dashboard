import pandas as pd


class EBirdDataProcessor:
    def __init__(self):
        pass

    def process_observations(self, observations):
        df = pd.DataFrame(observations)
        df["obsDt"] = pd.to_datetime(df["obsDt"])
        df["month"] = df["obsDt"].dt.month
        df["year"] = df["obsDt"].dt.year

        return df

    def top_ten_species(self, df: pd.DataFrame):
        aggregate_df = (
            df.groupby(["comName"])["howMany"]
            .sum()
            .sort_values(ascending=False)
        )
        top_ten_df = aggregate_df.head(10)

        return top_ten_df
