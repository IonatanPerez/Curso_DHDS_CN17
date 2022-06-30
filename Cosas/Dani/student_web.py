# importar librerias
import streamlit as st
import pickle
import pandas as pd
#import plotly.express as px
#import matplotlib.pyplot as plt

localpath = './SubRepos/Curso_DHDS_CN17/Cosas/Dani/'
localpath = ''

data_raw = pd.read_csv(localpath + "data_raw_final.csv",sep=';')  #leemos el archio csv desde la raiz

st.title("Nivel de Adaptabilidad Grupo 6")  #Titulo en streamlit
st.write(data_raw.head(4))  # visualize my dataframe in the Streamlit app 


# Convierto los modelos en Pickle para poder llamarlos desde afuera.
with open(localpath + 'lin_reg.pkl', 'rb') as li:
    lin_reg = pickle.load(li)

with open(localpath + 'log_reg.pkl', 'rb') as lo:
    log_reg = pickle.load(lo)

with open(localpath + 'forest.pkl', 'rb') as fo:
    forest = pickle.load(fo)


# funcion para clasificar el tipo de Adaptabilidad del Alumno
def classify(num):
    if num == 0:
        return 'Low'
    elif num == 1:
        return 'High'
    else:
        return 'Moderate'



# Seteo el titulo de mi Streamlit
st.title("Nivel de Adaptabilidad Grupo 6")


# st.write(data_raw)  # visualizar en Streamlit app web el data frame

def main():
    # titulo
    st.title('Graficas de Adaptabilidad')
    # titulo de sidebar
    st.sidebar.header('Parametros')


# Variables con los que entrenamos el modelo
gender = ["Boy", "Girl"]
age = ["1-5", "6-10", "11-15", "16-20", "21-25", "26-30"]
education_level = ["University", "College", "School"]
institution_type = ["Non Government", "Government"]
IT_student = ["No", "Yes"]
location = ["Yes", "No"]
electricity_supply = ["Low", "High"]
financial_condition = ["Mid", "Poor", "Rich"]
internet_type = ["Wifi", "Mobile Data"]
network_type = ["4G", "3G", "2G"]
class_duration = ["03-06", "01-03"]
learning_system = ["No", "Yes"]
device = ["Tab", "Mobile", "Computer"]

# Selección de datos de los Alumnos
def main():
    #titulo
    st.title('Adaptabilidad Alumno')
    #titulo de sidebar
    st.sidebar.header('User Input Parameters')

gender = st.selectbox("Gender", gender)
age = st.selectbox("Age", age)
education_level = st.selectbox("Education", education_level)
institution_type = st.selectbox("Institution type", institution_type)
IT_student = st.selectbox("IT student", IT_student)
location = st.selectbox("Live in city", location)
electricity_supply = st.selectbox("Electricity", electricity_supply)
financial_condition = st.selectbox("Incomes as..", financial_condition)
internet_type = st.selectbox("Internet", internet_type)
network_type = st.selectbox("Quality", network_type)
class_duration = st.selectbox("Class Duration", class_duration)
learning_system = st.selectbox("Custom System", learning_system)
device = st.selectbox("Type Device", device)
        

dict_datos_ingresados = {'gender' : gender,
'age' : age,
'education_level' : education_level,
'institution_type' : institution_type,
'IT_student' : IT_student,
'location' : location,
'electricity_supply': electricity_supply,
'financial_condition' : financial_condition,
'internet_type' : internet_type,
'network_type' : network_type,
'class_duration' : class_duration,
'learning_system' : learning_system,
'device' : device}

# escoger el modelo preferido
option = ['Linear Regression', 'Logistic Regression', 'forest']
model = st.sidebar.selectbox('Modelo a graficar?', option)

st.subheader('Ingrese Parametros')
# st.subheader(model1)
st.subheader(model)

# st.write(df)
while st.button('RUN'):
    X = data_raw.drop(columns = ['adaptivity_level','ID_student'])
    for key in dict_datos_ingresados:
        X.iloc[0][key] = dict_datos_ingresados[key]
    X = pd.get_dummies(X)
    print (X.iloc[0])
    if model == 'Linear Regression':
        st.success(classify(lin_reg.predict([X.iloc[0]])))
        break
    elif model == 'Logistic Regression':
        st.success(classify(log_reg.predict([X.iloc[0]])))
        break
    else:
        st.success(classify(forest.predict([X.iloc[0]])))
        break
    # else model == 'forest':
    # st.print('hola2')
    # st.success(classify(forest.predict(df)))

if __name__ == '__main__':
    main()
