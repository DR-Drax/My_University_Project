import matplotlib.pyplot as plt
import math

def graficar_resultados(table):
    """
    Genera un gráfico con los resultados calculados.

    Parameters:
        table: list, tabla de resultados con valores de x e y.
        metodo: str, nombre del método utilizado para el cálculo.

    Returns:
        None, muestra el gráfico.
    """
    x_values = table[0]
    y_values = table[1]

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, marker='o', label=f'Levas')
    plt.title('Grafica de levas')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()


def lineal(info,control,time,inter,table,plano,tiempo_temp):

    if info[1][control] == 1:
                            #info[2]=altura    info[0]=tiempo
        table[1].append((time*info[2][control])/info[0][control])
        tiempo_temp = 1 

    elif (info[1][control] == 3):

        if info[2][control] == 0:
            control_t= info[2][control-1] 

        else:
            control_t= info[2][control] 

        desenso =  plano -((tiempo_temp*inter*control_t)/info[0][control])

        if desenso <= 0:    desenso = 0

        table[1].append(desenso)

        tiempo_temp += 1

    return info,control,time,inter,table,plano,tiempo_temp    

def armónico(info,control,time,inter,table,plano,tiempo_temp):

    if info[1][control] == 1:
        formula = plano +(info[2][control]/2)*(1-math.cos((math.pi*time)/info[0][control]))
        table[1].append(formula)

    elif (info[1][control] == 3):

        #desenso =  plano -((tiempo_temp*inter*control_t)/info[0][control])
        print(f"Control --- {control}")
                # info[2][control] + (round(plano,2)/2)*(1 + math.cos((math.pi*tiempo_temp*inter)/info[0][control]))
        formula = info[2][control] + ((plano - info[2][control])/2)*(1 + math.cos((math.pi*tiempo_temp*inter)/info[0][control]))
        if formula <= 0:    formula = 0

        #print(f"Hj (inicial):{round(plano,2)}\nHf(final):{info[2][control]}\nti: {tiempo_temp*inter}\nTj: {info[0][control]}\nResult: {formula}\n")
        #if desenso <= 0:    desenso = 0

        table[1].append(formula)
        tiempo_temp += 1

    return info,control,time,inter,table,plano,tiempo_temp 

def cicloidal(info,control,time,inter,table,plano,tiempo_temp):

    if info[1][control] == 1:
        formula = plano + info[2][control]*((time/info[0][control])-(1/(math.pi*2))*math.sin((2*math.pi*time)/info[0][control]))
        table[1].append(formula)

    elif (info[1][control] == 3):

        #desenso =  plano -((tiempo_temp*inter*control_t)/info[0][control])
        print(f"Control --- {control}")
        formula = info[2][control] + (plano - info[2][control])*(1 - ((tiempo_temp*inter)/info[0][control]) + (1/(2*math.pi))*math.sin((2*math.pi*tiempo_temp*inter)/info[0][control]))

        if formula <= 0:    formula = 0

        print(f"Hj (inicial):{round(plano,2)}\nHf(final):{info[2][control]}\nti: {tiempo_temp*inter}\nTj: {info[0][control]}\nResult: {formula}\n")
        #if desenso <= 0:    desenso = 0

        table[1].append(formula)
        tiempo_temp += 1

    return info,control,time,inter,table,plano,tiempo_temp

def levas_Table(info,type_h,intervalor):       
    #   info = [[tiempo],[movimiento],[altura(m)]]
    sum = 0
    control_time = []
    table = [[],[]]


    for i in info[0]:
        sum += i
        control_time.append(round(sum,2))

    inter = 0.1 
    #inter = sum/intervalor
    wleva = 1/sum
    control = 0
    tiempo_temp = 0
    plano = 0
    desenso = 0
    #print("time\t\tmedida")

    for i in range (0,intervalor+1):

        time = round(i*inter,2)
        table[0].append(time)

        if info[1][control] == 2:
            table[1].append(plano)
            tiempo_temp = 1 

        if type_h[control] == 1:
            info,control,time,inter,table,plano,tiempo_temp = lineal(info,control,time,inter,table,plano,tiempo_temp)

        elif type_h[control] == 2:
            info,control,time,inter,table,plano,tiempo_temp = armónico(info,control,time,inter,table,plano,tiempo_temp)
                        
        elif type_h[control] == 3:
            info,control,time,inter,table,plano,tiempo_temp = cicloidal(info,control,time,inter,table,plano,tiempo_temp)
        print(f"{round(table[0][i],2)}\t\t{round(table[1][i],4)}")

        if ((time)==control_time[control] and control < (len(control_time)-1)): control += 1;plano = table[1][i]; print(f"Control {control}"); print("___________________")

        if time == round(sum,3): print(f"\ntiempo {time} == {round(sum,3)} "); break

    graficar_resultados([table[0],table[1]])
        


            # tiempo            #baja sube     altura

#Eje 1
levas_Table([[3,1,6,2],[1,2,3,2],[10,10,0,0]],[2,1,3,1],1000)

#EJE 2 
levas_Table([[.5,.1,.6],[1,2,3],[.5,.5,0]],[2,2,2],1000)

#EJE 3 ---- PENDIENTE
levas_Table([[4,1,4,1,2],[1,2,3,2,3],[1,1,.5,.5,0]],[3,3,3,3,3],1000)

#EJE 4 ---- PENDIENTE
levas_Table([[.8,.3,.6,.3,.7],[1,2,3,2,3],[1,1,.5,.5,0]],[3,3,3,3,3],1000)



#levas_Table([[1.7,.8,.8,.3,.8],[1,2,3,2,3],[1,1,.5,.5,0]],[2,2,2,2,2],100)
#levas_Table([[1.7,.8,.8,.3,.8],[1,2,3,2,3],[1,1,.5,.5,0]],[2,2,2,2,2],100)
#P50


# P49       Tiempo          aciende        altura
#levas_Table([[.2,.3,.3,.2,.2],[1,2,3,2,3],[24,24,10,10,0]],[2,1,2,1,2],1000)

#levas_Table([[.2,.3,.3,.2,.2],[1,2,3,2,3],[24,24,10,10,0]],[1,1,2,1,2],100)

#Pruevas 
# levas_Table([[1.7,.8,.8,.3,.8],[1,2,3,2,3],[1,1,.5,.5,0]],[1,1,1,1,1],100)
#levas_Table([[1.4,2.3,.8,1.5,.4],[1,2,3,2,3],[.75,.75,.5,.5,0]],[1,1,1,1,1],100)
