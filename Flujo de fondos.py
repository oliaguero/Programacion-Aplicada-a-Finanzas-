
class FF ():
    
    def __init__(self,tupla=tuple()):
       self.flujos=tupla
       
    def VAN (self,tasa, n=0):
       """ Calculo de valor actual neto recursivo
           tasa: (posicional)
           n: posicion en el vector. Sirve para manejar recursivamene las iteraciones 
           sin alterar la lista del flujo de fondos  
       """
       if len(self.flujos)>0:
           if n==len(self.flujos):
               salida = 0
           else:
               salida = self.flujos[n]+1/(1+tasa)*self.VAN(tasa, n=n+1)
       else:
           print('\n',"La tupla de flujo de fondos esta vacia. Se devuelve 0")
           salida = 0
       return salida
   
    def VT (self,tasa,t = 0):
       
       """ Calculo de valor del flujo de fondos a un tiempo t
           Funciona calculando van y luego llevando a tiempo t correspondiente
           tasa: (posicional)
           t: momento de valuación
       """
       return self.VAN(tasa)*(1+tasa)**t
   
        

claseff = FF((-80,10,10,10,10,10,10,10,10,100)) 
van1 = claseff.VAN(0.1)
vt = claseff.VT(0.1,10)

#%%

"""
Grid search: Poner un número máximo y mínimo para crear una grilla. 
Un parámetro que es la cantidad de particiones. 
Tolerancia para margen de error de la TIR. El margen de error es b-a. 

(b-a) < tol. Devuelve el promedio de (a+b)/2

a y b son valores de tasa. f es la función VAN. 

(a,b,n,tolerancia)

Toma el intervalo de origen y hace una partición en n subintervalos. Buscar el cambio 
de signo. Tomar el último cambio de signo, pasar de + a - .

Si hay dos TIR usar la tasa más alta. 

Hacerlo recursivo. 

INTERPOLACIÓN 
 y = fa  + ((fb - fa) / (b-a)) . (x-a)
 
Igualar a cero es la TIR
 x = a - fa.(b-a)/(fb-fa)
 

BISECCIÓN 

fa - fb < 0

OPERACIONES SUCESIVAS 
r = 0 
r0+h para la dirección (derecha o izquierda). Te moves al cero

"""

