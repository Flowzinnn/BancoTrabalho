from datetime import date
from typing import List, TYPE_CHECKING
from pessoa import Pessoa
from auxiliares import Notificacao

if TYPE_CHECKING:
    from conta import Conta

class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: date, cnh: str):
        super().__init__(nome, cpf, data_nascimento)
        self._cnh = cnh
        self._contas: List['Conta'] = []
        
    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf}"


    @property
    def cnh(self):
        return self._cnh

    @cnh.setter
    def cnh(self, value):
        self._cnh = value

    @property
    def contas(self):
        return tuple(self._contas)

    def adicionar_conta(self, conta: 'Conta'):
        self._contas.append(conta)
        
    def listar_contas(self):
        Notificacao.listar_contas(self.nome)
        if not self._contas:
            Notificacao.nenhuma_conta()
        else:
            for i, conta in enumerate(self._contas, 1):
                Notificacao.conta_enumerada(i, conta)

class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: date, cargo: str, matricula: str, salario: float):
        super().__init__(nome, cpf, data_nascimento)
        self._cargo = cargo
        self._matricula = matricula
        self._salario = salario

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        self._cargo = value

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, value):
        self._matricula = value

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, value):
        if value < 0:
            raise ValueError("Salário não pode ser negativo")
        self._salario = value
