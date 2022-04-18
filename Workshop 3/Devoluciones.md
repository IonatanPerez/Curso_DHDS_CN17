# Notebooks

## Grupo 8

### Integrantes

- Choconi Lucas
- Berra Eliel
- Mina Federico
- Scillato German

### Comentarios de codigo

- Hacen un value counts de los que no tienen datos de colesterol y les da mucho mas desbalanceado que el dataset general. Quizas sea un razon para no tirar esa columna y tratar de usar los datos de alguna manera (o no usando la columna o imputando) en lugar de tirar los registros.
- Bien analisis preliminar: sencillo, claro, correcto.
- Configuran random_states, porque? No es una buena practica salvo que quieran tener reproductivilidad en la ejecucion para testear o para mostrar, pero no es la idea en un trabajo concluido.
- No era que el mixedNB no andaba mejor? Por lo que veo si.
- Me gusto el analisis de los scores en funcion del umbral. Raro el error que mencionan, pero me paso!

- En este codigo:

```

df_scores_filter = df_scores[(df_scores.index<0.2) & (df_scores.index>0.1)]
df_scores_filter = df_scores_filter[df_scores_filter.recall_scores==max(recall_scores)]
best_ths = df_scores_filter.tail(1).index[0]

```

entiendo que quieren buscar el mejor umbral. No entiendo si el criterio de que este entre 0.1 y 0.2 es a ojo o porque. Entiendo que despues buscan donde mejora el recall. Yo hubiera hecho en todo caso algo como:

```
maximo_acc = df_scores.accuracy_scores.sort_values().to_list()[-1]
tolerancia = 0.03
df_scores_filter = df_scores[df_scores.accuracy_scores>= maximo_acc*(1-tolerancia)]
assert df_scores_filter.shape[0] > 10, "La tolerancia es muy baja y no hay suficientes valores para que la busqueda tenga sentido."
mejor_umbral = df_scores_filter.recall_scores.sort_values().tail(1).index[0]
print (f'El mejor umbral encontrado es {mejor_umbral}, que maximiza el recall con una tolerancia en el mejor accuracy de {tolerancia}%')
# Otra opcion es ver que pasa con la suma o con el producto.
df_scores["suma"] = (df_scores.accuracy_scores + df_scores.recall_scores)/2
df_scores["producto"] = df_scores.accuracy_scores * df_scores.recall_scores
ax = df_scores.plot()
ax.vlines(mejor_umbral,0,1)
```

donde me parece mas claro los criterios utilizados. Tomando tolerancia 0.03 me coinciden todas las metricas (lo cual es sintoma de que son criterios robustos.). Hice la prueba y me da mejor todavia la metrica de la matriz de confusion.

- Detalle, en el siguiente grafico repiten todo excepto los umbrales, tiene sentido hacer un grafico con varias lineas verticales.
- Un detalle no tan detalle, esto es en el fondo una busqueda de hiperparametros. Deberian hacer este analisis en el train, no en el test.

### Comentarios generales

- Esta muy bien el trabajo hasta aca, el codigo se entiende bien, es focalizado y completo. 
- Se nota que manejan los conceptos de programacion y de contenido que corresponden al Tp. La unica cuestion tecnica que es objetable es que prueben el umbral en test.
- Quizas estaria bueno repetir la busqueda del "hiperparametro" mejor umbral para los demas modelos, porque la sensibilidad puede depender del tipo de modelo elegido.

## Grupo 7

### Integrantes

- Daniela Rodriguez Golpe
- Mercedes Dorado
- Matías Chaves
- Edgar Wendler
- Nashira Calvo

### Comentarios del codigo

