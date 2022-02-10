from datetime import datetime
from functools import reduce
from logging import exception
#(Dos espacios para codigo limpio - regla de estilo para python)

class Transaccion: #Crear un clase con el Nombre

    VENTA = 1
    ABASTECIMIENTO = 2

    def __init__(self, tipo: int, cantidad: int):  #Metodo Inicializador para inicializar los valores del objeto creado / los elementos dentro de los parentesis son parámetros (Variables que solo existen dentro del Método)
        self._tipo = tipo
        self._cantidad = cantidad
        self._fecha = datetime.now()

    @property
    def tipo(self):
        return self._tipo #Propiedad para invocar el atributo encapsulando la info

    
    @property
    def cantidad(self):
        return self._cantidad


    @property
    def fecha(self):
        return self._fecha  



class Libro:
    def __init__(self, isbn:str, titulo:str, precio_venta:float, precio_compra:float,cantidad:int):
        self.isbn = isbn
        self.titulo = titulo
        self.precio_venta = precio_venta
        self.precio_compra = precio_compra
        selfcantidad =cantidad 
        self.transacciones = list() #Atributo que representa la relacion entre clase libro y clase transacciones
    

    def vender(self, cantidad) -> bool:
        """
        Vende una cantidad dada de ejemplares del libro, si no hay esa cantidad, no se realiza la venta y 
        el metodo retorna Falso, si la venta se realiza, el método retorna Verdadero. JuanV/TT
        """


        if self.cantidad_actual >= cantidad:
            self.cantidad_actual -= cantidad
            transaccion = Transaccion(Transaccion.VENTA, cantidad)
            self.transacciones.append(transaccion)
            return True
        else:
            return False


    def abastecer(self, cantidad):
        self.cantidad_actual += cantidad
        transaccion = Transaccion(Transaccion.ABASTECIMIENTO, cantidad)
        self.transacciones.append(transaccion)

    
    def informar_ejemplares_vendidos(self) ->int:
        if len(self.transacciones) > 0:
            # cantidades = [t.cantidad for t in self.transacciones if t.tipo == Transaccion.VENTA] #MODO DE ENCONTRAR EJEMPLARES VENDIDOS CON FUNCIONES DE PYTHON
            # total_ejemplares = reduce(lambda x,y: x + y, cantidades)
            # return total_ejemplares

            cantidad_ejemplares = 0
            for trans in self.transacciones:
                if trans.tipo == Transaccion.VENTA:
                    cantidad_ejemplares += trans.cantidad
            return cantidad_ejemplares
        else:
            return 0


    def __str__(self) -> str:
        return f"ISBN: {self.isbn} \nTitulo: {self.titulo}"


    @property
    def cantidad(self):
        return self._cantidad_actual


    cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad <= 0:  
            raise Exception("¡La cantidad de unidades de un libro no puede ser negativa!")
        self.cantidad_actual = nueva_cantidad


    

class Tienda:
    def __init__(self) -> None:
        self.dinero_caja = 1000000
        self.catalogo = dict() #El diccionario asocia una clave al elemento lo que lo hace mas facil para buscar dentro del dict


    def registrar_libro_en_catalogo(self, isbn, titulo, precio_venta, precio_compra, cantidad_actual):
        if isbn not in self.catalogo.keys():
            libro = Libro(isbn, titulo, precio_venta, precio_compra, cantidad_actual)
            self. catalogo[isbn] = libro
        else:
            raise Exception("Ya existe un libro bajo el ISBN # {isbn}")
    

    def eliminar_libro_catalogo(self, isbn):
        if isbn in self.catalogo.keys():
            del self.catalogo[isbn]
        else:
            raise Exception("No existe un libro con el ISBN ingresado")
    
    

    

