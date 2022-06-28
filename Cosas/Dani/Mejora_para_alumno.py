import streamlit as st
import pandas as pd 
import numpy as np
import xlrd

st.title("Discover your Adaptivity Level")

t1 = st.markdown("Complete with your ID and discover our special plan for you!")

t2 = st.caption("*We care about your well-being")


#Variables con los que entrenamos el modelo
#id_student = for i in data_raw.id_student():
#i = data_raw['id_student']
              
#ID = st.selectbox('Insert your ID student', id_student)

          
ID2 = st.text_input('Insert your ID student:')



#levantamos el df 
data_raw = pd.read_csv('data_raw_final.csv',sep=';')

maskid = data_raw['ID_student']
diccionario = {}
rango = data_raw.index

'''for indice in rango:
   dict_ing = {}
    dict_ing.clear()
    for ID2 in maskid:
        find = data_raw['ID_student'].iloc[indice].find(data_raw.adaptivity_level)
        if find != null:
            dict_ing[data_raw.adaptivity_level]
        else:
            find = null'''

#st.write("Your adaptatibity is:", Name)        
          

serie_id = data_raw['ID_student']
mask_alumno_momento = (serie_id == 'ID2')



adaptabilidad = data_raw.loc[mask_alumno_momento, "adaptivity_level"]

resultado = adaptabilidad 

resultado