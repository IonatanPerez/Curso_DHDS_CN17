import numpy as np

def random_binomial():
    seed_cualquier_numero = 2843
    random_generator_seed = np.random.default_rng(seed_cualquier_numero)
    n = 100
    p = 0.7
    size = 500
    respuesta = random_generator_seed.binomial(n, p, size)
    return(respuesta)

def precipitaciones(data):
    result = data[:, 3]
    return result

def cant_dias_sin_lluvia(precip):
    sin_lluvia_mask = precip == 0
    sin_lluvia = precip[sin_lluvia_mask]
    result = len(sin_lluvia)
    return result

def cant_dias_con_lluvia(precip):
    con_lluvia_mask = precip != 0
    con_lluvia = precip[con_lluvia_mask]
    result = len(con_lluvia)
    return result

def cant_dias_con_lluvia_mayor_100(precip):
    con_lluvia_mayor_100_mask = precip > 100
    con_lluvia_mayor_100 = precip[con_lluvia_mayor_100_mask]
    result = len(con_lluvia_mayor_100)
    return result

def cant_dias_con_lluvia_menorigual_100(precip):
    con_lluvia_menorigual_100_mask = (precip <= 100) & (precip > 0)
    con_lluvia_menorigual_100 = precip[con_lluvia_menorigual_100_mask]
    result = len(con_lluvia_menorigual_100)
    return result

