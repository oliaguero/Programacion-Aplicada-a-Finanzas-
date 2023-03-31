# 
"""Función para sacar el máximo común divisor entre dos números"""

def MCD_euclides (a,b):
    if b==0:
        return a 
    else:
        resto = a%b
        ans = MCD_euclides (b,resto)
        return ans

a = int(input("Ingrese un número natural:"))
b = int(input ("Ingrese otro número natural:"))

resultado = MCD_euclides (a,b)

print ("El MCD es", resultado)


#%%
"""Función para pasar de números decimales a binarios"""

def dec_a_bin (num):
    if num < 0:
        print ("Error. El número debe ser positivo.")
    if num == 0:
        return ""
    else:
        div = num // 2
        ans = dec_a_bin(div) + str(num%2)
        return ans
        
num = int(input("Ingrese un número:"))

print("Su número binario es", dec_a_bin(num))
    

#%%

def fibonacci (n):
    if n in {0,1}:
        return n 
    else:
        ans = fibonacci (n-1) + fibonacci (n-2)
        return ans 

fibonacci (5)


#%%

"""Base de programa para el juego de los elementos"""

lista = ['Actinium', 'Aluminum', 'Americium', 'Antimony', 'Argon', 'Arsenic', 'Astatine', 'Barium', 
 'Berkelium', 'Beryllium', 'Bismuth', 'Bohrium', 'Boron', 'Bromine', 'Cadmium', 'Calcium', 
 'Californium', 'Carbon', 'Cerium', 'Cesium', 'Chlorine', 'Chromium', 'Cobalt', 'Copernicium', 
 'Copper', 'Curium', 'Darmstadtium', 'Dubnium', 'Dysprosium', 'Einsteinium', 'Erbium', 
 'Europium', 'Fermium', 'Flerovium', 'Fluorine', 'Francium', 'Gadolinium', 'Gallium', 
 'Germanium', 'Gold', 'Hafnium', 'Hassium', 'Helium', 'Holmium', 'Hydrogen', 'Indium', 
 'Iodine', 'Iridium', 'Iron', 'Krypton', 'Lanthanum', 'Lawrencium', 'Lead', 'Lithium', 
 'Livermorium', 'Lutetium', 'Magnesium', 'Manganese', 'Meitnerium', 'Mendelevium', 'Mercury',
 'Molybdenum', 'Moscovium', 'Neodymium', 'Neon', 'Neptunium', 'Nickel', 'Nihonium', 'Niobium',
 'Nitrogen', 'Nobelium', 'Oganesson', 'Osmium', 'Oxygen', 'Palladium', 'Phosphorus', 
 'Platinum', 'Plutonium', 'Polonium', 'Potassium', 'Praseodymium', 'Promethium', 
 'Protactinium', 'Radium', 'Radon', 'Rhenium', 'Rhodium', 'Roentgenium', 'Rubidium', 
 'Ruthenium', 'Rutherfordium', 'Samarium', 'Scandium', 'Seaborgium', 'Selenium', 'Silicon', 
 'Silver', 'Sodium', 'Strontium', 'Sulfur', 'Tantalum', 'Technetium', 'Tellurium', 
 'Tennessine', 'Terbium', 'Thallium', 'Thorium', 'Thulium', 'Tin', 'Titanium', 'Tungsten', 
 'Uranium', 'Vanadium', 'Xenon', 'Ytterbium', 'Yttrium', 'Zinc', 'Zirconium']

list_ans = []

def secuencia (elemento,lista):
    for palabra in lista:
        palabra = palabra.lower()
        if palabra[-1] == elemento[0]:
            list_ans.append(palabra)
        if palabra[0] == elemento[-1]:
            list_ans.append(palabra)
    return list_ans

elemento = input("Ingrese un elemento:")
respuesta = secuencia (elemento, lista)
print(respuesta)

#%%

"""Función para sacar el valor actual de una lista de flujos y una TIR"""

l_flujos = [1500,3200,6800,2330,4790,5092]

def valor_actual (flujos,TIR):
    if len(flujos) == 0:
        return 0
    else:
        valor = flujos[0]/(1+TIR)**len(flujos)
        VA = valor + valor_actual (flujos[1:],TIR)
        return VA

print (valor_actual(l_flujos,0.05))

def valor_futuro (flujos,TIR):
    if len(flujos) == 0:    
        return 0
    else:
        valor = flujos[0]*(1+TIR)**len(flujos)
        VF = valor + valor_futuro(flujos[1:],TIR)
        return VF 

print((valor_futuro(l_flujos,0.05))

      
#%% 

def hanoi (n,origen,helper,destino):
    if n == 1:
        print ("Mover el disco",n, "de", origen, "->", destino)
    else:
        hanoi (n-1,origen,destino,helper)
        print ("Mover el disco", n, "de", origen,"->", destino)
        hanoi(n-1,helper,origen,destino)

hanoi (2,1,2,3)

            

        
        
    









