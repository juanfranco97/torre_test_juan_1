""" Some utilities that are used in the application"""
import pandas as pd

class Utils:

    def load_from_csv(self, path):
        """ Read a csv """
        return pd.read_csv(path