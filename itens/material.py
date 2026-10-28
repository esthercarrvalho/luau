from itens.item import Item


class Material(Item):
    def __init__(self, nome, quantidade=0, reutilizavel=True):
        super().__init__(nome, quantidade)
        self.reutilizavel = reutilizavel

    @property
    def categoria(self):
        return "Material"

    def descrever(self):
        tipo = "reutilizável" if self.reutilizavel else "descartável"
        return f"[Material] {self._resumo_base()} - {tipo}"