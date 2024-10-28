#<FUNCIONES>
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
#EJ06
def x06(n, intervalo)->list:
    encontrados=[]
    i=intervalo[0]
    while i<=intervalo[1]:
        if i%n==0:
            encontrados.append(i)
        i+=1
    return encontrados
#EJ07
def x07(lados)->bool:
    lado_mayor=lados[0]
    for i in lados:
        if(lado_mayor<i):
            lado_mayor=i
            lados.remove(i)
    if(lados[0]^2+lados[1]^2==lado_mayor^2):
        return True
    else:
        return False
#EJ08
def x08(a,b)->int:
    respuesta=True
    mcd=0
    if a<b:
        for i in range(2,a):
            if(a%i==0 and b%i==0):
                mcd=i
    elif b<a:
        for i in range(2,b):
            if(a%i==0 and b%i==0):
                mcd=i
    return mcd
#EJ09
def x09(n)->str:
    devuelve=""
    for i in range(1,n+1):
        for j in range(0,i):
            devuelve+=str(i)
        devuelve+="\n"
    return devuelve

#EJ10
def x10(n)->str:
    devuelve = ""
    espacio=" "
    #parte de arriba
    for i in range(1,n+1):
        for j in range(1,(n+1) - i):
            devuelve+=" "
        for j in range(1,i):
            devuelve+="*"
        for j in range(1,i+1):
            devuelve+="*"

        devuelve+="\n"

    #parte de abajo
    for i in range(n,0,-1):
        for j in range(1,(n+1) - i):
            devuelve+=" "
        for j in range(1, i):
            devuelve += "*"
        for j in range(1, i + 1):
            devuelve += "*"

        devuelve += "\n"
    return devuelve
#</FUNCIONES>

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
        a = int(input("Lado A: "))
        b = int(input("Lado B: "))
        c = int(input("Lado C: "))
        lados=[a,b,c]
        if x07(lados):
            print("El triángulo es rectángulo.")
        else:
            print("El triángulo no es rectángulo.")

    case 8:
        '''Ejercicio 8. Crea una función que calcule el máximo común divisor de dos números
        naturales'''
        a = int(input("Número A: "))
        b = int(input("Número B: "))
        print(f"El MCD de {a} y {b} es: {x08(a,b)}")

    case 9:
        '''Ejercicio 9. Crea una función que dado un número n imprima los siguientes
        ‘mosaicos’:
        Por ejemplo para n = 6:
        1
        22
        333
        4444
        55555
        666666  '''
        num = int(input("Número: "))
        print(x09(num))

    case 10:
        '''Ejercicio 10. Crea una función que imprima un mosaico rombo de anchura variable. '''
        num = int(input("Número: "))
        print(x10(num))







