import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        n,a=self._model.crea_grafo()
        min,max=self._model.get_min_max()
        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Numero di archi:{a}, Numero di nodi:{n}"
                                                                   f"\nPeso min: {min} Peso max: {max}"))
        self._view.update()

    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        # TODO
        try:
            self._view.lista_visualizzazione_2.controls.clear()
            s=int(self._view.txt_name.value)
            if s<3 or s>7:
                self._view.show_alert("Inserire un numero compreso tra 3 e 7")
            else:
                mi,ma=self._model.get_soglia(s)
                self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Numero di archi con valore minore della soglia:{mi}"
                                                                           f"\nNumero di archi con valore maggiore della soglia:{ma} "))
                self._view.update()

        except Exception:
            self._view.show_alert("Inserire un numero compreso tra 3 e 7")

    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        # TODO
        try:
            self._view.lista_visualizzazione_3.controls.clear()
            s = int(self._view.txt_name.value)
            r=self._model.get_cammino(s)
            if s<3 or s>7:
                self._view.show_alert("Inserire un numero compreso tra 3 e 7")
            else:
                mi,ma=self._model.get_soglia(s)
                self._view.lista_visualizzazione_3.controls.append(ft.Text(f"{r}"))
                self._view.update()

        except Exception:
            self._view.show_alert("Inserire un numero compreso tra 3 e 7")
