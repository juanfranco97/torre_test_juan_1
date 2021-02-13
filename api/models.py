"""This file have the constructor of regression model"""

#Libraries sklearn
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

#libraries torre test
from utils import Utils

#libraries numpy
import numpy as np

class Models:

    def __init__(self):
        self.reg = {
            'GRADIENT' : GradientBoostingRegressor()
        }

        self.params = {
           'GRADIENT' : {
               'loss' : ['ls', 'lad'],
               'learning_rate' : [0.01, 0.05, 0.1]
           }
        }

    def grid_training(self, X,y):
        """Train differents models with different configurations 
           and export best model based on its score"""

        best_score = 999
        best_model = None

        for name, reg in self.reg.items():

            grid_reg = GridSearchCV(reg, self.params[name], cv=3).fit(X, y.values.ravel())
            score = np.abs(grid_reg.best_score_)

            if score < best_score:
                best_score = score
                best_model = grid_reg.best_estimator_
        

        utils = Utils()
        utils.model_export(best_model, best_score)