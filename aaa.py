#Damos por conocidas las variables y sus valores
#Valores distancia A
x1=0
y1=0
z1=0
#Valores distancia B
x2=0
y2=0
z2=0
#Valor distancia total
d=0
#Iniciamos preguntando los valores que el usuario quiera asignar para cada distancia
print("Bienvenido, te ayudare a determinar la distancia entre dos puntos en el espacio :D")
print("Iniciaremos con el Punto A")
x1=int(input("Ingresa el valor de distancia de X:\n"))
y1=int(input("Ingresa el valor de distancia de Y:\n"))
z1=int(input("Ingresa el valor de profundidad en el espacio (Z):\n"))
print("Gracias, Seguimos con los valores del punto B")
x2=int(input("Ingresa el valor de distancia de X:\n"))
y2=int(input("Ingresa el valor de distancia de Y:\n"))
z2=int(input("Ingresa el valor de profundidad en el espacio (Z):\n"))
##Ahora con los valores guardados para cada punto procedemos con el calculo
d = ((x2-x1)**2 +(y2-y1)**2+(z2-z1)**2)**0.5
#mprimemos el resultado
print("La distancia entre el punto A y el punto B es:", d )