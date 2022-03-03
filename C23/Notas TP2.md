# Cronograma

- 7/3: Para el fin del dia lunes tiene que tener un dataset donde puedan ejecutar algun modelo y mostrarlo cuando pasemos por los grupos en la clase. 
- 10/3 Para el fin del jueves, tienen que tener la notebook donde con alguna seleccion de features hagan los tres modelos y comparen resultados.
- 14/3 Para el lunes de la entrega tienen que tener video+presentacion ademas de la notebook.

# Objetivos previos del Tp 1

- Tener una version limpia del dataset de properati 
- Tener un analisis descriptivo de dataset

# Objetivos especificos de este Tp 2

- Que hagan el OLS con sm y que discutan los resultados en terminos estadisticos.
- Que hagan Lasso/Ridge con skl y comparen con OLS.
- Que tengan un modelo con el cual poder predecir precios de propiedades dadas su caracteristicas.

# Objetivos generales de los Tp

- Tener claro el objetivo del trabajo que se quiere realizar (poder explicar para que se va a escribir las diferentes partes del codigo).
- Tener herramientas de visualizacion (graficos visualmente amigables y correctos en cuanto a contenido) que permitan justificar el trabajo a realizar y comprobar si el codigo cumple con lo que se busca.
- Armar una presentacion (ppt o equivalente) autoinclusiva donde se cuente el trabajo realizado pensando en un publico general.
- Armar un video donde basandose en la presentación se cuente el trabajo realizado.
- Presentar la notebook con los codigos utilizados incluyendo una documentacion minima que permita entender los mismos.

# Sugerencias para trabajar en este Tp

- Comenzar por una revision del estado del dataset del Tp 1.
    - Si no lo hicieron en su momento hagan una comparativa rapida entre el dataset antes y despues de la limpieza. Incluir graficos adecuados para visualizar el contraste.
    - Si no lograron tener el dataset limpio o consideran que conviene aplicar otro criterio hacerlo contando brevemente lo que agregaron/modificaron.
    - Describir brevemente el dataset con el que van a trabajar.
- Seleccionar un conjunto de features que tengan un criterio conceptual basados en la hipotesis de trabajo.
    - Pueden no usar todas las columnas o pueden no usar todas las filas en pos de simplificar el modelo o en pos de tener datos mas limpios, pero es importante que tengan claro, justifiquen y cuenten cual fue el criterio utilizado y porque.
    - Pueden hacer mas de una seleccion dentro del dataset para despues comparar resultados entre elecciones diferentes del dataset.
- Analisis de los diferentes modelos:
    - Comenzar por un analisis de las variables que les parezcan mas significativas con modelos de regresion simples. Hacer graficos (porque son las pocas cosas de las que pueden hacer graficos) mostrando los resultados obtenidos.
    - Hacer una regresion lineal multiple usando statsmodel para poder interpretar la significancia estadistica de los coeficientes obtenidos. Discutir los resultados y en funcion de ellos agregar variaciones (por ejemplo terminos polinomicos, logaritmicos o de interaccion) y comparar los resultados.
    - Utilizando los metodos Lasso y Ridge evaluar si hay sobreajuste en los modelos lineales y comparar resultados. Discutir que variables parece ser relevantes y cuales no en base a los resultados.
    - Hacer un cuadro comparativo con los resultados obtenidos y en caso de que haya hiperparametros cuales son los elegidos.
- Resultados de los modelos:
    - En caso de que tengan tiempo de aplicar los modelos a mas de un dataset diferente (seleccion diferente de columnas y filas) comparar la performance en los diferentes casos. Seria interesante ver si la seleccion del modelo y los hiperparametros es la misma o conviene cambiarla.
    - Generar una celda de codigo autoinclusiva con las mejores elecciones de modelos e hiperparametros donde se ajuste el modelo y luego se pueda predecir precios para propiedades nuevas (tener separado el codigo que efectivamente se quiere usar para entrenar el modelo del analisis previo). 
- Presentacion visual:
    - Hacer algun tipo de visualizacion donde muestren la variable target en geopandas u otra visualizacion razonable, puede ser descriptivo (a partir del dataset y no del modelo) en caso de que no lo hayan hecho antes.
    - Como opcion mas avanzada se puede entrenar diferentes modelos basados en variables especificas (por ejemplo geolocalizacion o propiedades categoricas de la casa restringiendose a valores fijo de otras variables) y luego armar una visualizacion donde se recorra los valores de la variables para representar como cambia del valor de la propiedad (o del metro cuadrado) en funcion de las variables predictoras. 