- Esta bien el analisis inicial, probaron hacer contra todas las categorias y despues en categorias mas agrupadas.
- Usan random_states. En clase los usamos para que los codigos sean replicables, pero en un codigo que funciona bien no tiene mucho sentido utilizarlo. 
- El codigo se entiende y esta claro pero quizas algun comentario introduciendo cual es la idea de cada celda sumaria. 
- ¿Porque toman el minimo de knn vecinos como 5? Tendria mas sentido poner 2 o 3, total es gratis probar que tiene mas sentido hacer una prueba exhaustiva para valor bajos que para valores altos porque es mas probable que ahi haya mas efectos.
- Probe poner un corss_validation con 10 folds y tira un error porque no hay un minimo de elementos de la minima categoria para cada grupo. Supongo que por eso eligieron 4. Eso significa que hay muy pocos registros de calidad 3, otro argumento para categorizar los vinos en muy buenos, buenos y malos porque entonces la estadistica seria mas robusta. Fijense que cuando hacen el numero de vecinos ideal con CV da diferentes que en el gridsearch, eso no tiene mucho sentido y es indicador de que la estadistica no esta siendo robusta.
- Ojo con el comentario de la regresion logistica. Es un error conceptual, la regresion logistica asume que hay linealidad en el sentido de que a mas valor de una variable mayor o menos calidad del vino, pero no dice nada de la distribucion de datos (que la frecuencia de aparicion de las caracteriticas no sea lineal).
- Respecto al analisis al agrupar en categorias, les dio bastante peor. Estuve revisando unas cuantas cosas (y volviendo para atras en el codigo) y encontre que buena parte del problema es que no estan estratificando los datos cuando hacen los split. Si se fijan de estartificar eso les mejora bastante las metricas. En el caso de la regresion logistica es mas complicado porque tienen categorias en orden, quizas tiene sentido pensar en una regresion lineal, sino otra opcion que les da algunos parametros significativos es fijarse por ejemplo si la variable target es mayor o menor a algun numero por ejemplo si da mejor o menor que 5 o 6, ahi pueden obtener algunos resultados.

### Comentarios generales

- El trabajo esta bien, pero si pueden revisen esto de la estratificacion porque les va a mejorar lo que hicieron. Respecto a la poca capacidad de predecir con regresion logisticas o con categorias simplificadas mas en general puede ser un problema de los datos. Hay que tener en cuenta que no siempre los datos permiten predecir cosas. Igual prueben lo que les comente que algunas cosas les va a dar mejor. 

## Grupo 6

### Integrantes

- Poner en la notebook

### Comentarios del codigo

- La parte de visualizacion y limpieza esta bien, me voy a focalizar en la parte de modelos. Lo unico que no me gusta mucho es que normalicen las dummies categoricas (creo que lo charlamos en clase pero tiene mas sentido dejarla como categoria y hacer un booleano cada vez que quieren una, porque estan generando una matriz gigante de datos sin mucho sentido, aunque despues filtren cuando la usen.)
- Igual ojo que no guardan la version escalada! Porque nunca ponen en una variable es fit_transform
- Ojo que tienen una celda que les intala cosas con pip. No es una buena idea dejar eso. Si necesitan instalar algo haganlo en consola o despues comenten la celda porque sino cualquiera que corre su codigo se pone a instalar cosas.
- Importan muchas cosas que no usan.
- Ojo que la hiptesis nula es al reves, que de mejor que 95.74, porque uno mide el accuracy, no el error. Y lo mas probable es que marque todo como no rock.
- No redondeen donde quieren mirar detalles en los numeros. No esta bueno redondear a dos decimales algo donde quieen ver como mejora respecto a 95.74 salvo que esperen que les de mucho mas grande que es dificil.
- No se suponia que usaran arboles porque recien lo vimos la clase siguiente a la entrega. Igualmente no parece mejorar mucho las metricas, al contrario (ojo que estan evaluando mal porque entreban y evaluaban en el mismo datset)
- Ojo que se hacen lio con los nombres de las variables. Usan Y_test, y_test, X_test, X, x. No es buena idea. Ademas con hacer un split al principio ya esta, no tiene sentido rehacerlo para cada modelo. Creo que se hicieron lio por eso!

### Comentarios generales

