"""Exceções personalizadas do sistema de eventos."""


class EventoError(Exception):
    """Classe base de todos os erros do sistema."""


class AtividadeLotadaError(EventoError):
    """Tentativa de adicionar participante em atividade sem vagas."""


class ParticipanteDuplicadoError(EventoError):
    """Convidado já inscrito na atividade."""


class QuantidadeInvalidaError(EventoError):
    """Quantidade negativa ou estoque insuficiente."""


class DadoInvalidoError(EventoError):
    """Dado de entrada inválido (nome vazio, limite <= 0 etc.)."""