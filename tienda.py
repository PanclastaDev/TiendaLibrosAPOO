from datetime import datetime
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

    @tipo.setter
    def tipo(self, valor): #Propiedad para invocar el atributo encapsulando la info
          if valor == 1 or valor == 2:
            self._tipo = valor


class Libro:
    def __init__(self, isbn:str, titulo:str, precio_venta:float, precio_compra:float, cantidad_actual:int):
        self.isbn = isbn
        self.titulo = titulo
        self.precio_venta = precio_venta
        self.precio_compra = precio_compra
        self.cantidad_actual = cantidad_actual 
        self.transacciones = list()   #Atributo que representa la relacion entre clase libro y clase transacciones


class Tienda:
    def __init__(self) -> None:
        self.dinero_caja = 1000000
        self.catalogo = dict() #El diccionario asocia una clave al elemento lo que lo ghace mas facil para buscar dentro del dict

if __name__ == "__main__":
    trans_1 = Transaccion(Transaccion.VENTA, 20)
    trans_2 = Transaccion(Transaccion.ABASTECIMIENTO,10)

print(f"Cantidad t1: {trans_1.tipo}")
print(f"Cantidad t2: {trans_2.tipo}")

