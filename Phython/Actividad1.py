from random import randint
listavacia = [randint(1, 9) for _ in range(10)]#Generación de la lista inicial

for i in range(7):
    listavacia.append(i+1)
print(listavacia) 

for x in range (len(listavacia)):#numero total de elementos
    for z in range(0, len(listavacia)-x-1):#Comprueba lista de rangos
        if listavacia[z] > listavacia [z+1]:
            listavacia[z], listavacia[z+1] = listavacia[z+1], listavacia[z]

print(listavacia)
print(listavacia[::-1])
            
#Cambiar el valor de 2 variables?