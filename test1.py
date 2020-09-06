import pickle
loaded_model = pickle.load(open('model.sav', 'rb'))
result = loaded_model.predict([[22.73726, 75.875987,     2018.0,  	2.0,	28.0,	21.0,	0.0]])
print(result)
