from itens.item import Item


class Alimento(Item):
    def __init__(self, nome, quantidade=0, validade=None, vegetariano=False):
        super().__init__(nome, quantidade)
        self.validade = validade
        self.vegetariano = vegetariano

    @property
    def categoria(self):
        return "Alimento"

    def descrever(self):
        extra = "vegetariano" if self.vegetariano else "contém carne/derivados"
        validade = f", validade: {self.validade}" if self.validade else ""
        return f"[Alimento] {self._resumo_base()} - {extra}{validade}"