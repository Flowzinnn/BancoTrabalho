from datetime import datetime
from conta import Conta
from interfaces import Tributavel, Rentavel
from auxiliares import Transacao, Notificacao

class Conta_Corrente(Conta, Tributavel):
    def __init__(self, numero: str, cliente: 'Cliente', saldo: float, senha: str, limite: float):
        super().__init__(numero, cliente, saldo, senha)
        self._limite = limite
        self._taxa_manutencao = 10.0
        
    def __str__(self):
        return f"💳 Conta Corrente Nº {self.numero} | Saldo: R$ {self.saldo:,.2f} | Limite: R$ {self.limite:,.2f}"


    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, value):
        self._limite = value
     
    def sacar(self, valor: float):
        if valor <= 0:
            Notificacao.erro_valor_invalido()
            return

        if valor > self._saldo + self._limite:
            Notificacao.erro_limite_excedido()
            return

        self._saldo -= valor
        transacao = Transacao("Saque", valor, self)
        self._transacoes.append(transacao)
        Notificacao.saque(valor)

    def aplicar_taxas(self):
        self._saldo -= self._taxa_manutencao
        transacao = Transacao("Taxa manutenção", self._taxa_manutencao, self)
        self._transacoes.append(transacao)
        Notificacao.taxa_manutencao(self._taxa_manutencao)
    
    def get_valor_imposto(self) -> float:
        return self.saldo * 0.07    
    
class Conta_Poupanca(Conta, Rentavel):
    def __init__(self, numero: str, cliente: 'Cliente', saldo: float, senha: str, taxa_rendimento: float):
        super().__init__(numero, cliente, saldo, senha)
        self._taxa_rendimento = taxa_rendimento
        self._data_aniversario = datetime.now().day
        
    def __str__(self):
        return f"🏦 Conta Poupança Nº {self.numero} | Saldo: R$ {self.saldo:,.2f} | Rendimento: {self.taxa_rendimento:.2f}%"

    def sacar(self, valor: float):
        if valor <= 0:
            Notificacao.erro_valor_invalido()
            return

        if valor > self._saldo:
            Notificacao.erro_saldo_insuficiente()
            return

        self._saldo -= valor
        transacao = Transacao("Saque", valor, self)
        self._transacoes.append(transacao)
        Notificacao.saque(valor)

    def aplicar_taxas(self):
        # Poupança geralmente não tem taxa, mas só pra cumprir o método
        Notificacao.sem_taxa_poupanca()
        
    def get_rendimento(self) -> float:
        rendimento = self.saldo * (self.taxa_rendimento / 100)
        return rendimento

    @property
    def taxa_rendimento(self):
        return self._taxa_rendimento

    @taxa_rendimento.setter
    def taxa_rendimento(self, value):
        self._taxa_rendimento = value

    @property
    def data_aniversario(self):
        return self._data_aniversario

    @data_aniversario.setter
    def data_aniversario(self, value):
        self._data_aniversario = value
