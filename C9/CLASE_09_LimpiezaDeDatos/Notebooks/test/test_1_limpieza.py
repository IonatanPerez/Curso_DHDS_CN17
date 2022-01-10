def dummy():
    return 0;

def test_not_null_count(data, result, axis):
    is_notnull_result = data.notnull()
    data_not_null = is_notnull_result.sum(axis = axis)
    test_ok = all(data_not_null == result)
    if test_ok:
        msg = "Muy bien!!"
    else:
        if type(result) == "pandas.core.series.Series":
            msg = "Error. El tipo de datos del resultado es correcto pero los valores de los elementos son incorrectos"
        else:
            msg = "Error. Se espera un resultado de tipo pandas.core.series.Series"
    return msg


def test_not_null_column_count(data, result):
    axis = 0
    msg = test_not_null_count(data, result, axis)
    return msg


def test_not_null_row_count(data, result):
    axis = 1
    msg = test_not_null_count(data, result, axis)
    return msg

def test_drop_columns_umbral(data, umbral, resultado):
    cant_filas = data.shape[0]    
    cant_filas_min = cant_filas * (1 - umbral)    
    data_clean_col_with_many_null = data.dropna(axis = 1, thresh=cant_filas_min)    
    if resultado is None:
        msg = "Error. Se espera un resultado de tipo pandas.core.frame.DataFrame"    
    else:                
        test_ok = resultado.shape == data_clean_col_with_many_null.shape
        if test_ok:
            msg = "Muy bien!!"    
        elif type(data) == type(resultado):
            msg = "Error. El tipo de datos del resultado es correcto pero el tam del dataframe resultado no lo es"
        else:
            msg = "Error. Se espera un resultado de tipo pandas.core.frame.DataFrame"    
    return msg
    