class Nodo():
    def __init__(self, dato):
       self.dato = dato
       self.siguiente = None
       self.anterior = None
       
class ListaCircularDoblementeEnlazada():
    def __init__(self):
        self.head=None
        self.last = None
     
    def Insertar(self, dato):
        if self.head is None:
            self.head = self.last = Nodo(dato)
        else:
            aux = self.last
            self.last = aux.siguiente = Nodo(dato)
            self.last.anterior = aux
            self.head.anterior = self.last
            self.last.siguiente = self.head
      
    def Imprimir(self):
        aux = self.head
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.head:
                break
            
    def Buscar(self, condicion):
        aux = self. head
        while aux:
            if str(aux.dato) == str(condicion):
                print("Anterior: ", aux.anterior.dato , " Actual: ", aux.dato, " Siguiente: ", aux.siguiente.dato)      
            aux = aux.siguiente
            if aux == self.head:
                break      
            
            
n = ListaCircularDoblementeEnlazada()
print("Lista Completa:")
n.Insertar(1)
n.Insertar(2)
n.Insertar(3)
n.Insertar(4)
n.Insertar(5)
n.Imprimir()
opcion = input("Seleccione numero: ")
n.Buscar(int(opcion))                