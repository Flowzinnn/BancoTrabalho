from typing import List, TYPE_CHECKING
from abc import abstractmethod
import hashlib
from interfaces import Autenticavel
from auxiliares import Transacao, Notificacao
from excecoes import Exceptions

if TYPE_CHECKING:
    from pessoas import Cliente

#Classe Abstrata/Abstract class : CLASSES ABSTRATAS NUNCA IRÃO GERAR UM OBJETO;
class Conta(Autenticavel):
    def __init__(self, numero: str, cliente: 'Cliente', saldo: float, senha: str):
        self._numero = numero
        self._cliente = cliente
        self._saldo = saldo 
        self._senha = self._criptografar_senha(senha)
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
        
    @abstractmethod
    def sacar(self, valor: float):
        pass

    @abstractmethod
    def aplicar_taxas(self):
        pass

    def _criptografar_senha(self, senha: str) -> str:
        """Criptografa a senha usando SHA-256"""
        if not senha or len(str(senha)) < 4:
            raise ValueError("Senha deve ter pelo menos 4 caracteres")
        return hashlib.sha256(senha.encode()).hexdigest()

    def autenticar(self, senha: str) -> bool:
        """Autentica comparando hash da senha fornecida com a armazenada"""
        senha_hash = self._criptografar_senha(senha)
        return self._senha == senha_hash
    
    def alterar_senha(self, senha_antiga: str, senha_nova: str) -> bool:
        """Altera a senha após autenticar com a senha antiga"""
        if not self.autenticar(senha_antiga):
            raise Exceptions.AutenticacaoError("Senha antiga incorreta")
        
        self._senha = self._criptografar_senha(senha_nova)
        return True
        
    def depositar(self, valor: float):
        try:
            Exceptions.validar_valor_positivo(valor)
            self._saldo += valor
            transacao = Transacao("Depósito", valor, self)
            self._transacoes.append(transacao)
            Notificacao.deposito(valor)
        except Exceptions.ValorInvalidoError as e:
            print(f"Erro: {e}")
    
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
