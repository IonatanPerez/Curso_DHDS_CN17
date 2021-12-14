import pytest
from scipy import stats
import numpy as np

def test_ejercicio1(result, media=5, desvio=2, tupla_dim=(1000)):
    
    if type(tupla_dim) == int:
        if tupla_dim == result.shape[0]:
            k, p_value = stats.normaltest(result)
            if p_value > 0.05:
                msg = "Bien!"
            else:
                msg = "Los datos no parecen seguir una distribución como la del enunciado"
        else:
            msg = "Los valores generados no tienen la forma (tamaño) pedida"
    elif type(tupla_dim) == tuple:
        if result.shape == tupla_dim:
             msg = "Bien!"
        else:
            msg = "Los valores generados no tienen la forma (tamaño) pedida"
    else:
            msg = "El parámetro tupla_dim no es una tupla"
        
    return msg

def test_ejercicio3(result, media=5, desvio=2, tupla_dim=(100, 20)):
    msg = test_ejercicio1(result, media, desvio, tupla_dim)
    return msg
    

def test_ejercicio2_media(datos, result):
    test_ok = np.mean(datos) == result
    if test_ok:
        msg = "Bien!"
    else:
        msg = "result no es la media de los datos pasados como parámetro"
    return msg

def test_ejercicio2_desvio(datos, result):
    test_ok = np.std(datos) == result
    if test_ok:
        msg = "Bien!"
    else:
        msg = "result no es el desvío de los datos pasados como parámetro"
    return msg

def test_ejercicio4_media_filas(datos, result):
    test_ok_mask = np.mean(datos, axis=1) == result
    test_ok = result[test_ok_mask]
    if len(test_ok) == datos.shape[0]:
        msg = "Bien!"
    else:
        msg = "result no es la media de los datos pasados como parámetro"
    return msg

def test_ejercicio4_desvio_filas(datos, result):
    test_ok_mask = np.std(datos, axis=1) == result
    test_ok = result[test_ok_mask]
    if len(test_ok) == datos.shape[0]:
        msg = "Bien!"
    else:
        msg = "result no es el desvío de los datos pasados como parámetro"
    return msg

def test_ejercicio5_media_columnas(datos, result):
    test_ok_mask = np.mean(datos, axis=0) == result
    test_ok = result[test_ok_mask]
    if len(test_ok) == datos.shape[1]:
        msg = "Bien!"
    else:
        msg = "result no es la media de los datos pasados como parámetro"
    return msg

def test_ejercicio5_desvio_columnas(datos, result):
    test_ok_mask = np.std(datos, axis=0) == result
    test_ok = result[test_ok_mask]
    if len(test_ok) == datos.shape[1]:
        msg = "Bien!"
    else:
        msg = "result no es el desvío de los datos pasados como parámetro"
    return msg