- El codigo esta un poco desprolijo en el sentido que le falta hacer una limpieza de cosas que no usa, unificar nombres de variables, evitar correr muchas veces lo mismo cuando es redundante, etc, pero implementan bien lo que vimos en clase.
- El problema que tienen es que no logran predecir lo que buscan, y parece ser un problema de la eleccion del dataset y la pregunta a trabajar. Eso no esta mal, es simplemente reenfocar el eje de la presentacion. 
- Yo les recomendaria que se encarguen de mostrar en la presentacion como los modelos que usaron no logran predecir lo que querian. Otra opcion es que re ejecuten el codigo para todos los generos (es cambiar una linea arriba, o meter todo en una funcion y llamarla con cada categoria) y vean si para algun genero si se puede predecir porque puede que algun genero sea mas distinguible que otro en sus caracteristicas musicales. Pero en general el trabajo esta bien aunque no haya dado como esperaban, solo sean honestes con los resultados que les dio, porque les dio consistentemente que no logran predecir lo que buscan (por ejemplo la curva ROC dio "pesima" lo cual tiene sentido y esta bien que lo cuenten).

## Grupo 5

### Integrantes

- Poner en la notebook

### Comentarios del codigo

- Importan cosas que no usan, limpien el import cada tanto porque cargar muchas cosas solo hace que tarde mas y que ocupe mas memoria correr el codigo. Ademas si alguien algun dia usa su codigo va a tener que tener instalado todo lo que importen.
- Les falta un pequeña intro con cual es el objetivo antes de empezar la descripcion del dataset. Porque despues empiezan a hablar de columnas mas significativas y no esta claro para que.
- Parece estar bien pero como no esta explicada la logica de lo que quieren revisar me pierdo un poco en la visualizacion, limpieza y analisis preliminar.
- Detalle: no tiene sentido hacer dummie de una variable que ya es booleana como sexo (asumo que lo es en los datos).
- Cuando hacen prints o displays de dataframes con muchas columnas, si quieren verlas enteras o usen algo tipo data.columns() o sino pueden usar pd.set_option("display.max_columns", None) que borra el limite de columnas que muestra para que muestre todas.
- No fijen random_state salvo que tenga sentido
Pasando a la parte de modelos
- Esta bien implementado la regresion logistica, pero falta explicar un poco porque hacen lo que hacen y que hacen con los resultados. Por ejemplo, no se entiende porque eligen las features que elijen en el primer caso ni porque cambian a otras en el segundo mas alla de haber elegido al azar. De hecho en una regresion es facil ver cuales son mas significativas y de hecho piden el resumen estadistico pero no lo interpretan. Es evidente que hay variables mas predictivas que otras, ¿donde analizan eso?, ya sea cualitativamente con intuicion o cuantitativamente con los resultados.
- Cuando hacen el Kfold pueden hacer uno estratificado, de hecho seria imporante porque tienen un dataset muy desbalanceado (aunque tambien tienen muchas muestras)
- Esta bien lo que hacen de medir las metricas para diferentes vecinos pero una implementacion mas sencilla es usar gridsearch. 
- Cuando comparan estandarizando con sin estandarizar en knn, esta bien hacerlo una vez para entender como funciona, pero en general uno aplica directo estandarizacion, porque no hay caso en que en un modelo que use distancias no de mejor estandarizando. 
- Dicen que les dio mejor regresion logistica, pero me parece que no, o entendi algo mal...
- Tiene sentido que NB multinomial funcione peor porque esta pensado para cuando algo toma categorias discretas y se cuentan eventos. 

### Comentarios generales

- La implementacion de los codigos esta bien y cumple con lo que se pedia, pero creo que se podria ordenar un poco el analisis de los datos. Por ejemplo en el analisis preliminar y descriptivo que hicieron pareciera verse que ingresos y edad son factores que influyen mucho en la variable target que estan buscando, y despues no me queda claro que lo retomen.
- Si bien no es el objetivo en si de la notebook, me costo seguir el hilo de que querian ir analizando, quizas intercalar comentarios mas explicativos ayude a leer la notebook y entender porque hacen lo que hacen.
- En cuanto a analisis con codigo podrian profundizar en el analisis de las estadisticas de las regresiones para explicar lo que se ve y tambien hacer algo mas tipo gridsearch con algun parametro mas que el numero de vecinos. 

## Grupo 4

### Integrantes

- Griselda Itovich
- Agustin Helou
- María Eva Ortega

### Comentarios codigo

