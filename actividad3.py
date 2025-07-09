#Actividad
#punto 1

# notas=[]
# print(notas)
# not1=float(input("ingrese su nota: "))
# not2=float(input("ingrese su nota: "))
# not3=float(input("ingrese su nota: "))
# operacion=not1+not2+not3
# prom=operacion/3
# notas.append(not1)
# notas.append(not2)
# notas.append(not3)
# print(f"tu promedio es de {prom}, y la lista quedaria asi {notas}")

#punto 2

# producto={
#     "shampoo":300,
#     "crema":4000,
#     "locion":1200
# }
# print(producto)
# por=float(input("porcentaje y aumento: "))
# producto["shampoo"]+=producto["shampoo"]*(por/100)
# producto["crema"]+=producto["crema"]*(por/100)
# producto["locion"]+=producto["locion"]*(por/100)
# print(producto)

# punto 3

# temperatura=()
# temp1=float(input("ingresa una temperatura en grados c: "))
# temp2=float(input("ingresa una temperatura en grados c: "))
# temp3=float(input("ingresa una temperatura en grados c: "))
# temp4=float(input("ingresa una temperatura en grados c: "))
# temp5=float(input("ingresa una temperatura en grados c: "))
# lista=list(temperatura)
# lista.append(temp1)
# lista.append(temp2)
# lista.append(temp3)
# lista.append(temp4)
# lista.append(temp5)
# tupla=tuple(lista)
# faren1=temp1*9/5+32
# faren2=temp2*9/5+32
# faren3=temp3*9/5+32
# faren4=temp4*9/5+32
# faren5=temp5*9/5+32
# print(faren1)
# print(faren2)
# print(faren3)
# print(faren4)
# print(faren5)

#punto 4

# edades=[]
# print(edades)
# edad1=int(input("ingresa una edad: "))
# edad2=int(input("ingresa una edad: "))
# edad3=int(input("ingresa una edad: "))
# edad4=int(input("ingresa una edad: "))
# edad5=int(input("ingresa una edad: "))
# edades.append(edad1)
# edades.append(edad2)
# edades.append(edad3)
# edades.append(edad4)
# edades.append(edad5)
# prom=sum(edades)/len(edades)
# print(f"mayor: {max(edades)}, menor: {min(edades)}, promedio{prom}")

# punto 5 

# frutas={
#     "fresa": 2000,
#     "manzana": 3000,
#     "piña": 2000
# }
# print(frutas)
# pro1=float(input("ingrese el peso de la fruta:"))
# pro2=float(input("ingrese el peso de la fruta:"))
# pro3=float(input("ingrese el peso de la fruta:"))
# cant1=pro1*frutas["fresa"]
# cant2=pro2*frutas["manzana"]
# cant3=pro3*frutas["piña"]
# total=cant1+cant2+cant3
# print(f"el precio total es {total}, en total la fresa es {cant1}, el de la manzana es {cant2}, y el de la piña es {cant3}")

#punto 6

# tupla=(5,8,9,4,2)
# print(tupla)
# lista=list(tupla)
# operacion=tupla[0]+tupla[1]+tupla[2]+tupla[3]+tupla[4]
# print(operacion)
# print(f"el resultado es {operacion}")

#punto 7

# lista=[]
#  producto1={
#      "producto1": input("ingrese el nombre del producto"),
#      "cantidad": int("ingresa la cantidad que deseas"),
#      "precio": float("ingresa el valor del producto")
#  }
# lista.append(producto1)
#  print(producto1)

# lista=[]
#  producto2={
#      "producto1": input("ingrese el nombre del producto"),
#      "cantidad": int("ingresa la cantidad que deseas"),
#      "precio": float("ingresa el valor del producto")
#  }
# lista.append(producto2)
# print(producto2)

# lista=[]
# producto3={
#      "producto1": input("ingrese el nombre del producto"),
#      "cantidad": int("ingresa la cantidad que deseas"),
#      "precio": float("ingresa el valor del producto")
#  }
# lista.append(producto3)
# print(producto3)

