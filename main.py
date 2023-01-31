from config import Calcular_ISR, Calcular_Seguro

print()
print("""Bienvenido estimado usuario
en esta pequeña app, podra calcular el seguro facultativo e
ISR vigente conforme Ley tributaria vigente en Nicaragua""")

def main():
    print()

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    print()
    salario = float(input("Ingresar salario: "))
    porcentaje = float(input("Ingresar porcentaje de seguro: "))

    print("""
    Indicar 12: Mensual
    Indicar 24: Quincenal
    """)

    tiempo = int(input("Periodo de nomina: "))
    
    INSS_Laboral = (Calcular_Seguro(salario,porcentaje))

    ISR = Calcular_ISR(salario,porcentaje,tiempo)

    Neto =  salario - INSS_Laboral - ISR
    print()
    print("===========================================")
    print("||       Recibo Oficial de pago          ||")
    print("===========================================")
    print("Nombre completo: ",nombre+" "+apellido      )
    print(f'Salario        : C${salario:,.2f}         ')               
    print(f'INSS Laboral   : C${INSS_Laboral:,.2f}    ') 
    print(f'ISR            : C${ISR:,.2f}             ')
    print(f'Neto a recibir : C${Neto:,.2f}            ')
    print("===========================================")
    print()

if __name__ == "__main__":
    main()

