import pytest
from scipy import stats
import numpy as np

# https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.binom_test.html

def test_random_binomial(result, n=100, p=0.7):
    
    size = len(result)
    
    if type(result) == np.ndarray:
        p_values = [(stats.binom_test(x, n, p) < 0.05) for x in result]
        proporcion_rechazo = sum(p_values) / size
        if proporcion_rechazo > 0.05:
            msg = "Los datos parecen no cumplir con la distribución pedida."
        else:
            msg = "Muy bien!!"
    else:
        msg = "El tipo devuelto es incorrecto. El resultado debe ser un array ndimensional de Numpy (numpy.ndarray)."    
    return msg



def test_precipitaciones(data):
    
    if type(data) == np.ndarray:
        if len(data) == 365:
            msg = "Muy bien!!"
        elif len(data) < 365:
            msg = "Hay menos elementos de los esperados, se perdió alguna linea del csv"
        else:
            msg = "Hay más elementos de los esperados"
    else:
        msg = "El tipo devuelto es incorrecto. El resultado debe ser un array ndimensional de Numpy (numpy.ndarray)."    
    
    return msg


def test_cant_dias_sin_lluvia(cantidad):
    if cantidad == 215:
        msg = "Muy bien!!"
    else:
        msg = "La respuesta es incorrecta, revisá cómo escribiste la máscara booleana"        
    return msg

def test_cant_dias_con_lluvia(cantidad):
    if cantidad == 150:
        msg = "Muy bien!!"
    else:
        msg = "La respuesta es incorrecta, revisá cómo escribiste la máscara booleana"        
    return msg

def test_cant_dias_con_lluvia_mayor_100(cantidad):
    if cantidad == 47:
        msg = "Muy bien!!"
    else:
        msg = "La respuesta es incorrecta, revisá cómo escribiste la máscara booleana"        
    return msg

def test_cant_dias_con_lluvia_menorigual_100(cantidad):
    if cantidad == 103:
        msg = "Muy bien!!"
    else:
        msg = "La respuesta es incorrecta, revisá cómo escribiste la máscara booleana"
    return msg

