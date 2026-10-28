from itens.item import Item
from excecoes import DadoInvalidoError


class Bebida(Item):
    def __init__(self, nome, quantidade=0, volume_ml=500, alcoolica=False):
        super().__init__(nome, quantidade)
        if not isinstance(volume_ml, (int, float)) or volume_ml <= 0:
            raise DadoInvalidoError("O volume da bebida deve ser maior que zero.")
        self.volume_ml = volume_ml
        self.alcoolica = alcoolica

    @property
    def categoria(self):
        return "Bebida"

    def volume_total_ml(self):
        return self.volume_ml * self.consultar_quantidade()

    def descrever(self):
        tipo = "alcoólica" if self.alcoolica else "sem álcool"
        return f"[Bebida] {self._resumo_base()} - {self.volume_ml} ml cada, {tipo}"