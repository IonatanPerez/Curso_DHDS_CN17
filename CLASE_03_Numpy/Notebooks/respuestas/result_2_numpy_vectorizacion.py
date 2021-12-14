import numpy as np

def ejercicio1_3(media, desvio, tupla_dim):
    seed_cualquier_numero = 4703
    random_generator_seed = np.random.default_rng(seed_cualquier_numero)
    result = random_generator_seed.normal(media, desvio, size = tupla_dim)
    return result

def ejercicio1():
    media = 5
    desvio = 2
    tupla_dim = 100
    result = ejercicio1_3(media, desvio, tupla_dim)
    return result


def ejercicio3():
    media = 5
    desvio = 2
    tupla_dim = (100, 20)
    result = ejercicio1_3(media, desvio, tupla_dim)
    return result


def ejercicio2_media(array):
    result = np.mean(array)
    return result

def ejercicio2_desvio(array):
    result = np.std(array)
    return result

def ejercicio4_media_filas(data):
    result = np.mean(data, axis=1)
    return result

def ejercicio4_desvio_filas(data):
    result = np.std(data, axis=1)
    return result

def ejercicio5_media_columnas(data):
    result = np.mean(data, axis=0)
    return result

def ejercicio5_desvio_columnas(data):
    result = np.std(data, axis=0)
    return result