- Bien el analisis preliminar
- Bien implementacion de codigo en general
- Falta un poco analizar como dan las metricas en comparacion a la hipotesis nula.
- La gracia del gridsearch es no hacer un for!
- No hace falta volver a hacer un tran_test_split en principio, si no lo pisaron pueden usar el original y se aseguran que miran los mismos datos con los diferentes modelos.

### Comentarios generales

- La implementacion del codigo de lo visto en clase esta bien, excepto la idea del gridsearch, y cumplen con el objetivo del trabajo.
- No analizan mucho las metricas y yo que lo volvi a ejecutar no obtengo los mismos resultados qu mencionan al final (no me dio mejor NB sino regresin logistica en la curva ROC por ejemplo)
- En general no les dio mucho mejor que la hipotesis nula, eso no lo mencionan mucho y salvo que por alguna razon les importe la precision, la metrica estandar es el accuracy porque ademas es claro cual es la hipotesis nula con la que comparar. 
- No me queda muy claro cual es la ideal del kmeans del final. Hacen un unico kmeans de todos los datos y despues grafican con variables por separado? Hubiese estado bueno agregar como marker (para distinguir del hue) un indicador de donde estan los que tienen diabetes y los que no, para ver si de alguna manera responde a la clusterizacion. 
- Algo que se podria hacer es ver por ejemplo (con statsmodel) en la regresion logistica cuales son las variables mas explicativas para probar si sacando variables mejora la capacidad predictora de los modelos.

## Grupo 3

### Intregrantes

Pongan integrantes en la notebook

### Comentarios del codigo

- Si usan los datos del ultimo mes, no pueden tener un sesgo de que todavia no haya evolucionado la enfermedad? Quizas hubiera convenido usar datos de tres meses atras o algo asi. Ademas hay que tener en cuenta que justo estamos en un dataset que puede no tener consistencia temporal porque aparecieron las vacunas.
- Me gusta la visualizacion preliminar. Cuando grafican edad hay un claro dato mal cargado (edad=222, debe haber sido 22 y tipearon mal), que despues arrastran.
- Quizas tiene mas sentido para visualizas la informacion normalizar con algun tipo de criterio poblacional, por ejemplo, en lugar de cuantos mueren a cada edad, cuantos de los de cada edad mueren. O cuantos son los casos por distrito en relacion a la poblacion del distrito. 
- Cuando seleccionan las columnas explicativas, porque eligen las que eligen? Es razonable tener algun indice de cuanto tiempo lleva enferma la persona. Esta la columna sepi pero quizas podrian haber levantado de alguna variable con fecha (como fecha internacion) cuanto tiempo paso hasta la fecha de corte de los datos.
- Cuando hacen la estandarizacion, ¿Porque la hacen con min_max? ¿Porque no estadarizan todas las columnas con el mismo criterio?
- Detalle: si van a hacer una instruccion de varias lineas como en el pie, tabulen para que se note que son todos parametros del pie.
- No entiendo que quisieron ver en el pie donde grafican fallecidos y ruido. Haciendo df_scaled[df_scaled["Ruido"]==-1]["fallecido_SI"].value_counts() se que ve hay datos mezclados pero mas fallecidos que no fallecidos, lo cual dice que hay parte alta de los fallecidos que quieren detectar. No es buena idea tirar los outliers con ese criterio, pero menos descartar solo los outliers que son no fallecidos porque estan sesgando mucho los datos justo donde quieren mirar.
- ¿Porque si ya estan rebalancenado el dataset despues prueban darle mas peso a la clase 1? Creo que estan forzando un poco el modelo al hacer balanceo, darle mas peso a la clase 1 y ademas pedir recall. Osea, va a dar un recall alto, pero a que costo? Les da MUY mal el accuracy (peor que la hipotesis nula), y la matriz de confusion da tambien muy mal.
´´´
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
print (accuracy_score(y_test,y_test_pred))
print (y_test.value_counts())
confusion_matrix(y_test, y_test_pred)


0.5591160220994476
0    1676
1     134
Name: fallecido_SI, dtype: int64
array([[886, 790],
       [  8, 126]], dtype=int64)
´´´
- Yo hubiera probado sin hacer resampling, sin forzar recall y viendo despues de jugar con el umbral y analizando la curva ROC.

