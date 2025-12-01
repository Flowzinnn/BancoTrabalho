from typing import List
from abc import abstractmethod
from interfaces import Autenticavel
from auxiliares import Transacao, Notificacao

#Classe Abstrata/Abstract class : CLASSES ABSTRATAS NUNCA IRÃO GERAR UM OBJETO;
class Conta(Autenticavel):
    def __init__(self, numero: str, cliente: 'Cliente', saldo: float, senha: str):
        self._numero = numero
        self._cliente = cliente
        self._saldo =saldo 
        self._senha = senha
        self._transacoes: List['Transacao'] = []
        
        cliente.adicionar_conta(self)
    
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, value):
        self._cliente = value

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo = value

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, value):
        self._senha = value
        
    @abstractmethod
    def sacar(self, valor: float):
        pass

    @abstractmethod
    def aplicar_taxas(self):
        pass

    def autenticar(self, senha):
        return self.senha == senha
        
    def depositar(self, valor: float):
        if valor <= 0:
            Notificacao.erro_valor_invalido()
            return

        self._saldo += valor
        transacao = Transacao("Depósito", valor, self)
        self._transacoes.append(transacao)
        Notificacao.deposito(valor)
    
    #========================================================= EXTRATO ===============================================================#
    
    def extrato(self):
        Notificacao.cabecalho_extrato()
        Notificacao.cabecalho_conta(self.numero, self.cliente.nome)

        if not self._transacoes:
            Notificacao.nenhuma_transacao()
            Notificacao.rodape_extrato(self.saldo)
            return

        for t in self._transacoes:
            Notificacao.mostrar_transacao(t)

        Notificacao.rodape_extrato(self.saldo)
