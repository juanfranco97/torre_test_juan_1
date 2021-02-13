  
"""This is the main file when we want retrain the regression model or add new features"""

#libraries torre test
from utils import Utils
from models import Models

if __name__ == "__main__":

    utils = Utils()
    models = Models()

    data = utils.load_from_csv('./in/to_model.csv')
    X, y = utils.features_target(data)

    models.grid_training(X,y)