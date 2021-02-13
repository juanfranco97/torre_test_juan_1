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

    def get_x_test(id_job_offer):
        print(id_job_offer)
        df = pd.read_csv('./in/to_api.csv')
        df_2 = pd.get_dummies(df, drop_first=True , dtype=float) 
        row = df_2.loc[df['job_offer_id']==int(id_job_offer)]
        row = row.drop(columns=['job_offer_id'])
        #print(type(row))
        X_test = row.to_numpy()
        #print(X_test)
        #print(type(X_test))
        return X_test