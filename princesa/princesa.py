import networkx as nx
import matplotlib.pyplot as plt


class Juego:
    def __init__(self, ruta):
        archivo = open(ruta, "rt")
        # primera linea contiene c s d
        linea1 = archivo.readline().split() 
        c = int(linea1[0])  # cantidad de claros
        # s = int(linea1[1])  # cantidad de senderos
        # d = int(linea1[2])  # cantidad de dragones

        # segunda linea contiene cf cm
        linea2 = archivo.readline().split() 
        self.cf = int(linea2[0])  # donde está la princesa
        self.cm = int(linea2[1])  # donde está el príncipe

        # segunda linea contiene claros con dragones
        self.dragones = [int(i) for i in archivo.readline().split()] 
        # list(map(int, archivo.readline().split()))

        # lista con c claros
        claros = []  # nodos del grafo
        for i in range(1, c+1):
            claros.append(i)

        # s lineas con senderos
        senderos = []  # aristas del grafo
        for x in archivo:
            senderos.append(tuple(int(i) for i in x.split()))
        archivo.close()
    
        # crear grafo
        self.bosque = nx.Graph()
        self.bosque.add_nodes_from(claros)
        self.bosque.add_weighted_edges_from(senderos)

        # atributos con los resultados
        self.salida = ""
        self.puntaje = 0

    def encontrarCamino(self):
        try:
            interceptado = False
            camino = nx.dijkstra_path(self.bosque, self.cm, self.cf)
            interceptado = self.esInterceptado(camino)
            if interceptado:
                self.puntaje = 70
                bosqueSinDragones = self.removerClarosConDragones()
                camino = nx.dijkstra_path(bosqueSinDragones, self.cm, self.cf)
            else:
                self.puntaje = 100
            self.salida = camino
        except nx.NetworkXNoPath:
            puntaje = 0
            if interceptado:
                self.salida = "INTERCEPTADO"
            else:
                self.salida = "NO HAY CAMINO"

    def mostrarPuntaje(self):
        print(self.salida)
        print("Puntaje =", self.puntaje)

    #### Metodos auxiliares ####
    def esInterceptado(self, camino):
        for i in self.dragones:
            try:
                camino.index(i)
                return True
            except:
                pass

    def removerClarosConDragones(self):
        gr = self.bosque.copy()
        for i in self.dragones:
            gr.remove_node(i)
        return gr

    def dibujarBosque(self):
        nx.draw(self.bosque, pos=nx.circular_layout(self.bosque),
                node_color='r', edge_color='b', with_labels=True)
        plt.show()

print("### Prueba ejemplo de la consigna ###")
b1 = Juego("entradaEjemplo.in")
b1.encontrarCamino()
b1.mostrarPuntaje()
print("### Prueba principe sin camino a la princesa ###")
b2 = Juego("entradaSinCamino.in")
b2.encontrarCamino()
b2.mostrarPuntaje()
print("### Prueba principe interceptado por dragon y sin camino ###")
b3 = Juego("entradaInterceptado.in")
b3.encontrarCamino()
b3.mostrarPuntaje()
print("### Prueba principe interceptado por dragon y con camino alternativo ###")
b4 = Juego("entradaConCaminoAlternativo.in")
b4.encontrarCamino()
b4.mostrarPuntaje()

b1.dibujarBosque()