- Fijense que en knn cuando pasan a test cae brutalmente incluso el recall, lo cual indica que estaban tuneando demasiado el modelo para lo que quieren ver.
- El grafico final probablemente explique porque les dio consistente el modelo re gresion y no los otros. Solo mira la edad, y si, si uno asume que toda la gente muy mayor va a fallecer es un buen predictor, casi que para cualquier escenario. 

### Comentario general

- El analisis preliminar y la implementacion de las cosas vistas en clase esta bien.
- Lo que no esta muy bueno es que se hayan focalizado tanto en el recall porque estan perdiendo la capacidad predictiva de los modelos.

## Grupo 2

### Integrantes

- Poner en la notebook

### Comentarios del codigo

- No pasaron el dataset!!!!! Lo tuve que buscar.

- Tienen algunas cosas que no me queda claro cuando las usan.
- Tienen un accuracy pero no comparan con la hipotesis nula, cuan bueno es ese resultado?
- Ojo que usan el dataset con la constante incluida en la regresion logistica de scikit learn, me tira un error de convergencia, puede ser por eso.
- Ojo que vuelven a usar la columna constante en knn, eso no tiene sentido. Justo como es una constante no deberia romperles el modelo, pero no deberia ir.
- No comparan metricas entre modelos, ni con hipotesis nulas. 
- Hay una parte larga de muchos graficos que no me queda claro que quisieron hacer
- Trate de volver a ejecutar algunos codigos pero tarda muchisimo.

### Comentarios generales

- La implementacion (mas alla del tema de la constante) esta bien.
- Les falto profundizar en comparar las metricas con la hipotesis nula y ente modelos (es corto de hacer)
- Quizas hubiera estado bueno hacer algo tipo curvas ROC porque tienen un datset muy desvalanceado y podrian haber analizado el tema de recall o como focalizarse en el tema de detectar los pocos positivos.

## Grupo 1

### Integrantes

- Poner en la notebook

### Comentarios del codigo

- Trabajaron un monton y el codigo es muy largo, voy a tratar de focalizarme en las partes mas conceptuales de los modelos teniendo en cuenta lo que ya charlamos durante el workshop
- Cuando ejecutas knn, como hiciste una division por espacio de variables es esperable que te de un accuracy de casi 1
- Me perdi un poco en que querian buscar con el primer dbscan
- En el dendograma que se busca agrupar? Usan el resultado de dbscan? En ese caso estan induciendo un mismo agrupamiento.
- Me parece raro que haya dado tantos grupos y tan chicos con dbscan si pusieron que el minimo de los grupos en 25. Y que no separe las categorias manuales 1 y 2
- Me pierdo en que quieren analizar en la parte final cuando vuelven a ejecutar todos los modelos.

###  Comentarios generales

- Es evidente que trabajaron muchisimo y que los contenidos tecnicos de lo que vimos en el curso los manejan muy bien.
- Respecto al enfoque general del trabajo como ya charlamos durante el workshop no comparto el criterio general de poner tantos criterios manuales. 
- Creo que se estan mordiendo la cola con el analisis de modelos al querer "validar" los criterios manuales. No es que este mal, si el criterio es priorizar los criterios manuales, pero no es el objetivo principal con el que vemos los modelos de aprendizaje donde la idea es que el modelo descubra criterios de segmentacion y/o categorizacion. Igual no es que este bien ni mal porque es una discusion de cual es el objetivo con el que uno esta pensando el analisis de datos y depende de lo que cada uno quiera hacer.
- Otro comentario mas en general es que en un codigo mas generico (entiendo que igual no es la logica con que la pensaron), cuantos menos numeros haya mejor. A veces si se van a hacer criterios y parametros conviene explicitarlo en constantes, por ejemplo:

```
data_filtrada = data_filtrada[data_filtrada.ejemplo < 5]
```

conviene ponerlo como:


```
umbral = 5
data_filtrada = data_filtrada[data_filtrada.ejemplo < umbral]
```

Porque entonces la logica del codigo se puede rastrear mejor.

Igual el trabajo es muy completo y mas que cumple los objetos del TP.

