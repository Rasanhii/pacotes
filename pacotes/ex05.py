while True:
    try:    
        numero = int(input('Entre com um número: '))
        print(5/numero)
        break
    except ValueError:
        print('Valor errado')
    except ZeroDivisionError:
        print('Desculpe não posso dividir por zero')
    except:
        print('EXPLOÇÃOOOOOOOOOOOOOOOOOO BOOOOOMMMM')