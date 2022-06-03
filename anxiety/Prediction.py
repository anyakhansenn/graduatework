
from sklearn.ensemble import RandomForestClassifier
import joblib

rf = RandomForestClassifier()

loaded_model = joblib.load('finalized_model.sav')

print(loaded_model.predict([[8.0, 9.0, 7.0, 6.0, 4.0, 4.0, 8.0, 10.0, 6.0, 5.0, 3.0, 6.0, 
6.0, 2.0, 6.0, 5.0, 9.0, 8.0, 6.0, 7.0, 4.0, 6.0, 7.0, 4.0, 3.0, 7.0, 8.0, 2.0, 8.0, 6.0, 
0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 
0.0, 0.0, 0.0]]))

