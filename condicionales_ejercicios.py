# fruta=[]
# print(fruta)
# fru1=input("ingresa una fruta: ")
# fru2=input("ingresa una fruta: ")
# fru3=input("ingresa una fruta: ")
# fruta.append(fru1)
# fruta.append(fru2)
# fruta.append(fru3)
# print(fruta)

# edades=[]
# print(edades)
# edad1=input("ingresa la edad de tu mama")
# edad2=input("ingresa la edad de tu papa")
# edad3=input("ingresa tu eddad")
# edades.append(edad1)
# edades.append(edad2)
# edades.append(edad3)
# print(edades)

# notas=[]
# print(notas)
# not1=float(input("ingresa un numero decimal: "))
# not2=float(input("ingresa un numero decimal: "))
# not3=float(input("ingresa un numero decimal: "))
# not4=float(input("ingresa un numero decimal: "))
# notas.append(not1)
# notas.append(not2)
# notas.append(not3)
# notas.append(not4)
# print(notas)

# productos=[]
# print(productos)
# pro=input("ingresa lo que te hace falta: ")
# pro2=input("ingresa lo que te hace falta: ")
# pro3=input("ingresa lo que te hace falta: ")
# productos.append(pro)
# productos.append(pro2)
# productos.append(pro3)
# print(productos)

# precios=[]
# print(precios)
# pre=float(input("ingresa el precio de un producto: "))
# pre2=float(input("ingresa el precio de un producto: "))
# pre3=float(input("ingresa el precio de un producto: "))
# precios.append(pre)
# precios.append(pre2)
# precios.append(pre3)
# print(precios)

# numeros=[]
# print(numeros)
# pre=float(input("ingresa un numero: "))
# pre1=float(input("ingresa un numero: "))
# pre2=float(input("ingresa un numero: "))
# pre3=float(input("ingresa un numero: "))
# numeros.append(pre)
# numeros.append(pre1)
# numeros.append(pre2)
# numeros.append(pre3)
# print(numeros)
# print("el numero mayor es : ", max(numeros))
# print("el numero mayor es : ", min(numeros))

# nombres=[]
# print(nombres)
# nom1=input("ingresa un nombre: ")
# nom2=input("ingresa un nombre: ")
# nombres.append(nom1)
# nombres.append(nom2)
# print(nombres)
# print(f"hola, {nombres[0]}")

# temperaturas=[]
# print(temperaturas)
# tem1=float(input("ingresa la temperatura: "))
# tem2=float(input("ingresa la temperatura: "))
# operacion=tem1*1.8 + 32
# operacion1=tem2*1.8 +32
# temperaturas.append(operacion)
# temperaturas.append(operacion1)
# print(temperaturas)
#********************************************************************
#EJERCICIOS CONDICIONALES
#********************************************************************
#ejercicio 1
# num=float(input("ingresa un numero: "))
# if num < 0:
#     print(f"{num} el numero es negativo")
# elif num > 0:
#     print(f"{num} el numero es positivo")
# else:
#     print("el numero es cero")

# ejercicio 2
# num=float(input("ingresa un numero: "))
# num1=float(input("ingresa un numero: "))
# if num < num1:
#     print(f"{num} es menor que {num1}")
# elif num > num1:
#     print(f"{num} es mayor que {num1}")
# else:
#     print("los dos numero soon iguales")

#ejercicio 3
# num=float(input("ingresa un numero: "))
# if num % 2 ==0:
#     print(f"{num} es par")
# else:
#     print(f"{num} no es par")

# ejercicio 4
# num=float(input("ingresa un numero: "))
# if num >= 10 and num <= 20:
#     print(f"{num} esta en el rango")
# else:
#     print(f"{num} no esta en el rango")

#ejercicio 5
# num=int(input("ingresa un numero: "))
# num2=int(input("ingresa un numero: "))
# num3=int(input("ingresa un numero: "))
# if num >= num2 and num2 <= num3:
#     print(f"{num}es mayor que {num2}")
# elif num2>num and num2 >= num3:
#     print(f"el menor es {num2}")
# else:
#     print(f"el mayor es {num3}")

