from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conta import Conta

class Notificacao:
    
    @staticmethod
    def deposito(valor):
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    @staticmethod
    def saque(valor):
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    @staticmethod
    def taxa_manutencao(valor):
        print(f"Taxa de manutenção de R$ {valor:.2f} aplicada.")

    @staticmethod
    def nenhuma_transacao():
        print("Nenhuma transação realizada.")

    @staticmethod
    def cabecalho_extrato():
        print("\n" + "="*40)
        print(f"{'EXTRATO BANCÁRIO':^40}")
        print("="*40)

    @staticmethod
    def cabecalho_conta(numero, nome_cliente):
        print(f"Conta: {numero}")
        print(f"Cliente: {nome_cliente}")
        print("-"*40)

    @staticmethod
    def rodape_extrato(saldo):
        print("="*40)
        print(f"{'Saldo atual:':<27} R$ {saldo:,.2f}")
        print("="*40 + "\n")

    @staticmethod
    def listar_contas(cliente_nome):
        print(f"\nContas de {cliente_nome}:")

    @staticmethod
    def nenhuma_conta():
        print("Nenhuma conta cadastrada.")

    @staticmethod
    def listar_agencias_do_banco(nome_banco):
        print(f"\nAgências do {nome_banco}:")

    @staticmethod
    def nenhuma_agencia():
        print("Não há agências cadastradas.")
        
    @staticmethod
    def agencia_detalhes(agencia):
        print(f"{agencia.nome} | Nº: {agencia.numero} | Endereço: {agencia.endereco} | Telefone: {agencia.fone}")
        
    @staticmethod
    def conta_enumerada(indice, conta):
        print(f"{indice}. {conta}")
        
    @staticmethod
    def mostrar_transacao(transacao: 'Transacao'):
        print(transacao)
        
    @staticmethod
    def senha_alterada():
        print("Senha alterada com sucesso!")
    
    @staticmethod
    def autenticacao_sucesso():
        print("Autenticação realizada com sucesso!")
    
    @staticmethod
    def autenticacao_falhou():
        print("Falha na autenticação: senha incorreta.")
    
    @staticmethod
    def erro_autenticacao(mensagem):
        print(f"Erro de autenticação: {mensagem}")

  
class Endereco:
    def __init__(self, cep: str, numero: str, rua: str, bairro: str, cidade: str, estado: str):
        self._cep = cep
        self._numero = numero
        self._rua = rua
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado

    def __str__(self):
        return f"{self._rua}, {self._numero}, {self._bairro}, {self._cidade} - {self._estado}, CEP: {self._cep}"
    
    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, value):
        self._cep = value

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def rua(self):
        return self._rua

    @rua.setter
    def rua(self, value):
        self._rua = value

    @property
    def bairro(self):
        return self._bairro

    @bairro.setter
    def bairro(self, value):
        self._bairro = value

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, value):
        self._cidade = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value       

class Transacao:
    def __init__(self, tipo: str, valor: float, conta: 'Conta'):
        self._tipo = tipo
        self._valor = valor
        self._conta = conta
        self._data = datetime.now()

    def __str__(self):
        data = self._data.strftime('%d/%m/%Y %H:%M')
        valor = f"R$ {self._valor:,.2f}"
        return f"{data} | {self._tipo:<10} | {valor.rjust(12)}"

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value):
        self._valor = value

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, value):
        self._conta = value

    @property
    def data(self):
        return self._data