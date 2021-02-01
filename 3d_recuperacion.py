"""
Alumna: Brito Barredo Ingrid Dumary
NoControl: 18390017

3D-Recuperacion
"""
import matplotlib.pyplot as plt 
from math import sin, cos, radians,sqrt

import msvcrt #importamos la libreria keyboard para poder ejecutar acciones pulsando una tecla
from pynput import keyboard as kb 
import keyboard 

#Coordenadas iniciales
xg=[]
yg=[]
zg=[]

#Cordenadas centrales
xc=10
yc=30
zc=40

#Coordenadas del sistema local plano 
x=[]
y=[]
z=[]

#Metodo para determinar las coordenadas del plano 
def coordenadasplano(x,y,z,xc,yc,zc,xg,yg,zg,hpx,hpy):
    x=[40,30,80,hpx] #-----Integre la asignacion de las coordenadas aqui debido a que el hitpoint o coordenada 3 es dada por el usuario (dinamica)
    y=[60,10,60,hpy] 
    z=[0,0,0,0]

    xg=[] #-----establecemos o reestablecemos los valores de las coordenadas iniciales
    yg=[]
    zg=[]

    for i in range(len(x)):
        xg.append(x[i]+xc)
        yg.append(y[i]+yc)
        zg.append(z[i]+zc)

    return x,y,z,xg,yg,zg


#____Plotear el sistema 
def plotPlaneLine(xg,yg,zg,hitcolor,areaA,areaA1,areaA2):
    plt.axis([0,150,200,0])
    plt.axis('on')
    plt.grid(False)
    
    plt.plot([xg[0],xg[2]],[yg[0],yg[2]],color='orange')#ploteo del plano o triangulo A
    plt.plot([xg[2],xg[1]],[yg[2],yg[1]],color='orange')
    plt.plot([xg[1],xg[0]],[yg[1],yg[0]],color='orange')

    plt.plot([xg[3],xg[0]],[yg[3],yg[0]],linestyle=":",color='steelblue')#ploteo del plano o triangulo A2
    plt.plot([xg[3],xg[1]],[yg[3],yg[1]],linestyle=":",color='steelblue')
    plt.plot([xg[1],xg[0]],[yg[1],yg[0]],linestyle=":",color='steelblue')

    plt.plot([xg[0],xg[2]],[yg[0],yg[2]],linestyle=":",color='g')#ploteo del plano o triangulo A1
    plt.plot([xg[3],xg[2]],[yg[3],yg[2]],linestyle=":",color='g')
    plt.plot([xg[3],xg[0]],[yg[3],yg[0]],linestyle=":",color='g')

    #etiquetas de cada punto
    plt.text(xg[3]+5,yg[3],'Hitpoint')
    plt.text(xg[3],yg[3],'3')
    plt.text(xg[0],yg[0]+5,'0')
    plt.text(xg[2],yg[2],'2')
    plt.text(xg[1],yg[1]-5,'1')

    #___________ETIQUETAS DE LAS AREAS
    plt.text(10,150,'Área del Triángulo A (012) es: ' + str(areaA),color ='orange')
    plt.text(10,160,'Área del Triángulo A2 (013) es: ' + str(areaA1),color='g')
    plt.text(10,170,'Área del Triángulo A3 (023) es: ' + str(areaA2),color ='steelblue')
    AT=areaA2+areaA1
    plt.text(10,180,'Triángulo A2 + Triángulo A3 = ' + str(AT))

#------Define el resultado de la etiqueta  mostrando si esta fuera del limite y dentro del limite.
    if(hitcolor =='red'):
        plt.text(10,10,'OUT: El punto de impacto esta FUERA de los limites',color ='red')
        plt.scatter(xg[3],yg[3],s=20,color=hitcolor) #marco el hitpoint
    elif hitcolor =='yellow':
        plt.text(10,10,'IN: El punto de impacto esta DENTRO de los limites',color ='darkblue')
        plt.scatter(xg[3],yg[3],s=20,color=hitcolor) #marco el hitpoint


#------Etiquetar los ejes X, Y, y poner un titulo
    plt.xlabel("EJE X")
    plt.ylabel("EJE Y")
    plt.title("--- 3D-Recuperacion ---")

    plt.show()

def hitpointIN_OUT(x,y,z):
#-Para poder aplicar la formula de Heron necesitamos saber la distancia que hay entre cada uno de los puntos

