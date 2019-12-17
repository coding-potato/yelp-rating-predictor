from surprise import BaselineOnly, accuracy


class BaseLineRecommender(object):
    """
    Use surprise's baselineonly algorithm as the baseline of prediction
    """

    def __init__(self):
        self.model = None

    def fit(self, train):
        """
        Fit the model
        """
        self.model = BaselineOnly(
            bsl_options={"method": "als", "n_epochs": 25, "reg_u": 5, "reg_i": 3}
        )
        self.model.fit(train)

    def predict(self, user_id, item_id):
        """
        Predict ratings
        """
        return self.model.predict(user_id, item_id)

    def rmse(self, test):
        """
        Calculate RMSE for the predicted ratings
        """
        pred = self.model.test(test)
        return accuracy.rmse(pred)
    
    def mae(self, test):
        """
        Calculate MAE for the predicted ratings
        """
        pred = self.model.test(test)
        return accuracy.mae(pred)