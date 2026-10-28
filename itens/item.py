from abc import ABC, abstractmethod

from excecoes import DadoInvalidoError, QuantidadeInvalidaError


class Item(ABC):
    """Classe base (abstrata) dos itens do evento."""

    def __init__(self, nome, quantidade=0):
        self.__nome = None
        self.__quantidade = 0
        self.nome = nome
        self.__quantidade = self._validar_quantidade(quantidade)

    @staticmethod
    def _validar_quantidade(valor):
        if not isinstance(valor, int) or isinstance(valor, bool) or valor < 0:
            raise QuantidadeInvalidaError("A quantidade deve ser um inteiro maior ou igual a zero.")
        return valor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise DadoInvalidoError("O nome do item não pode ser vazio.")
        self.__nome = valor.strip()

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    @abstractmethod
    def categoria(self):
        """'Alimento', 'Bebida' ou 'Material' (usado nas tabelas da interface)."""

    def consultar_quantidade(self):
        return self.__quantidade

    def atualizar_estoque(self, variacao):
        if not isinstance(variacao, int) or isinstance(variacao, bool):
            raise QuantidadeInvalidaError("A variação deve ser um número inteiro.")
        novo = self.__quantidade + variacao
        if novo < 0:
            raise QuantidadeInvalidaError(
                f"Estoque insuficiente de '{self.__nome}': há {self.__quantidade}, tentou retirar {-variacao}."
            )
        self.__quantidade = novo

    def definir_quantidade(self, nova_quantidade):
        self.__quantidade = self._validar_quantidade(nova_quantidade)

    def adicionar(self, quantidade):
        self._validar_quantidade(quantidade)
        self.atualizar_estoque(quantidade)

    def retirar(self, quantidade):
        self._validar_quantidade(quantidade)
        self.atualizar_estoque(-quantidade)

    @abstractmethod
    def descrever(self):

    def _resumo_base(self):
        return f"{self.__nome} (qtd: {self.__quantidade})"

    def __str__(self):
        return self.descrever()