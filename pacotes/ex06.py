while True:
    try:    
        numero = int(input('Entre com um número: '))
        print(5/numero)
        break
    except (ValueError, ZeroDivisionError):
        print('Valor errado ou não é possivel dividir0 por zero')
    except:
        print('EXPLOÇÃOOOOOOOOOOOOOOOOOO BOOOOOMMMM')