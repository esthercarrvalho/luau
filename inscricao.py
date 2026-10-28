from datetime import datetime

from excecoes import AtividadeLotadaError, DadoInvalidoError


class Inscricao:

    def __init__(self, convidado, atividade):
        if convidado is None or atividade is None:
            raise DadoInvalidoError("Convidado e atividade são obrigatórios.")
        self.__convidado = convidado
        self.__atividade = atividade
        self.__registrada = False
        self.__data = None

    @property
    def convidado(self):
        return self.__convidado

    @property
    def atividade(self):
        return self.__atividade

    @property
    def registrada(self):
        return self.__registrada

    @property
    def data(self):
        return self.__data

    def verificar_vagas(self):
        return self.__atividade.verificar_vagas()

    def registrar(self):

        if self.__registrada:
            raise DadoInvalidoError("Esta inscrição já foi registrada.")
        if not self.verificar_vagas():
            raise AtividadeLotadaError(f"Sem vagas em '{self.__atividade.nome}'.")
        self.__atividade.adicionar_participante(self.__convidado)
        self.__registrada = True
        self.__data = datetime.now()

    def cancelar(self):
        if not self.__registrada:
            raise DadoInvalidoError("Inscrição ainda não registrada.")
        self.__atividade.remover_participante(self.__convidado)
        self.__registrada = False

    def __str__(self):
        nome = getattr(self.__convidado, "nome", str(self.__convidado))
        status = "confirmada" if self.__registrada else "pendente"
        return f"Inscrição de {nome} em {self.__atividade.nome} ({status})"