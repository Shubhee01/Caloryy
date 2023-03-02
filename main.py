import pickle
import sklearn
import numpy as np

def caloriespred(gender,age,height,weight,duration,heartrate,bodytemp):
  loaded_model = pickle.load(open('calorymodel.pkl', 'rb'))
  input_data = [gender,age,height,weight,duration,heartrate,bodytemp]
  X_new = np.asarray(input_data)
  X_new = X_new.reshape(1,-1)
  Y_pred = loaded_model.predict(X_new)
  return Y_pred[0]

# Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp
# prediction1([1,27,165.0,65.0,6.0,85.0,39.2])