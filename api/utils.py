""" Some utilities that are used in the application"""
import pandas as pd
import joblib

class Utils:

    def load_from_csv(self, path):
        return pd.read_csv(path)

    def features_target(self, dataset):
        y = dataset['salary']
        X = dataset.drop(['salary'], axis=1)
        return X,y

    def model_export(self, clf, score):
        print(score)
        joblib.dump(clf, './models/best_model.pkl')

    def get_x_test(self, id_job_offer):
        print(id_job_offer)
        df = self.load_from_csv('./in/to_model.csv')
        row = df.iloc[df['id_job_offer']==id_job_offer]
        print(row)