# punto 8

# lista=[]
# print(lista)
# valor1=int(input("ingresa un valor con descuento del 20%: "))
# valor2=int(input("ingresa un valor con descuento del 15%: "))
# valor3=int(input("ingresa un valor con descuento  del 30%: "))
# valor4=int(input("ingresa un valor con descuento del 10%: "))
# valor5=int(input("ingresa un valor con descuento del 40%: "))
# lista.append(valor1)
# lista.append(valor2)
# lista.append(valor3)
# lista.append(valor4)
# lista.append(valor5)
# print(lista)
# descuento=valor1*0.20
# descuento2=valor2*0.15
# descuento3=valor3*0.30
# descuento4=valor4*0.10
# descuento5=valor5*0.40
# print(descuento)
# print(descuento2)
# print(descuento3)
# print(descuento4)
# print(descuento5)

#punto 9

# tupla=()
# print(tupla)
# lista=[]
# calificacion1=float(input("ingrese su nota: "))
# calificacion2=float(input("ingrese su nota: "))
# calificacion3=float(input("ingrese su nota: "))
# lista=list(tupla)
# lista.append(calificacion1)
# lista.append(calificacion2)
# lista.append(calificacion3)
# tupla=tuple(lista)
# print(lista)
# print(tupla)
# print(f"la nota mas bajita fue {min(tupla)}, y la nota mas alta fue {max(tupla)}")

#punto 10

# unidades={
#     "km": 1000,
#     "m": 1,
#     "cm": 0.01
# }
# num=float(input("ingresa el numero a convertir: "))
# uni=input("ingresa la cantidad(km, m, cm): ")
# metros=num*unidades.get(uni,0)
# print(f"{num} {uni} son iguales a {metros}")

#punto 11

# precios=float(input("ingresa el precio del primer producto: "))
# precios2=float(input("ingresa el precio del segundo producto: "))
# precios3=float(input("ingresa el precio del tercer producto: "))
# precios=[precios,precios2,precios3]
# precio_iva=[
#     precios[0]*1.19,
#     precios[1]*1.19,
#     precios[2]*1.19
# ]
# print(f"precio original:{precios}")
# print(f"precio con iva (19%): {precio_iva}")

#punto 12

# num1=float(input("ingresa un numero: "))
# num2=float(input("ingresa un numero: "))
# operacion=num1+num2
# operacion2=num1-num2
# operacion3=num1*num2
# operacion4=num1/num2
# total=(operacion,operacion2,operacion3,operacion4)
# print(operacion)
# print(operacion2)
# print(operacion3)
# print(operacion4)
# print(f"el resultado de las operaciones es {total}")

#punto 13

# estudiante={
#     "Danilo": 4.0,
#     "Ailyn": 5.0,
#     "Isabella": 3.5,
#     "Sharyk": 4.5,
#     "Laura": 3.0
# }
# promedio=sum(estudiante.values())/len(estudiante)
# print("diccionario de estudiantes: ",estudiante )
# print("promedio general: ", promedio)

#punto 14

# salario1=float(input("ingresa el primer salario: "))
# salario2=float(input("ingresa el segundo salario: "))
# salario3=float(input("ingresa el tercero salario: "))
# salario4=float(input("ingresa el cuarto salario: "))
# salario5=float(input("ingresa el quinto salario: "))
# salarios=[salario1,salario2,salario3,salario4,salario5]
# salario1_a=salario1*1.10
# salario2_a=salario2*1.10
# salario3_a=salario3*1.10
# salario4_a=salario4*1.10
# salario5_a=salario5*1.10
# salarios_aumentados=[salario1_a,salario2_a,salario3_a,salario4_a,salario5_a]
# print("salarios originales: ", salarios)
# print("salarios con aumento del 10%: ", salarios_aumentados)

#punto 15

