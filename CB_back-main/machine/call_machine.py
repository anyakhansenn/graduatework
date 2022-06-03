from sklearn.ensemble import RandomForestClassifier
import joblib


def get_prediction(pr_list: list):
    rf = RandomForestClassifier()
    loaded_model = joblib.load('finalized_model.sav')
    return loaded_model.predict([pr_list])
