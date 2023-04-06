
"TP1, operando con matrices"

class myarray1: 
    
    def __init__(self,lista,r,c,by_row):
        
        """Constructor de la clase myarray1 que inicializa los atributos lista, r, c
        y by_row """
        
        self.lista = lista
        self.r = r
        self.c = c
        self.by_row = by_row
        
    def get_pos (self,j,k):
        
        """ Devuelve la posición en la lista elems correspondiente a la fila j
        y columna k"""
        
        elems = self.lista
        pos = 0
        fila = 1
        col = 1
        if j > self.r or k > self.c:
            raise ValueError("Las coordenadas j y k deben ser menores que r y c respectivamente.")
        if self.by_row == True:
            for n in elems: 
                if fila == j and col == k:
                    return pos
                if self.c == col:
                    fila+=1
                    col = 0
                col+=1
                pos+=1
        if self.by_row == False:
            for n in elems:
                if fila == j and col == k:
                    return pos 
                if self.r == fila:
                    col+=1
                    fila = 0
                fila+=1
                pos+=1 
       
    def get_coords (self,m):
        
        """Devuelve las coordenadas (fila, columna) correspondientes a la posición 
        m en la lista elems"""
        
        elems = self.lista
        pos = 0
        fila = 1
        col = 1
        if m >= self.r * self.c:
            raise ValueError("La posición m debe ser menor que r * c.")
        if self.by_row == True:
            for n in elems:
                if pos == m:
                    return (fila, col)
                if self.c == col:
                    fila+=1
                    col = 0
                col+=1
                pos+=1
        if self.by_row == False:
            for n in elems: 
                if pos == m:
                    return (fila,col)
                if self.r == fila:
                    col+=1
                    fila=0
                fila+=1
                pos+=1
    
    def switch (self):
        
        """ Devuelve un nuevo objeto myarray1 que representa la lista elems
        alterada para obtener la misma matriz independiente de la forma de recorrerla"""
            
        elems = self.lista 
        new_list = []
        if self.r <= 0 or self.c <= 0:
          raise ValueError("La matriz debe tener al menos una fila y una columna.")
        if self.by_row == True:
            for fila in range(self.r):
                for columna in range (self.c):
                    new_list.append (elems[columna * self.r + fila])
        if self.by_row == False:
            for columna in range(self.c):
                for fila in range (self.r):
                    new_list.append (elems[fila * self.c + columna])
    
        return myarray1 (new_list,self.r,self.c,self.by_row)
        
    def get_row (self,j):
        
        """Devuelve una lista con los elementos de la fila j de la matriz original"""
        
        elems = self.lista
        fila = 1
        col = 1
        l_row = []
        if j > self.r:
           raise ValueError("La fila j debe ser menor que r.")
        if self.by_row == True:
            for n in elems: 
                if fila == j:
                    l_row.append (n)
                if self.c == col:
                    fila+=1
                    col=0
                col+=1
            return l_row
        if self.by_row == False:
            for n in elems: 
                if fila == j:
                    l_row.append(n)
                if self.r == fila:
                    col+=1
                    fila=0
                fila+=1
            return l_row
        
    def get_col(self,k):
        
        """Devuelve una lista con los elementos de la columna k de la matriz original"""
        
        elems = self.lista 
        fila = 1
        col = 1
        l_col = []
        if k > self.c:
            raise ValueError("La columna k debe ser menor que c.")
        if self.by_row == True:
            for n in elems: 
                if col == k:
                    l_col.append(n)
                if self.c == col:
                    fila+=1
                    col=0
                col+=1
            return l_col
        if self.by_row == False:
            for n in elems: 
                if col == k:
                    l_col.append (n)
                if self.r == fila:
                    col+=1
                    fila=0
                fila+=1
            return l_col
        
    def get_elem (self,coord):
        
        """Devuelve el elemento de la matriz original correspondiente a las coordenadas 
        (fila, columna) dadas en coord en formato de tupla"""
        
        elems = self.lista 
        j = coord[0]
        k = coord[1]
        if j > self.r or k > self.c:
           raise ValueError("Las coordenadas j y k deben ser menores que r y c.")
        m = matriz.get_pos(j,k)
        return elems[m]
    
    def del_row (self,j):
        
        """Devuelve una nueva lista sin la fila j de la matriz original."""
        
        elems = self.lista
        new_object = []
        if j > self.r:
           raise ValueError("La fila j debe ser menor que r.")
        restar = matriz.get_row(j)
        for n in elems:
            if n not in restar:
                new_object.append(n)
      
        return myarray1(new_object,self.r-1, self.c,self.by_row)
    
    def del_col (self,k):
        
        """Devuelve una nueva lista sin la columna k de la matriz original."""
        
        elems = self.lista
        new_object = []
        if k > self.c:
            raise ValueError("La columna k debe ser menor que c.")
        restar = matriz.get_col(k)
        for n in elems:
            if n not in restar:
                new_object.append(n)
        return myarray1(new_object,self.r, self.c-1,self.by_row)

    def swap_rows (self,j,k):
       
       """Devuelve una nueva lista con las filas j y k intercambiadas."""
        
       elems = self.lista
       listanueva = self.lista.copy()
       if j > self.r or k > self.r:
           raise ValueError("Las filas j y k deben ser menores que r.")
       if self.by_row == True:
           for n in range (self.c):
               listanueva[(j-1)*self.c + n] = elems[(k-1)*self.c + n]
               listanueva[(k-1)*self.c + n] = elems[(j-1)*self.c + n]
       if self.by_row == False: 
           for n in range (self.r):  
               listanueva[n*self.c + (j-1)] = elems[n*self.c + (k-1)]
               listanueva[n*self.c + (k-1)] = elems[n*self.c + (j-1)]
               
       return myarray1(listanueva,self.r,self.c,self.by_row)
   
    def swap_cols (self,l,m):
        
        """ Devuelve una nueva lista con las columnas l y m intercambiadas """
        
        elems = self.lista 
        nuevascols = self.lista.copy() 
        if l > self.c or m > self.c:
           raise ValueError("Las columnas l y m deben ser menores que c.")
        if self.by_row == True:
            for n in range (self.r):
               c1 = n * self.c + (l-1)
               c2 = n * self.c + (m-1)
               nuevascols[c1] = elems[c2]
               nuevascols[c2] = elems[c1]
        if self.by_row == False:
            for n in range(self.c):
               c1 = (l-1)* self.r + n
               c2 = (m-1) * self.r + n
               nuevascols[c1], nuevascols[c2] = elems[c2], elems[c1]

        return myarray1(nuevascols,self.r,self.c,self.by_row)
            
           
    def scale_rows (self,j,x):
        
        """ Devuelve un nuevo objeto de la clase multiplicando la fila j por el 
        número x, el resto de los elementos quedan igual"""
        
        newlist = self.lista.copy()
        if j > self.r:
           raise ValueError("La fila j debe ser menor que r.")
        for i in range(self.c):
            newlist[(j - 1) * self.c + i] *= x
            
        return newlist
    
    def scale_cols (self,k,y):
        
        """ Devuelve un nuevo objeto de la clase multiplicando la columna k por el 
        número y, el resto de los elementos quedan igual """
        
        elems = self.lista
        nuevalista = []
        if k > self.c:
           raise ValueError("La columna k debe ser menor que c.")
        if self.by_row == True:
            for n in range (len(elems)):
                if n % self.c == k-1:
                    nuevalista.append(elems[n]*y)
                else: 
                    nuevalista.append(elems[n])
            return nuevalista
        if self.by_row == False:
            for i in range(self.r):
                for x in range(self.c):
                    pos = x*self.r + i
                    if x == k-1:
                        nuevalista.append(elems[pos] * y)
                    else:
                        nuevalista.append(elems[pos])

        return myarray1(nuevalista,self.r,self.c,self.by_row)
    
    def transpose(self):
        
        """ Devuelve una lista con la matriz transpuesta """
        
        elems = self.lista 
        transpuesta = []
        if self.by_row == True:
            for x in range(self.c):
                for i in range(self.r):
                    transpuesta.append(elems[i * self.c + x])
        if self.by_row == False:
            for x in range(self.r):
                for i in range(self.c):
                    transpuesta.append(elems[x* self.r + i])
    
        return transpuesta
    
    def flip_cols(self):
        
        """ Devuelve una lista con las columnas de la matriz intercambiadas en forma 
        de espejo"""
        
        elems = self.lista
        flipcols = []
        if self.by_row == True:
            for f in range(self.r):
                fila = elems[f * self.c : (f+1) * self.c]
                flipcols.extend(fila[::-1])
        if self.by_row == False:
            for c in range(self.r):
                col = elems [c::self.c]
                flipcols.extend(col[::-1])
        return flipcols
    
    def flip_rows(self):
        
        """Devuelve una lista con las filas de la matriz intercambiadas en forma de 
        espejo"""
    
        elems = self.lista
        fliprows = []
        if self.by_row == True:
            first_row = elems[:self.c]
            last_row = elems[(self.r - 1) * self.c:self.r * self.c]
            salida = last_row + elems[self.c:self.c * (self.r - 1)] + first_row
        if self.by_row == False:
            for c in range(self.r):
                col = elems [c::self.c]
                fliprows.extend(col[::-1])
                salida = fliprows
        return salida 
    
    def det (self):
        
        """ Calcula el determinante de una matriz cuadrada"""
        
        elems = self.lista 
        if self.r != self.c:
            raise ValueError("La matriz debe ser cuadrada.")
        
        if self.r == 1:
            return elems[0]
        
        elif self.r == 2:
            return elems[0]*elems[3] - elems[1]*elems[2]
        
        else:
        
            det = 0
            signo = 1
            
            for j in range(self.c):
                submatriz = []
                for i in range(1, self.r):
                    for k in range(self.c):
                        if k != j:
                            submatriz.append(elems[i*self.c + k])
                submatriz_det = myarray1(submatriz, self.r-1, self.c-1,self.by_row).det()
                det += elems[j] * submatriz_det * signo
                signo = -signo

            return det
    
    def __add__ (self, other):
        
        """ Redefine la operación de la suma para poder utilizarla dentro de la clase"""
        
        if isinstance (other,myarray1):
            if self.r != other.r or self.c != other.c:
                raise ValueError ("Las matrices deben ser del mismo tamaño para sumarlas")
            suma = []
            for fila in range (self.r):
                for col in range (self.c):
                    pos1 = self.get_pos(fila+1,col+1)
                    pos2 = self.get_pos(fila+1,col+1)
                    suma.append(self.lista[pos1]+ other.lista[pos2])
        if isinstance (other,int):
            suma = []
            for fila in range (self.r):
                for col in range (self.c):
                    pos = self.get_pos(fila+1,col+1)
                    suma.append(self.lista[pos]+other)
                
        return suma
    
    def __radd__ (self,num):
        
        """ Redefine la operación de la suma para poder utilizarla dentro de la clase, 
        pero para que se pueda operar en cualquier orden"""
        
        if isinstance (num,int):
            return self.__add__(num)
        

    def __sub__ (self, other):
        
        """ Redefine la operación de la resta para poder utilizarla dentro de la clase"""
        
        if isinstance (other,myarray1):
            if self.r != other.r or self.c != other.c:
                raise ValueError ("Las matrices deben ser del mismo tamaño para restarlas")
            resta = []
            for fila in range (self.r):
                for col in range (self.c):
                    pos1 = self.get_pos(fila+1,col+1)
                    pos2 = self.get_pos(fila+1,col+1)
                    resta.append(self.lista[pos1] - other.lista[pos2])
        if isinstance (other,int):
            resta = []
            for fila in range (self.r):
                for col in range (self.c):
                    pos = self.get_pos(fila+1,col+1)
                    resta.append(self.lista[pos] - other)
                
        return resta
    
    def __rsub__ (self,num):
        
        """ Redefine la operación de la resta para poder utilizarla dentro de la clase, 
        pero para que se pueda operar en cualquier orden"""
        
        if isinstance (num,int):
            return self.__sub__(num)
    
    def __mul__ (self,num): 
        
        """ Redefine la operación de la multiplicación para poder utilizarla dentro de la clase"""
        
        if isinstance (num,int):
            mult = []
            for i in range (len(self.lista)):
                mult.append(self.lista[i]*num)
        elif isinstance (num,myarray1):
            mult = []
            for i in range(len(self.lista)):
                mult.append(self.lista[i] * num.lista[i])
          
        return mult
    
    def __rmul__ (self, num):
        
        """ Redefine la operación de la multiplicación para poder utilizarla dentro de la clase, 
        pero para que se pueda operar en cualquier orden"""
        
        return self.__mul__(num)
    
    def __matmul__ (self,other):
        
        """ Redefine la operación de la multiplicación para poder multiplicar matrices 
        dentro de la clase"""
        
        if self.c != other.r:
            raise ValueError ("La cantidad de columnas de la primer matriz debe ser igual a la cantidad de filas de la segunda matriz")
        resultado = []
        for i in range (1, self.r + 1):
            fila = []
            for j in range (1, other.c + 1):
                producto = sum(x*y for x,y in zip (self.get_row(i), other.get_col(j)))
                fila.append(producto)
            resultado.extend(fila)
            
        return myarray1 (resultado, self.r, other.c, self.by_row)
    
    def __pow__ (self,exp):
        
        """ Redefine la operación de potenciación para poder utilizarla dentro de la clase"""
        
        if self.r != self.c: 
            raise ValueError ("La matriz tiene que ser cuadrada")
        if exp < 0:
            raise ValueError ("La potencia tiene que ser un número entero positivo")
        if exp == 1:
            resultado = myarray1 (self.lista,self.r,self.c,self.by_row)
        else: 
            resultado = myarray1 (self.lista,self.r,self.c,self.by_row)
            for i in range (exp-1):
                resultado = resultado.__matmul__(self)
        return resultado.lista
    
    def ident_matrix(self):
        
        """Inicializar una lista vacía para almacenar los elementos de la matriz"""
        
        identidad = []
        
        """Colocar unos en la diagonal principal y ceros en las demás posiciones"""
        
        for i in range(self.r):
            for j in range(self.c):
                if i == j:
                    identidad.append(1)
                else:
                    identidad.append(0)
                
        return identidad
    
    def ident_swaprow (self, j, k):
        
        """Devuelve una nueva lista con las filas j y k intercambiadas."""
        
        listanueva = identity.copy()
        if j > self.r or k > self.r:
            raise ValueError("Las filas j y k deben ser menores que r.")
        if self.by_row == True:
            for n in range (self.c):
                listanueva[(j-1)*self.c + n] = identity[(k-1)*self.c + n]
                listanueva[(k-1)*self.c + n] = identity[(j-1)*self.c + n]
        if self.by_row == False: 
            for n in range (self.r):  
                listanueva[n*self.c + (j-1)] = identity[n*self.c + (k-1)]
                listanueva[n*self.c + (k-1)] = identity[n*self.c + (j-1)]
                
        return myarray1(listanueva,self.r,self.c,self.by_row)
                
    def ident_swapcol (self, l, m):
        
        """ Devuelve una nueva lista con las columnas l y m intercambiadas """
        
        nuevascols = identity.copy() 
        if l > self.c or m > self.c:
           raise ValueError("Las columnas l y m deben ser menores que c.")
        if self.by_row == True:
            for n in range (self.r):
               c1 = n * self.c + (l-1)
               c2 = n * self.c + (m-1)
               nuevascols[c1] = identity[c2]
               nuevascols[c2] = identity[c1]
        if self.by_row == False:
            for n in range(self.c):
               c1 = (l-1)* self.r + n
               c2 = (m-1) * self.r + n
               nuevascols[c1], nuevascols[c2] = identity[c2], identity[c1]

        return myarray1(nuevascols,self.r,self.c,self.by_row)
    
    def ident_delrow (self,j):
        
        """Devuelve una nueva lista sin la fila j de la matriz original."""
        
        new_object = []
        if j > self.r:
           raise ValueError("La fila j debe ser menor que r.")
        for i in range (self.r):
            if i != (j-1):
                for k in range (self.c):
                    new_object.append(identity[i*self.c+k])
      
        return myarray1(new_object,self.r-1, self.c,self.by_row)

    def ident_delcol (self,k):
        
        """Devuelve una nueva lista sin la columna k de la matriz original."""
        
        new_object = []
        if k > self.c:
            raise ValueError("La columna k debe ser menor que c.")
        for i in range (self.r):
            for j in range (self.c):
                if j != (k-1):
                    new_object.append(identity[i*self.c+j])
                    
        return myarray1(new_object,self.r, self.c-1,self.by_row)
        
        
