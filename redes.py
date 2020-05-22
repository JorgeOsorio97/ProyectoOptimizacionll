#Este programa realizara el metodo simplex para redes
#empezaremos por capturar el grafo 
#importante tener numpy instalado, sino instalar desde terminal
#por error de visual estudio code el import de numpy seguira marcando error aunque funcione bien

import pdb       #   pdb.set_trace()   es el debogger de python
import numpy as np
import math

def simplex_redes():
    num_nodos=int(input("Dame la candidad de nodos de tu red: "))
    
    #Ascii de 65(A) a 90(Z) chr(65)=A


    red=np.ones((num_nodos,num_nodos))#Se crea una matriz de adyacencia de nxn con costos c_ij
    
    red_minima=np.ones((num_nodos,num_nodos)) 
    red_iteracion_x=np.ones((num_nodos,num_nodos))#costos calculados x_ij
    red_iteracion_c=np.ones((num_nodos,num_nodos))#costos c_ij de iteracion que se ocupan esa iteracion
    red_iteracion_z=np.ones((num_nodos,num_nodos))
    indices_ecuaciones=np.ones((num_nodos-1,3))

    aristas=np.ones(((num_nodos)**2,3))
    aristas_c=np.ones(((num_nodos)**2,3))

    w_i=np.ones((num_nodos,1))
    indices_ecuaciones=np.empty((num_nodos-1,3))
    
    nodo_ofe_dem=[]   #demandas y productos de nodos (b_i)
    print(f"Nombremos a tus nodos desde A hasta {chr(64+num_nodos)};\n"
        f"A sera tu nodo de salida y {chr(64+num_nodos)} sera tu nodo destino\n")

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
            
    #red[num_nodos,num_nodos]=10**8
    #lista_nodo_artificial=np.full((num_nodos+1,3), 10**8)

    print("ahora dame la demanda o la oferta de cada nodo\n")
    for i in range(num_nodos):
        nodo_ofe_dem.append(input((f"valor del nodo {chr(65+i)}: \n")))
        #if(int(nodo_ofe_dem[i])==0):
         #   lista_nodo_artificial[i,0]=65+i
          #  lista_nodo_artificial[i,1]=10**8
           # lista_nodo_artificial[i,2]=64
       # if(int(nodo_ofe_dem[i])>0):
        #    lista_nodo_artificial[i,0]=65+i
         #   lista_nodo_artificial[i,1]=int(nodo_ofe_dem[i])
          #  lista_nodo_artificial[i,2]=64
        #elif (int(nodo_ofe_dem[i])<0):
         #   lista_nodo_artificial[i,2]=65+i
          #  lista_nodo_artificial[i,1]=int(nodo_ofe_dem[i])*(-1)
           # lista_nodo_artificial[i,0]=64
    #lista_nodo_artificial[num_nodos,0]=64
    #lista_nodo_artificial[num_nodos,1]=0
    #lista_nodo_artificial[num_nodos,2]=63

    b_n=0
    for i in range(len(nodo_ofe_dem)):
        b_n=b_n+int(nodo_ofe_dem[i])
    if (b_n != 0):
        print("El grafo no esta balanceado")
    print("Funcion objetivo: \n")
    funcion=[]
    for i in range(num_nodos**2):
        if (aristas[i,1] !=10**8):
            if (lista_vacia(funcion)==True):
                funcion.append(f"({(aristas[i,1])*(-1)}X_{chr(int(aristas[i,0]))}{chr(int(aristas[i,2]))})")
            else:
                funcion.append(f"+({(aristas[i,1])*(-1)}X_{chr(int(aristas[i,0]))}{chr(int(aristas[i,2]))})")
     

    lista_nodos = np.array(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
                    'S','T','U','V','W','X','Y','Z'])
    print("Tu matriz de adyasencia es: ")
    print(f"  {lista_nodos[0:num_nodos]}")
    for i in range(num_nodos):
        print(f"{chr(65+i)} {red[i,0:]}") 

    for i in range(n):
        print(chr(int(aristas[i,0])),aristas[i,1], chr(int(aristas[i,2])))
    
    print(f"Minizar z={funcion}")
    

    aristas_c=aristas.copy()
    red_iteracion_c=red.copy()
    
    con=0
    for i in range(num_nodos):
        for j in range(num_nodos):
            if (red_iteracion_c[i,j] != 10**8):
                if(int(nodo_ofe_dem[i]) <0 ):
                    if(int(nodo_ofe_dem[j])>0):#eliminamos la linea
                        
                        red_iteracion_c[i,j]=10**8
                        aristas_c[con,0]=65+i
                        aristas_c[con,1]=10**8
                        aristas_c[con,2]=65+j
            con=con+1
    







        



                    
    
    red_minima=metodo2(red_iteracion_c, aristas_c)
    
    
    for i in range(num_nodos):
        for j in range(num_nodos):
            red_iteracion_x[i,j]=10**8

    
    red_iteracion_c=red_minima.copy()
    

    nodos_hojas_raices=np.ones((num_nodos,2))# (num nodos que manda, num nodos que recibe)
    manda=0
    recibe=0
    cos_red_pos=0
    #n_h=0
    
    print(red_minima)
    print("Definimos que nodos son hojas y que nodos son de transicion")
    for i in range(num_nodos):
        manda=0
        recibe=0
        for j in range(num_nodos):
            
            
            if(red_iteracion_c[i,j] != 10**8):
                manda=manda+1
            nodos_hojas_raices[i,0]=manda
            
        for k in range(num_nodos):
            if (red_iteracion_c[k,i] != 10**8):
                recibe=recibe+1 
            nodos_hojas_raices[i,1]=recibe    
                                        
        
    
    print("Llenamos la matriz de x_ij con los costos de demanda y oferta")
    print("nodos hojas")
    print(nodos_hojas_raices)
    #pdb.set_trace()
    for i in range(num_nodos):
        if((nodos_hojas_raices[i,0]+nodos_hojas_raices[i,1]) == 1):
            if (int(nodo_ofe_dem[i])<0):
                for s in range(num_nodos):
                    if (red_iteracion_c[s,i]!=10**8):
                        red_iteracion_x[s,i]=int(nodo_ofe_dem[i])*(-1)
            elif(int(nodo_ofe_dem[i])>0 and nodos_hojas_raices[i,0]==1):
                for s in range(num_nodos):
                    if (red_iteracion_c[i,s] != 10**8):
                        red_iteracion_x[i,s]=int(nodo_ofe_dem[i])
        else:
            flujo=0
            aristas_temporales=[]
            for s in range(num_nodos):
                if (red_iteracion_x[s,i]!=10**8):
                    flujo = flujo + red_iteracion_x[s,i]
            flujo=flujo + int(nodo_ofe_dem[i])
            if (flujo>=0):

                if(nodos_hojas_raices[i,0]!=0):
                    for j in range(int(nodos_hojas_raices[i,0])-1):
                        aristas_temporales.append(int(flujo/nodos_hojas_raices[i,0]))
                    aristas_temporales.append(int(flujo/nodos_hojas_raices[i,0])+flujo%nodos_hojas_raices[i,0])
                    ar=0
                for k in range(num_nodos):
                    if(red_iteracion_c[i,k] != 10**8):
                        
                        red_iteracion_x[i,k]=aristas_temporales[ar]
                        ar=ar+1
    it=0
    
    while(cos_red_pos==0):
        it=it+1
        z_i=0
        funcion_i=[]
        for i in range(num_nodos):
            for j in range(num_nodos):
                if (red_iteracion_c[i,j] != 10**8):
                    z_i=z_i+(red_iteracion_c[i,j]*red_iteracion_x[i,j])
                    if (lista_vacia(funcion_i)==True):
                        funcion_i.append(f"({red_iteracion_c[i,j]})*({red_iteracion_x[i,j]})")
                    else:
                        funcion_i.append(f"+({red_iteracion_c[i,j]})*({red_iteracion_x[i,j]})")
                    

                    

                    


        print(f"z={funcion_i}\n Z={z_i}")

        print("Calculamos las variables W_i")
        
         #se llena segun las aristas que participen en el arbol
        for i in range(num_nodos-1):
            indices_ecuaciones[i,0]=10**8
            indices_ecuaciones[i,1]=10**8
            indices_ecuaciones[i,2]=10**8

        counter = 0
        for i in range(num_nodos):
            for j in range(num_nodos):
                
                if (red_iteracion_c[i,j] != 10**8):
                    print(f"w_{i}-w_{j}={red_iteracion_c[i,j]}")
                    indices_ecuaciones[counter,0]=i           #0-1=2 subindices para resolver el sistema
                    indices_ecuaciones[counter,1]=j
                    indices_ecuaciones[counter,2]=red_iteracion_c[i,j] #guardamos una referencia de que 
                    print(indices_ecuaciones[i,0:])  
                    print(f"w_{i}-w_{j}={red_iteracion_c[i,j]}")  
                    counter += 1
                
                                  
        print("indices ecuaciones\n ") 
        print(indices_ecuaciones)                                      #w_i - w_j=c_ij    #lo que nos deja guardar las ecuaciones
        for i in range(num_nodos):#llenamos de M los valores de w_i
            w_i[i,0]=10**8
                                                            
        w_i[num_nodos-1,0]=0 #hacemos que el nodo w_k = 0 para poder resolver el sistema de ecuaciones
        w_lleno=0
        while(w_lleno!=1):#hasta que en w_1 ya no queden M por resolver no deja de resolver las ecuaciones
            for i in range(num_nodos):
                if (w_i[i,0] != 10**8):
                    for j in range(num_nodos-1):
                       
                        if (indices_ecuaciones[j,0] == i):
                            if (w_i[int(indices_ecuaciones[j,1]),0] == 10**8):
                                w_i[int(indices_ecuaciones[j,1]),0] =w_i[i,0]-indices_ecuaciones[j,2]

                        if (indices_ecuaciones[j,1]==i):
                            if (w_i[int(indices_ecuaciones[j,0]),0] == 10**8):
                                w_i[int(indices_ecuaciones[j,0]),0]=indices_ecuaciones[j,2]+w_i[i,0]
                                
                           
                            
            w_lleno=1
            for i in range(num_nodos):
                if(w_i[i,0]==10**8):
                    w_lleno=0
            #Procederemos a calcular la matriz  Z_ij (costos reducidos)
            #  para saber si se necesita otra iteracion
        
        cos_red_pos=1
        z_maxima=[]
        maximo_z=0
        nodo_productor=10**8
        nodo_destino=10**8
        for i in range(num_nodos): #vaciamos la matriz por iteraciones anteriores
            for j in range(num_nodos):
                red_iteracion_z[i,j]=10**8
        for i in range(num_nodos): #llenamos la matriz con los arcos que no pertenecen a la matriz C_ij
            for j in range(num_nodos):
                if (red[i,j]==red_iteracion_c[i,j]):
                    red_iteracion_z[i,j]=0
                else:
                    red_iteracion_z[i,j]= w_i[i,0]-w_i[j,0]-red[i,j]
                    z_maxima.append(red_iteracion_z[i,j])
                    if (red_iteracion_z[i,j]>0):
                        cos_red_pos=0
        #pdb.set_trace()
        

                    #asignamos los costos reducidos y verificamos si existen costos reducidos positivos
        if (cos_red_pos==0):#ya que aun no se llega a la z minima procedemos a calcular 
                               #la solucion inicial de la nueva iteracion
            maximo_z=max(z_maxima)
            for i in range(num_nodos):
                for j in range(num_nodos):
                    if (red_iteracion_z[i,j]==maximo_z):#coordenadas de la nueva arista basica
                        nodo_productor=i
                        nodo_destino=j # son importantes para balancear el problema
            delta=10**7 #inicializo a delta en M pero una M diferente
            #agrego el arco a la base
            #determino que arco abandona la base
            
            #hay que buscar que aristas y nodos forman el bucle al agregar el nuevo nodo a la base
            nodos_bucle=[]
            nodos_bucle.append(nodo_destino)
            
            nodo_temporal=nodo_destino
            exceso=0
            while(nodo_temporal != nodo_productor):
                for i in range(num_nodos):
                    
                    if(red_iteracion_c[i, nodo_temporal] != 10**8):
                        nodos_bucle.append(i)
                        nodo_temporal=i

                exceso=exceso+1
                if (exceso==num_nodos**2):
                    nodos_bucle.append(nodo_productor)
                    nodo_temporal=nodo_productor
                    

                
            
            
           
            nodos_bucle=nodos_bucle[::-1]
            x_minima=[]
            minimo_x=0
            for i in range(len(nodos_bucle)-1):
                x_minima.append(red_iteracion_x[i,(i+1)])
            minimo_x=min(x_minima)
            arista_en_bucle=0
            arista_i_sale=10**8
            arista_j_sale=10**8
            #buscamos la arista minima que saldra de la base
            for i in range(num_nodos):
                for j in range(num_nodos):
                    for k in range(len(nodos_bucle)):
                        if (i==nodos_bucle[k] and j==nodos_bucle[k]):
                            arista_en_bucle=1
                    if(minimo_x==red_iteracion_x[i,j] and arista_en_bucle==1 ):
                        delta=red_iteracion_x[i,j]
                        arista_i_sale=i
                        arista_j_sale=j
            nodo_temporal=nodo_destino
            exceso=0
            ultimo_nodo=np.ones((1,2))
            while(nodo_temporal != nodo_productor):
                for i in range(num_nodos):
                    if(red_iteracion_c[i, nodo_temporal] != 10**8):
                        red_iteracion_x[i,nodo_temporal]=red_iteracion_x[i,nodo_temporal]-delta
                        ultimo_nodo[0,0]=i
                        ultimo_nodo[0,1]=nodo_temporal
                exceso=exceso+1
                if (exceso==num_nodos**2):
                    red_iteracion_x[int(ultimo_nodo[0,0]),nodo_productor]=red_iteracion_x[int(ultimo_nodo[0,0]),nodo_productor]+delta
                    nodo_temporal=nodo_productor

            #ya solo falta sacar la arista de la base y meter la nueva a la base
            red_iteracion_x[arista_i_sale,arista_j_sale]=10**8
            red_iteracion_c[arista_i_sale,arista_j_sale]=10**8
            red_iteracion_x[nodo_productor,nodo_destino]=delta
            red_iteracion_c[nodo_productor,nodo_destino]=red[nodo_productor,nodo_destino]


    red_iteracion_x_impresion=np.full((num_nodos,num_nodos),"___________")
    red_iteracion_c_impresion=np.full((num_nodos,num_nodos),"___________")
    red_iteracion_z_impresion=np.full((num_nodos,num_nodos),"___________")
    red_impresion=np.full((num_nodos,num_nodos),"___________")

    for i in range(num_nodos):
        for j in range(num_nodos):
            if (red_iteracion_x[i,j] != 10**8):
                red_iteracion_x_impresion[i,j]=red_iteracion_x[i,j]
            else:
                red_iteracion_x_impresion[i,j]="X"

            if (red_iteracion_c[i,j] != 10**8):
                red_iteracion_c_impresion[i,j]=red_iteracion_c[i,j]
            else:
                red_iteracion_c_impresion[i,j]="X"

            if (red_iteracion_z[i,j] != 10**8):
                red_iteracion_z_impresion[i,j]=red_iteracion_z[i,j]
            else:
                red_iteracion_z_impresion[i,j]="X"
            
            if (red[i,j] != 10**8):
                red_impresion[i,j]=red[i,j]
            else:
                red_impresion[i,j]="X"
    z_i=0
    funcion_i=[]
    for i in range(num_nodos):
        for j in range(num_nodos):
            if (red_iteracion_c[i,j] != 10**8):
                z_i=z_i+(red_iteracion_c[i,j]*red_iteracion_x[i,j])
            if (lista_vacia(funcion_i)==True):
                funcion_i.append(f"({red_iteracion_c[i,j]})*({red_iteracion_x[i,j]})")
            else:
                funcion_i.append(f"+({red_iteracion_c[i,j]})*({red_iteracion_x[i,j]})")
                



    print(red)
    print("\nTu matriz de adyasencia era: ")
    print(f"  {lista_nodos[0:num_nodos]}")
    for i in range(num_nodos):
        print(f"{chr(65+i)} {red_impresion[i,0:]}")
    print("Tu matriz de costos (C_ij) es: ")
    print(f"  {lista_nodos[0:num_nodos]}")
    for i in range(num_nodos):
        print(f"{chr(65+i)} {red_iteracion_c_impresion[i,0:]}")
    print("Tu matriz de flijo (X_ij) es: ")
    print(f"  {lista_nodos[0:num_nodos]}")
    for i in range(num_nodos):
        print(f"{chr(65+i)} {red_iteracion_x_impresion[i,0:]}")
    print("Tu matriz de precios sombra es: ")
    print(f"  {lista_nodos[0:num_nodos]}")
    for i in range(num_nodos):
        print(f"{chr(65+i)} {red_iteracion_z_impresion[i,0:]}")
    

    print(f"z={funcion_i}\n Z={z_i}")
    print(f"Acabo en la iteracion{it}")


            



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

    print("Tu matriz de adyacencia inicial es:\n")
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
    
    return arbol_minimo




def lista_vacia(lista_1):
    return not lista_1
    
    















simplex_redes()


    
