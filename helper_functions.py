

class Helper:
    """
    Create a Helper object, with built-in functions for working with a dataframe.
    ----------
    title : Helper
    -------
    This object has methods to facilitate exploratory data analysis.
    """
    def __init__(self, df):
        """ Initializes the Helper object"""
        self.df = df

    def null_count(self):
        """ Returns the number of NA results in the dataframe."""
        return self.df.isnull().sum().sum()

    def train_test_split(self, frac):
        """ Returns the training and test set of the dataframe for model creation and validation."""
        df = self.df
        n = len(df.index)
        train_length = round(n * frac)
        train_df = df.iloc[:train_length, :]
        test_df = df.iloc[train_length:, :]
        return train_df, test_df
