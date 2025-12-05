from typing import List, TYPE_CHECKING
from auxiliares import Endereco, Notificacao

if TYPE_CHECKING:
    from conta import Conta

class Banco:
    def __init__(self, nome: str, cnpj: str, endereco: Endereco, fone: str) -> None:
        self._nome = nome
        self._cnpj = cnpj
        self._endereco = endereco
        self._fone = fone
        self._agencias: List['Agencia'] = []
        
    def __str__(self):
        return f"Banco: {self._nome}, CNPJ: {self._cnpj}, Endereço: {self._endereco}, Telefone: {self._fone}"

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, value):
        self._cnpj = value

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, value):
        self._endereco = value

    @property
    def fone(self):
        return self._fone

    @fone.setter
    def fone(self, value):
        self._fone = value

    def adicionar_agencia(self, *agencias: 'Agencia'):
        self._agencias.extend(agencias)
        
    def listar_agencias(self):
        Notificacao.listar_agencias_do_banco(self.nome)
        if not self._agencias:
            Notificacao.nenhuma_agencia()
        else:
            for agencia in self._agencias:
                Notificacao.agencia_detalhes(agencia)
                   
class Agencia:
    def __init__(self, nome: str, numero: str, endereco: Endereco, fone: str):
        self._nome = nome
        self._numero = numero
        self._endereco = endereco
        self._fone = fone
        self._contas: List['Conta'] = []
    
    def __str__(self):
        return f"Agência: {self._nome}, Número: {self._numero}, Endereço: {self._endereco}, Telefone: {self._fone}"
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, value):
        self._endereco = value

    @property
    def fone(self):
        return self._fone

    @fone.setter
    def fone(self, value):
        self._fone = value

    @property
    def contas(self):
        return self._contas
