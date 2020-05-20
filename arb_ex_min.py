#Este programa realizara el metodo simplex para redes
#empezaremos por capturar el grafo 
#importante tener numpy instalado, sino instalar desde terminal
#por error de visual estudio code el import de numpy seguira marcando error aunque funcione bien
import numpy as np
import math


def arbol_exp_minima():
    num_nodos=int(input("Dame la candidad de nodos de tu grafo: "))
    
    #Ascii de 65(A) a 90(Z) chr(65)=A


    red=np.ones((num_nodos,num_nodos)) #Se crea una matriz de incidencia de nxn con 10**8  en cada espacio
    
    aristas= np.ones((num_nodos**2,3))
    aristas_modificaciones=np.ones((num_nodos**2,3))
    print(f"Nombremos a tus nodos desde A hasta {chr(64+num_nodos)};\n")

    print("Procederemos a llenar tus aristas, AB quiere decir que pregunto por el \n"
        "precio de ir de A a B. Es importante notar que AB no es lo mismo que BA en un grafo dirigido\n\n"
        "0 representa que no tiene costo mientras que None representa que no hay camino de A a B\n"
        "Si precionas enter sin dejar un valor se pondra None automaticamente y se entendera que no hay camino")
    n=0
    for i in range(num_nodos):
        for j in range(num_nodos):
            try:
                red[i,j]=input((f"Valor de {chr(65+i)} a {chr(65+j)}: "))
                aristas[n,0]=65+i
                aristas[n,1]=red[i,j]
                aristas[n,2]=65+j

            except:
                red[i,j]= 10**8
                aristas[n,0]=65+i
                aristas[n,1]=10**8
                aristas[n,2]=65+j
            n=n+1



            print("\n")



    lista_nodos = np.array(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
                    'S','T','U','V','W','X','Y','Z'])
    print("Tu matriz de incidencia es: ")
    print(f"  {lista_nodos[0:num_nodos]}")
    for i in range(num_nodos):
        print(f"{chr(65+i)} {red[i,0:]}") 

    for i in range(n):
        print(chr(int(aristas[i,0])),aristas[i,1], chr(int(aristas[i,2])))
    aristas_modificaciones=aristas
    
    metodo2(red, aristas_modificaciones)

    






def metodo2(matriz, lista_modificaciones):
    print("Metodo del arbol de expansion minima")
    #print(matriz)
    
    print(lista_modificaciones)
    
    #lista de nodos que no pertene aun al grafo final
    n= int(math.sqrt(matriz.size)) 
    arbol_minimo=np.ones((n,n))
    for i in range(n):
        for j in range(n):
            arbol_minimo[i,j]=10**8
    no_final=np.ones((1, n ))
    menor=[]
    minimo=10**8
    for i in range(n):
        no_final[0,i]=65+i
    #lista de nodos que ya pertenecen al grafo final
    si_final=[]
    index=10**8
    nodo_valido=0

    
    while (int(no_final.sum()) != n):#mientras existan nodos sueltos (o sea no se encuentren en el grafo final)
                                #el programa seguira buscando la siguiente mejor arista que complete el arbol
        for i in range(matriz.size):#valida si los nodos que una la arista ya estan contemplados en el arbol final
            for j in range(len(si_final)):
                if (lista_modificaciones[i,0] == si_final[j]):
                    nodo_valido=nodo_valido+1
                if (lista_modificaciones[i,2] == si_final[j]):
                    nodo_valido=nodo_valido+1
            print(f"nodo valido vale {nodo_valido}")
            if(nodo_valido==2):
                lista_modificaciones[i,1]=10**8 #si ambos nodos ya estan en el arbol entonces la arista ya no es relevante
            nodo_valido=0                           #y podemos igualarla a M (10**8) 
        minimo=10**8
        menor=[]
        index=10**8
        for i in range(matriz.size):
            if (lista_vacia(si_final)==True):
                menor.append(lista_modificaciones[i,1])
            else:
                for j in range(len(si_final)):
                    if (lista_modificaciones[i,0]==si_final[j] or lista_modificaciones[i,2]== si_final[j]):
                        menor.append(lista_modificaciones[i,1])

        minimo=min(menor)
        print(minimo)
        
        for i in range(matriz.size):
            print(f"minimo= {minimo}")
            print(f"tiene que ser igual a {lista_modificaciones[i,1]}")
            if (minimo==lista_modificaciones[i,1]):
                if (lista_vacia(si_final)==True):
                    index=i
                else:
                    for j in range(len(si_final)):
                        if (lista_modificaciones[i,0]==si_final[j] or lista_modificaciones[i,2]== si_final[j]):
                            index=i


        if (index==10**8):
            print("Algo salio muy mal  CORREEEEE")#significaria que aun no se conecta todo el arbol pero ya no hay aristas factibles
        arbol_minimo[(int(lista_modificaciones[index,0])-65), (int(lista_modificaciones[index,2])-65)]=float(lista_modificaciones[index,1])
        si_final.append(lista_modificaciones[index,0])
        si_final.append(lista_modificaciones[index,2])
        lista_modificaciones[index,1]=10**8
        for k in range(n):
            if (int(no_final[0,k])==int(lista_modificaciones[index,0])):
                no_final[0,k]=1
            if (int(no_final[0,k])==int(lista_modificaciones[index,2])):
                no_final[0,k]=1


        si_final=list(set(si_final))
        print("Iniciamos el rellenado de la matriz\n\n\n\n")
        print("matriz")
        print(arbol_minimo)
        print("nodos finales")
        for i in range(len(si_final)):
            print(chr(int(si_final[i])))
        print("nodos no finales")
        print(no_final)
    
        print(f"la condicion se rompe cuando {int(no_final.sum())} ={n}")

    print("Matriz final\n\n\n\n")
    print(arbol_minimo)
    for i in range(len(si_final)):
        print(chr(int(si_final[i])))
    print(no_final)
    print(f"lista modificaciones\n {lista_modificaciones}")
    lista_nodos = np.array(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
                    'S','T','U','V','W','X','Y','Z'])
    z=0
    contador=0
    for i in range(n):
        for j in range(n):
            if (arbol_minimo[i,j] == 10**8):
                contador=contador+1

    matriz_imp=np.full((n,n),"espero_funcione_lo_que_voy_a_intentar")
    for i in range(n):
        for j in range(n):
            if (matriz[i,j] ==10**8):
                matriz_imp[i,j]="X"
            else:
                matriz_imp[i,j]=str(matriz[i,j])

    print("Tu matriz de incidensia inicial es:\n")
    print(f"  {lista_nodos[0:n]}")
    for i in range(n):
        print(f"{chr(65+i)} {matriz_imp[i,0:]}")

    z=arbol_minimo.sum()-(contador*(10**8))
    arbol_minimo_imp=np.full((n,n),"espero_funcione_lo_que_voy_a_intentar")
    for i in range(n):
        for j in range(n):
            if (arbol_minimo[i,j] == 10**8):
                arbol_minimo_imp[i,j]="X"
            else:
                arbol_minimo_imp[i,j]=str(arbol_minimo[i,j])

    print("Resultado final, arbol de expansion minida del grafo:\n")
    print(f"  {lista_nodos[0:n]}")
    for i in range(n):
        print(f"{chr(65+i)} {arbol_minimo_imp[i,0:]}")

    print(f"Z={z}")


            
def lista_vacia(lista_1):
    return not lista_1
#arbol_exp_minima()
