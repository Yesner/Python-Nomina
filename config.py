def Calcular_Seguro(salario, porcentaje)->float:
    seguro = round((salario * (porcentaje/100)),2)
    return seguro


def Calcular_ISR(salario, porcentaje, tiempo)->float:
    seguro = round((salario * (porcentaje/100)),2)

    proyeccion_anual =  ((salario-seguro)*tiempo)

    if proyeccion_anual <100000:
        ISR = 0
    elif proyeccion_anual <=200000:
        ISR = ((proyeccion_anual-100000)*.15)/tiempo
    elif proyeccion_anual <= 350000:
        ISR = (((proyeccion_anual-200000)*.20)+15000)/tiempo
    elif proyeccion_anual <= 500000:
        ISR = (((proyeccion_anual-350000)*.25)+45000)/tiempo
    else:
        ISR = (((proyeccion_anual-500000)*.30)+82500)/tiempo

    return ISR
