class Exceptions:
    """
    Centraliza as exceções de domínio do sistema bancário
    e oferece métodos auxiliares de validação.
    """

    # ===================== CLASSES DE EXCEÇÃO ===================== #

    class BancoError(Exception):
        """Exceção base para o domínio bancário."""
        pass

    class ValorInvalidoError(BancoError):
        """Lançada quando o valor informado é menor ou igual a zero."""
        pass

    class SaldoInsuficienteError(BancoError):
        """Lançada quando o saldo não é suficiente para a operação."""
        pass

    class LimiteExcedidoError(BancoError):
        """Lançada quando o valor solicitado ultrapassa saldo + limite."""
        pass

    class AutenticacaoError(BancoError):
        """Lançada quando a autenticação de uma conta falha."""
        pass

    # ===================== MÉTODOS ESTÁTICOS DE VALIDAÇÃO ===================== #

    @staticmethod
    def validar_valor_positivo(valor: float) -> None:
        
        if valor <= 0:
            raise Exceptions.ValorInvalidoError(
                "Valor informado deve ser maior que zero."
            )

    @staticmethod
    def validar_saque_poupanca(saldo: float, valor: float) -> None:
        
        Exceptions.validar_valor_positivo(valor)

        if valor > saldo:
            raise Exceptions.SaldoInsuficienteError(
                "Saldo insuficiente para realizar o saque."
            )

    @staticmethod
    def validar_saque_corrente(saldo: float, limite: float, valor: float) -> None:
        
        Exceptions.validar_valor_positivo(valor)

        if valor > (saldo + limite):
            raise Exceptions.LimiteExcedidoError(
                "Valor do saque excede o limite disponível da conta."
            )

    @staticmethod
    def validar_autenticacao(autenticado: bool) -> None:

        if not autenticado:
            raise Exceptions.AutenticacaoError("Falha na autenticação: senha inválida.")