if __name__ == "__main__":
     matriz = myarray1([1,2,3,4,5,6,7,8,9],3,3,True)
     print(f'La matriz es: {matriz}')
     pos = matriz.get_pos(1,2)
     print(f'La posición del elemento en la lista es:\t\n{pos}') 
     coord = matriz.get_coords (1)
     print(f'Las coordenadas de la posición dada son:\t\n{coord}') 
     lista_switch = matriz.switch()
     print(f'La lista intercambiada queda:\t\n{lista_switch.lista}') 
     fila = matriz.get_row(2)
     print(f'La fila es:\t\n{fila}') 
     columna = matriz.get_col(2)
     print(f'La columna es:\t\n{columna}') 
     m = matriz.get_elem((2,1))
     print(f'El elemento es:\t\n{m}') 
     delrow = matriz.del_row(1)
     print(f'La nueva matriz es:\t\n{delrow.lista}') 
     delcol = matriz.del_col(1)
     print(f'La nueva matriz es:\t\n{delcol.lista}') 
     swaprows = matriz.swap_rows (1,2)
     print(f'La matriz con las filas intercambiadas queda:\t\n{swaprows.lista}') 
     swapcols = matriz.swap_cols(1,2)
     print(f'La matriz con las columnas intercambiadas queda:\t\n{swapcols.lista}') 
     scalerow = matriz.scale_rows(2, 2)
     print(f'Las filas multiplicadas por un escalar quedan:\t\n{scalerow}') 
     scalecol = matriz.scale_cols(1, 2)
     print(f'Las columnas mutiplicadas por un escalar quedan:\t\n{scalecol}') 
     transp = matriz.transpose()
     print(f'La lista transpuesta queda:\t\n{transp}') 
     flipcol = matriz.flip_cols()
     print(f'La lista con las columnas intercambiadas queda:\t\n{flipcol}') 
     fliprows = matriz.flip_rows()
     print(f'La lista con las filas intercambiadas queda:\t\n{fliprows}') 
     det = matriz.det()
     print(f'El determinante es:\t\n{det}') 
     matriz1 = myarray1([1,2,3,4],2,2,True)
     matriz2 = myarray1([5,6,7,8],2,2,True)
     identity = matriz.ident_matrix()
     print (f'La identidad de la matriz es:\t\n{identity}')
     swaprow_ident = matriz.ident_swaprow(1,3)
     swapcol_ident = matriz.ident_swapcol(2,3)
     delrow_ident = matriz.ident_delrow(2)
     delcol_ident = matriz.ident_delcol(1)
     mul_swaprows = (swaprow_ident@matriz).lista
     print (f'Intercambiando las filas de la identidad, la matriz es:\t\n{mul_swaprows}')
     mul_swapcols = (swapcol_ident@matriz).lista
     print (f'Intercambiando las columnas de la identidad, la matriz es:\t\n{mul_swapcols}')
     mul_delrow = (delrow_ident@matriz).lista
     print (f'Eliminando una fila de la identidad, la matriz es:\t\n{mul_delrow}')
     mul_delcol = (matriz@delcol_ident).lista
     print (f'Eliminando una columna de la identidad, la matriz es:\t\n{mul_delcol}')
     suma = matriz1 + matriz2
     print(f'La suma de matrices es:\t\n{suma}') 
     nsuma = 2 + matriz1
     print(f'La suma de un número a la matriz es:\t\n{nsuma}') 
     resta = matriz1 - matriz2
     print(f'La resta de matrices es:\t\n{resta}') 
     nresta = 1 - matriz2
     print(f'La resta de un número a la matriz es:\t\n{nresta}') 
     nmul = matriz1*2
     print(f'La mutiplicación de la matriz por un escalar es:\t\n{nmul}') 
     matmul = (matriz1@matriz2).lista
     print(f'La multiplicación de matrices es:\t\n{matmul}') 
     power = matriz1**3
     print(f'La potenciación de la matriz es:\t\n{power}') 
     


