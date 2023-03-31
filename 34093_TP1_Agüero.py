
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
        m = matriz.get_pos(j,k)
        return elems[m]
    
    def del_row (self,j):
        
        """Devuelve una nueva lista sin la fila j de la matriz original."""
        
        elems = self.lista
        new_object = []
        restar = matriz.get_row(j)
        for n in elems:
            if n not in restar:
                new_object.append(n)
      
        return myarray1(new_object,self.r-1, self.c,self.by_row)
    
    def del_col (self,k):
        
        """Devuelve una nueva lista sin la columna k de la matriz original."""
        
        elems = self.lista
        new_object = []
        restar = matriz.get_col(k)
        for n in elems:
            if n not in restar:
                new_object.append(n)
        return myarray1(new_object,self.r, self.c-1,self.by_row)

    def swap_rows (self,j,k):
       
       """Devuelve una nueva lista con las filas j y k intercambiadas."""
        
       elems = self.lista
       listanueva = self.lista.copy()
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
        
        nuevalista = []
        fila = matriz.get_row(j)
        for n in fila:
            nuevalista.append (n*x)
            
        listr = matriz.del_row(j).lista
        listr.insert((j-1)*self.c,nuevalista)
            
        return myarray1(listr,self.r,self.c,self.by_row)
    
    def scale_cols (self,k,y):
        
        """ Devuelve un nuevo objeto de la clase multiplicando la columna k por el 
        número y, el resto de los elementos quedan igual """
        
        elems = self.lista
        nuevalista = []
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
        if self.by_row == True:
            first_row = elems[:self.c]
            last_row = elems[(self.r - 1) * self.c:self.r * self.c]
            new_flist = last_row + elems[self.c:self.c * (self.r - 1)] + first_row
        if self.by_row == False:
            pass 
        
        return new_flist
      
          
if __name__ == "__main__":
    matriz = myarray1 ([1,2,3,4,5,6,7,8,9],3,3,True)
    pos = matriz.get_pos(2,3)
    coord = matriz.get_coords (1)
    lista_switch = matriz.switch()
    fila = matriz.get_row (2)
    columna = matriz.get_col(2)
    m = matriz.get_elem((2,1))
    delrow = matriz.del_row(1)
    delcol = matriz.del_col (1) 
    swaprows = matriz.swap_rows (1,3)
    swapcols = matriz.swap_cols(1,3)
    scalerow = matriz.scale_rows(2, 2)
    scalecol = matriz.scale_cols(1, 2)
    transp = matriz.transpose ()
    flipcol = matriz.flip_cols()
    fliprows = matriz.flip_rows()  

#%% 
"""Para multiplicar las matrices, las columnas de A tienen q ser igual a las filas de B
   Resultado = Filas de A por las columnas de B. 
   getrow (i), getcol (j)
   [l1[n]*l2[n] for n in range (self.c)] sumar 
   
   class eye (myarray1) es una subclase. Hereda los atributos de myarray1. 
   
   def __init__ (self,n):
       self.elems = [0] x (n**2)
       poner unos en la posicion 1,1 2,2 3,3 4,4
       self.r = n
       self.c = n

   premultiplicar es rxr y posmultiplicar es cxc
        
"""

