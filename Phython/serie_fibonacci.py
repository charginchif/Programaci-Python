def a(n):#Define una variable llamada a
    if n <= 1:#Comprueba que  si n es 0 o 1
        return n #En caso de que si te regresa 0 o 1
    else:
        return a(n-1) + a(n-2)#Este calcula mediante recurcion llama a a y por medio de la funcion va llamando los datos 
                                #mientras los descompone en 2 numeros que se van agegando a la lista hasta llegar 1

n = int(input("Dame un numero a continuacion: "))  # Pide un número a ingresar
R = [a(i) for i in range(n+1)]  #Genera los primeros términos utilizando la función 
print(R)  #Imprime la lista 


#Explicacion de () y []
#El () es para una lista pero no es cambiable ni modificable(tuplas)
#Sireve para sepra operaciones

#Mientras que el [] si se puede cambiar y modificar
#Son mejores para hacer listas