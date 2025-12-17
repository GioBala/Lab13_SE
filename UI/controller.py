import flet as ft
from pyparsing import alphanums

from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        n_n,n_a,min,max=self._model.Crea_graph()
        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Numero di vertici: {n_n}, numero di nodi: {n_a}\n min: {min}\n max: {max}"))
        self._view.page.update()


    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        # TODO
        self._view.lista_visualizzazione_2.controls.clear()
        soglia=self._view.txt_name.value()
        if soglia is not int or soglia < 3 or soglia > 7:
            self._view.alert("inserire un numero valido")
        sup,inf=self._model.conta_archi(soglia)
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Numero di vertici con peso maggiore {sup}\n Numero di nodi con peso minore: {inf}"))
        self._view.page.update()


    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        # TODO