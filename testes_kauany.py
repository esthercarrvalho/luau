from excecoes import (
    AtividadeLotadaError,
    DadoInvalidoError,
    QuantidadeInvalidaError,
)
from inscricao import Inscricao
from itens.alimento import Alimento
from itens.bebida import Bebida
from itens.gerenciador_itens import GerenciadorItens
from itens.material import Material

class Convidado: 
    def __init__(self, nome):
        self.nome = nome


class AtividadeRecreativa: 
    def __init__(self, nome, limite):
        self.nome = nome
        self._limite = limite
        self._participantes = []

    def verificar_vagas(self):
        return len(self._participantes) < self._limite

    def adicionar_participante(self, convidado):
        self._participantes.append(convidado)

    def remover_participante(self, convidado):
        self._participantes.remove(convidado)


def testar_itens():
    itens = [
        Alimento("Coxinha", 50, "30/10/2026", False),
        Bebida("Suco de uva", 20, 300, False),
        Material("Cones", 10, True),
    ]
    for i in itens: 
        print(i.descrever(), "| categoria:", i.categoria)

    suco = itens[1]
    suco.retirar(5)
    suco.adicionar(10)
    assert suco.consultar_quantidade() == 25
    suco.definir_quantidade(40)
    assert suco.quantidade == 40
    print("Volume total (ml):", suco.volume_total_ml())

    operacoes = (
        lambda: suco.retirar(999),
        lambda: suco.adicionar(-3),
        lambda: suco.definir_quantidade(-1),
        lambda: Material("Bola", -1),
    )
    for operacao in operacoes:
        try:
            operacao()
            assert False, "deveria lançar QuantidadeInvalidaError"
        except QuantidadeInvalidaError as e:
            print("OK (quantidade inválida):", e)

    try:
        Alimento("   ", 1)
        assert False
    except DadoInvalidoError as e:
        print("OK (nome vazio):", e)


def testar_gerenciador():
    g = GerenciadorItens()
    g.cadastrar(Alimento("Hambúrguer", 50))
    g.cadastrar(Bebida("Refrigerante", 30))
    g.cadastrar(Bebida("Água", 50))
    g.cadastrar(Material("Cones", 10))

    assert g.total() == 4
    assert g.total("Alimento", "Bebida") == 3
    assert [i.nome for i in g.listar("Bebida")] == ["Refrigerante", "Água"]
    assert [i.nome for i in g.buscar_por_nome("ref", "Alimento", "Bebida")] == ["Refrigerante"]
    print("Resumo:", g.resumo())

    try:
        g.cadastrar(Bebida("água", 5))
        assert False
    except DadoInvalidoError as e:
        print("OK (duplicado):", e)

    g.excluir("Água")
    assert g.total("Bebida") == 1
    try:
        g.obter("Água")
        assert False
    except DadoInvalidoError as e:
        print("OK (não encontrado):", e)


def testar_inscricao():
    pira = AtividadeRecreativa("Pira-pega", 1)
    ana, bia = Convidado("Ana"), Convidado("Bia")

    insc_ana = Inscricao(ana, pira)
    insc_ana.registrar()
    print(insc_ana)

    try:
        Inscricao(bia, pira).registrar()
        assert False, "deveria lançar AtividadeLotadaError"
    except AtividadeLotadaError as e:
        print("OK (lotada):", e)

    try:
        insc_ana.registrar()
        assert False
    except DadoInvalidoError as e:
        print("OK (já registrada):", e)

    insc_ana.cancelar()
    assert pira.verificar_vagas()
    print("Inscrição cancelada, vaga liberada.")


if __name__ == "__main__":
    testar_itens()
    testar_gerenciador()
    testar_inscricao()
    print("\nTodos os testes passaram.")