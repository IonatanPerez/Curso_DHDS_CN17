#importar las librerias necesarias
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
import pandas as pd
import pickle

localpath = './SubRepos/Curso_DHDS_CN17/Cosas/Dani/'
data_raw = pd.read_csv(localpath + 'data_raw_final.csv',sep=';')  #leemos el archio csv desde la raiz

y = data_raw['adaptivity_level'] == 'Moderate' #target
print (y)
X = data_raw.drop(columns = ['adaptivity_level','ID_student'])
X = pd.get_dummies(X)

#separar los datos en entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(X, y)

lin_reg = LinearRegression()
forest = RandomForestClassifier()
log_reg = LogisticRegression()


#entrenar modelos
forest = forest.fit(x_train, y_train)
lin_regr = lin_reg.fit(x_train, y_train)
log_regr = log_reg.fit(x_train, y_train)


with open(localpath + 'lin_reg.pkl', 'wb') as li:
    pickle.dump(lin_regr, li)

with open(localpath + 'log_reg.pkl', 'wb') as lo:
    pickle.dump(log_reg, lo)

with open(localpath + 'forest.pkl', 'wb') as fo:
    pickle.dump(forest, fo)


print (forest.predict([X.iloc[1]]))
print (X.iloc[1])
