try:
    print(5/0)
except ZeroDivisionError:
    print('Error: No puedes dividir por cero!')
except ArithmeticError: 
    print('Error: Error matematico')
except:
    print('Error: Algo salió mal')