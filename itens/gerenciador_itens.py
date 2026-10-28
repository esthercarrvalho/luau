from excecoes import DadoInvalidoError
from itens.item import Item


class GerenciadorItens:
    """Guarda os itens do evento. Alimenta as telas Comida e Bebidas,
    Materiais e Resumo da interface."""

    def __init__(self):
        self.__itens = []

    def _indice(self, nome):
        alvo = nome.strip().lower()
        for i, item in enumerate(self.__itens):
            if item.nome.lower() == alvo:
                return i
        return None

    def cadastrar(self, item):
        if not isinstance(item, Item):
            raise DadoInvalidoError("Só é possível cadastrar objetos do tipo Item.")
        if self._indice(item.nome) is not None:
            raise DadoInvalidoError(f"Já existe um item chamado '{item.nome}'.")
        self.__itens.append(item)

    def obter(self, nome):
        indice = self._indice(nome)
        if indice is None:
            raise DadoInvalidoError(f"Item '{nome}' não encontrado.")
        return self.__itens[indice]

    def excluir(self, nome):
        indice = self._indice(nome)
        if indice is None:
            raise DadoInvalidoError(f"Item '{nome}' não encontrado.")
        del self.__itens[indice]

    def listar(self, *categorias):
        """listar() -> todos | listar('Alimento', 'Bebida') -> só essas categorias."""
        if not categorias:
            return list(self.__itens)
        return [i for i in self.__itens if i.categoria in categorias]

    def buscar_por_nome(self, trecho, *categorias):
        trecho = trecho.strip().lower()
        return [i for i in self.listar(*categorias) if trecho in i.nome.lower()]

    def total(self, *categorias):
        return len(self.listar(*categorias))

    def resumo(self):
        """Números usados na tela Resumo."""
        return {
            "comida_e_bebida": self.total("Alimento", "Bebida"),
            "materiais": self.total("Material"),
        }