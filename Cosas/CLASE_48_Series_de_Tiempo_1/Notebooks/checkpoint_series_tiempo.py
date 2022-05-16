import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.insert(1, '../../../common/')
from checkpoint import *

descripcion_1 = '''
Cuando descomponemos una serie de tiempo, la evolución de largo plazo de la variable que estamos analizando la capturamos con:
'''
opciones_1 = ['La tendencia', 'La estacionalidad', 'La componente aleatoria']
feedback_1 = ['¡Muy bien! La tendencia corresponde a la evolución de largo plazo de la variable que estamos analizando. Puede ser generada por la lenta evolución y cambios en las preferencias, la tecnología, las instituciones o en la demografía.',
              'Pensálo de nuevo y tené en cuenta que un patrón estacional se repite todos los años.',
              'La componente aleatoria captura shocks que no presentan un efecto duradero.']
test_1 = create_multiple_choice(descripcion_1, opciones_1, opciones_1[0], feedback_1)

descripcion_2 = '''
Cuando trabajamos con series de tiempo, al hacer el split entre train y test sets, lo hacemos de forma aleatoria, es decir con shuffle = True. 
'''
opciones_2 = ['Verdadero: hay que hacer el split de forma aleatoria para no sesgar los sets.', 'Falso: si hacemos un shuffle vamos a tener un problema de data leakage.','Es indistinto, las dos opciones están bien.']
feedback_2 = ['¡Ojo! Al trabajar con series de tiempo tenemos que evitar el data leakage que se generaría al testear con datos del pasado.','¡Muy Bien!','No es indistinto. Si randomizas el split vas a tener un problema de data leakage y vas a sobreestimar la bondad de tu modelo. El shuffle va en False.']
test_2 = create_multiple_choice(descripcion_2, opciones_2, opciones_2[1], feedback=feedback_2)

descripcion_3 = '''
¿Cuáles de las siguientes condiciones son necesarias para que una serie sea estacionaria en sentido débil o estacionaria en la covarianza?

1) La esperanza de y_t es constante a lo largo del tiempo.
2) La varianza debe ser un valor constante y finito para todo t.
3) La autocovarianza debe depender solamente de la traslación k y no de t.

'''
opciones_3 = ['La condición 1.', 'Las condiciones 1 y 2.', 'Las 3 condiciones.']
feedback_3 = ['De esta forma sería solamente estacionaria la media, pero la dispersión podría depender del tiempo.',
              'Nos faltaría asegurar que la covarianza no depende del tiempo.',
              '¡Muy bien¡']
test_3 = create_multiple_choice(descripcion_3, opciones_3, opciones_3[2], feedback=feedback_3)

descripcion_4 = '''
En un modelo ARIMA(p,d,q), el valor de p representa: 
'''
opciones_4 = ['Los rezagos de la serie de tiempo y_t que se incluyen en el modelo.', 'Los errores de pronóstico rezagados que se incluyen en el modelo.','son las diferencias no estacionales que necesitamos para la estacionariedad.']
feedback_4 = ['¡Muy Bien!','No, ese sería el valor de q de la componente de medias móviles.','No, ese sería el valor de d.']
test_4 = create_multiple_choice(descripcion_4, opciones_4, opciones_4[0], feedback=feedback_4)

descripcion_5 = '''
Podemos rechazar la H0. ¿Esto significa que la serie es estacionaria o no? 
'''
opciones_5 = ['Sí, al rechazar la H0 podemos afirmar con una confianza superior al 99% que el residuo es estacionario.', 'No, no podemos afirmar que el residuo sea estacionario.']
feedback_5 = ['¡Muy Bien!','La H0 es que la serie es NO estacionarla, por lo tanto al rechazarla podemos afirmar con un determinado nivel de confianza que la serie es estacionaria.']
test_5 = create_multiple_choice(descripcion_5, opciones_5, opciones_5[0], feedback=feedback_5)