# #elercicio 6
# val=float(input("ingresa el cuanto se te fue en la compra: "))
# if val >= 100:
#     oper=val*0.10
#     opera=val-oper
#     print(f"si se le hace descuento el valor de la cmpra seria {opera}")
# else:
#     print(f"a esta compra no se le aplico el descuento")

#ejercico 7
# años=int(input("ingrea tu edad: "))
# if años >=18:
#     print("eres mayor de edad, puedes votar")
# else:
#     print("eres menor de edad, no puedes votar")

#ejercicio 8
# valor=float(input("cuanto se te fue en la compra: "))
# cliente=input("que tipo de cliente eres: ")
# if cliente== "VIP":
#     des=valor*0.20
#     total=valor-des
#     print("por ser VIP se le realiza un descuento")

#ejercicio 9
# num=int(input("ingresa un numero: "))
# if num % 5 == 0 and num % 3 == 0:
#     print("el numero no es multiplo de 5 y de 3 al mismo tiempo")
# else:
#     print("el numero no es multiplo de ninguno de los dos numeros")

#ejercicio 10
# num=int(input("ingresa un numero:"))
# if num % 2 == 0:
#     print("el numero es divisible entre dos")
# else:
#     print("el numero no es divisible entre dos")

#ejercicio 11
# num=[4,12,15,8,3]
# if num[2] > 10:
#     print("mayor a 10")
# else:
#     print("manor o igual a 10")

#ejercico 12
# lis=[3,5,7,9]
# if 7 in lis:
#     print("esta en la lista")
# else:
#     print("no esta en la lista")

#ejercicio 13
# lis=[4,6,2,8]
# operacion= lis[0]+lis[1]
# if operacion > 10:
#     print("suma alta")
# else:
#     print("suma baja")

#ejercisio 14
# nom=["Ailyn","Camila","Samantha","Danilo"]
# ultimo=nom[-1]
# print("ultimo nombre:", ultimo)
# if ultimo == "Danilo":
#     print("nombre correcto")
# else:
#     print("nombre diferente")

#ejercicio 15
# color=["rojo","azul","verde"]
# if color [1]== "azul":
#     color[1]= "amarillo"
#     print("lista actualizada:", color)

#ejercicio 16
# tupla=(5,8,12,20)
# if tupla[0]<tupla[-1]:
#     print("orden ascendente")
# else:
#     print("orden descendente")

#ejercicio 17
# tupla=(25,32,28)
# if tupla[1]>30:
#     print("edad mayor a 30")
# else:
#     print("edad menor o igual a 30")

#ejercicio 18
# tupla=(1,2,3)
# lista=list(tupla)
# if lista[1]==2:
#     lista[1]=10
# nueva_tupla=tuple(list)
# print("nueva tupla:", nueva_tupla)
# #ejercicio 19
# tupla=(4,9)
# valor=tupla[1]
# if valor>5:
#     print("coordenada alta")
# else:
#     print("coordenada baja")

#ejercicio 20
# tupla=(3,4)
# tupla1=(3,5)
# if tupla==tupla1:
#     print("tuplas iguales")
# else:
#     print("tuplas diferentes")

#ejercicio 21
# person={"nombre":"Lusia", "edad": 17}
# if person ["edad"]>=18:
#     print("Adulto")
# else:
#     print("menor edad")

#ejercicio 22
# person={"nombre":"Lucia","edad":20}
# if person["edad"]>18:
#     person["edad"]=21
#     print("diccionario actualizado:", person)

#ejercicio 23
# person={"nombre":"Carlos"}
# if "ciudad" not in person:
#     person["ciudad"]= "Bogota"
# print("diccionario con ciudad:", person)

#ejercicio 24
# producto={"producto":"pan","precio":1200}
# if "precio" in producto:
#     print("precio:", producto["precio"])
# else:
#     print("no hay precio")

#ejercicio 25
# inventario={"pan":1200, "leche":2000}
# if "pan" in inventario:
#     print("precio del pan:",inventario["pan"])
# else:
#     print("producto no disponible")´{}