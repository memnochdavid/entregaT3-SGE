#FUNCIONES
#EJ01
def x01(lista) ->int:
    mayor=lista[0]
    for i in lista:
        if i>mayor:
            mayor=i
    return mayor
#EJ02
def x02(lista) ->str:
    suma=0
    devuelve=""
    for i in lista:
        devuelve+=f"{i}+"
        suma+=i
    devuelve=devuelve[:-1]
    devuelve+=f"={suma}"
    return devuelve
#EJ03
def x03(millas)->float:
    return millas*1.6
#EJ04
def x04(letra)->bool:
    vocales=["a","e","i","o","u"]
    if letra[0] in vocales:
        return True
    else:
        return False
#EJ05
def x05(nums)->list:
    devuelve=[]
    for i in nums:
        if i%2==0:
            devuelve.append(i)
    return devuelve
#EJ05
def x06(n, intervalo)->list:
    encontrados=[]
    i=intervalo[0]
    while i<=intervalo[1]:
        if i%n==0:
            encontrados.append(i)
        i+=1
    return encontrados








ej=int(input("Ejercicio a probar: "))
match(ej):
    case 1:
        '''Ejercicio 1. Crea una función que obtenga el máximo de una lista de números'''
        lista=[1,4,5,7,2,99]
        print(f"La lista es {lista}")
        print(f"El mayor número de la lista es {x01(lista)}")

    case 2:
        '''Ejercicio 2. Crea una función que obtenga la sumatoria de una lista de números'''
        lista=[2,5,7,8,1,7]
        print("")
        print(f"La lista es {lista}")
        print(f"La sumatoria de la lista es {x02(lista)}")

    case 3:
        '''Ejercicio 3. Crea una función que dada una distancia en millas calcule su correspondiente en kms.'''
        millas=int(input("Millas? "))
        print(f"{millas} millas = {x03(millas)} KM")

    case 4:
        '''Ejercicio 4. Crea una función que determina si una letra es una vocal'''
        seguir=True
        caracter=""
        while(seguir):
            caracter=str(input("Escribe un caracter a comprobar: "))
            if len(caracter)==1:
                seguir=False
            else:
                break;
        if x04(caracter):
            print(f"{caracter} es una vocal")
        else:
            print(f"{caracter} no es una vocal")

    case 5:
        '''Ejercicio 5. Crea una función que cuenta la cantidad de números pares de una lista de números.'''
        lista=[2,4,5,7,8,4,32,6,7,21]
        print(f"La lista de números es: {lista}")
        print(f"Los pares son: {x05(lista)}")

    case 6:
        '''Ejercicio 6. Crea una función que dados un número y un intervalo (inicio, fin) cuente la cantidad de 
        múltiplos del número en dicho intervalo'''
        interv=[]
        num=int(input("Número a comprobar: "))
        print("Ahora el intervalo...")
        interv.append(int(input("Comienza en: ")))
        interv.append(int(input("Termina en: ")))
        multiplos=x06(num, interv)
        if len(x06(num, interv))==0:
            print(f"No se han encontrado múltiplos en el intervalo [{interv[0]}-{interv[1]}].")
        else:
            print(f"Los múltiplos de {num} en el intervalo [{interv[0]}-{interv[1]}] son:\n{multiplos}")

    case 7:
        '''Ejercicio 7. Crea una función que dada la longitud de los tres lados de un triángulo determine 
        si el triangulo es rectángulo'''












