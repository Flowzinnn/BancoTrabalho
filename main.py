from datetime import date
from auxiliares import Endereco
from pessoas import Cliente
from contas import Conta_Corrente, Conta_Poupanca
from banco import Banco, Agencia   

def main():
    
    # Endereço Banco
    enderecoBancoWolf = Endereco("122312", "123", "rua a", "bairro b", "tree lake city", "MS")
    enderecoAgenciaSul = Endereco("123121", "1323", "rua b", "bairro a", "tree lake city", "MS")
    
    # Criando as contas
    clienteNicolas = Cliente("Nicolas", "123.456.789-00", date(2003, 5, 10), "000000000")
    contaCorrenteNicolas001 = Conta_Corrente("001", clienteNicolas, 1000.0, "1234", 1000)
    contaPoupancaNicolas001 = Conta_Poupanca("001", clienteNicolas, 15000, "2508", 0.5)

    # Realizando operações
    contaCorrenteNicolas001.depositar(500)
    contaCorrenteNicolas001.sacar(150)

    # Imprimindo extrato
    contaCorrenteNicolas001.extrato()

    # Mostrando as contas do cliente
    clienteNicolas.listar_contas()


    agenciaSul = Agencia("Agência Sul", "001", enderecoAgenciaSul, "(11) 12345-6789")

    bancoWolf = Banco("Banco Wolf", "12.345.678/0001-90", enderecoBancoWolf, "(11) 98765-4321")

    bancoWolf.adicionar_agencia(agenciaSul)

    print(bancoWolf)

    bancoWolf.listar_agencias()

if __name__ == '__main__':
    main()