#-------------------------------------TRIANGULO A
    #_____distance point 0 to 1
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    Q01=sqrt(a*a+b*b+c*c) #distancia neta
    #_____distance point 1 to 2
    a=x[2]-x[1]
    b=y[2]-y[1]
    c=z[2]-z[1]
    Q12=sqrt(a*a+b*b+c*c) 
    #_____distance point 0 to 2
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    Q02=sqrt(a*a+b*b+c*c) 
#-------------------------------------TRIANGULO A1
    #_____distance point 0 to 3
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    Q03=sqrt(a*a+b*b+c*c)  
    #_____distance point 1 to 3
    a=x[3]-x[1]
    b=y[3]-y[1]
    c=z[3]-z[1]
    Q13=sqrt(a*a+b*b+c*c) 

    #_____distance point 0 to 1
        #----Se calculo previamente
#-------------------------------------TRIANGULO A2
    #_____distance point 2 to 3
    a=x[3]-x[2]
    b=y[3]-y[2]
    c=z[3]-z[2]
    Q23=sqrt(a*a+b*b+c*c) 

    #_____distance point 0 to 2
        #----Se calculo previamente
    #_____distance point 0 to 3
        #----Se calculo previamente

#-------------Otra forma más simple de obtener las distancias entre cada punto
    #Q01 = sqrt( (x[0]-x[1])**2 + (y[0]-y[1])**2 )
    #Q12 = sqrt( (x[1]-x[2])**2 + (y[1]-y[2])**2 )
    #Q02 = sqrt( (x[0]-x[2])**2 + (y[0]-y[2])**2 )
    #Q13 = sqrt( (x[1]-x[3])**2 + (y[1]-y[3])**2 )
    #Q03 = sqrt( (x[3]-x[0])**2 + (y[3]-y[0])**2 )
    #Q23 = sqrt( (x[3]-x[2])**2 + (y[3]-y[2])**2 )


#-Una vez que tengamos los datos de las distancias, procedemos a aplicar las formulas de semiperimetro y area 

#---------CALCULAMOS CADA SEMIPERIMETRO Y AREA---------------- Formulas a aplicar-> s=(a+b+c)/2  a=sqrt(s*(s-a)*(s-b)*(s-c))
    sA = (Q01+Q12+Q02)/2 # TRIANGULO A
    areaA = sqrt(sA*(sA-Q01)*(sA-Q12)*(sA-Q02))
    sA1 = (Q01+Q13+Q03)/2 # TRIANGULO A1
    areaA1 = sqrt(sA1*(sA1-Q01)*(sA1-Q13)*(sA1-Q03))
    sA2 = (Q02+Q23+Q03)/2 # TRIANGULO A2
    areaA2 = sqrt(sA2*(sA2-Q02)*(sA2-Q23)*(sA2-Q03))

#Con esta decision definimos el hitpoint esta dentro o fuera del limite
    if(areaA1 + areaA2 > areaA):
        hitcolor='red'
    elif (areaA1 + areaA2 < areaA):
        hitcolor= 'yellow' 

    return hitcolor,areaA,areaA1,areaA2
 

while True:
    axis=input('Press "h" to define the hitpoint coordinates. Pulse key esc to exit (honestly doesnt work that): ')

    if axis=='h':
        hpx=(float(input('Coordinate X: ')))  #---Pedir al usuario el hitpoint con el que desea trabajar y plotear el PlaneLine
        hpy=(float(input('Coordinate Y: ')))
        x,y,z,xg,yg,zg = coordenadasplano(x,y,z,xc,yc,zc,xg,yg,zg,hpx,hpy)
        hitcolor,areaA,areaA1,areaA2 = hitpointIN_OUT(x,y,z)
        plotPlaneLine(xg,yg,zg,hitcolor,areaA,areaA1,areaA2)

    elif axis=='esc': 
        break
    
   #I tried but I didn't succeed;( ->    #---El programa termina hasta que el usuario pulse la tecla “Esc” 
    #if msvcrt.kbhit() and msvcrt.getch().decode() == chr(27):
     #   break
    #if msvcrt.kbhit() and msvcrt.getch() == b'\x1b':
     #   break
    #elif keyboard.is_pressed(): 
     #  break
    #elif keyboard.is_pressed('\x1b'): 
     #  break
    #elif keyboard.read_key() == kb.Key.esc: 
     #   break
    #elif keyboard.read_key() ==b'\x1b':
     #   break

#def suelta(tecla):
	##print('Se ha soltado la tecla ' + str(tecla))
	#if tecla == kb.Key.esc:
	#	return False

#kb.Listener(suelta).run()   

        
    
        
        
