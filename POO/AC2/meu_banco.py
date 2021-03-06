# Programação Orientada a Objetos
# AC02 ADS-EaD - Criando classes
#
# Email Impacta: bruna.reveriego@aluno.faculdadeimpacta.com.br
                                                                                                                                                    
import re
class Cliente:45                        
    """
    Classe que modela os clientes do banco.

    expõe os atributos públicos:
    + nome
    + telefone
    + email

    e não expõe nenhum método público e não possui nenhum método não-público.

    --> O nome deve ser recebido na inicialização do objeto e ser guardado em
        um atributo não-público, não podendo ser alterado posteriormente, após
        o cliente ter sido criado. O valor do atributo deve ser acessado pelo
        identificador público `nome` (use uma @property para isso).

    --> Tanto o email quanto o telefone também precisam ser obrgatoriamente
        recebidos na inicialização e guardados em atributos não-públicos.
        O acesso externo deve ser feito pelos atributos públicos
        `telefone` e `email`, usando a property e o setter.

    Considerações ao atribuir o valor do telefone e do email, válidas
    tanto para a incialização do objeto quanto para uma eventual
    alteração posterior feita através do atributo público:
    * caso o email não seja uma string, levanta um TypeError;
    * caso o email não seja válido (verificar se contém um @) levanta um ValueError;
    * caso o telefone não seja uma string, levanta um TypeError.
    * caso o telefone não seja composto apenas por números, hífens, parênteses e
      espaços em branco, levanta um ValueError

    ------------------------------------------------------------------------
    Esta é a lista do que deve ser implementado nesta classe:
        --> o método __init__
        --> 3 def's com property
        --> 2 def's com setter

    Implemente os seguintes métodos, properties ou setters,
    de acordo com o que é pedido no enunciado.

    * Inicialização do objeto, como método especial __init__
        deve receber na inicialização os parâmetros:
            nome,
            telefone,
            email
    * Property do nome
    * Property do telefone
    * Setter do telefone
    * Property do email
    * Setter do email

    DICA: Para o atributo nome, faça a atribuição do valor recebido como
    parâmetro diretamente ao atributo não público (self._nome).
    Já para telefone e email, use o atributo exposto pelo setter (público)
    para fazer a atribuição no __init__, dessa forma, só é preciso fazer a
    validação em um único lugar.
    """

    def __init__(self, nome, telefone, email):
        self._nome = nome
        self.telefone = telefone
        self.email = email
      
    

    @property
    def nome(self):
        """Property do nome do cliente"""
        return self._nome

    @property
    def telefone(self):
        """Property do telefone do cliente"""
        return self._telefone
    



    @telefone.setter
    def telefone(self, novo_telefone):
        """
        Setter do telefone do cliente, caso não receba um número,
        levanta um TypeError
        """
        if not isinstance(novo_telefone, str):
            raise TypeError 

        
        for x in novo_telefone:
            if x not in ("0123456789-() "):
                raise ValueError
                
        
        self._telefone = novo_telefone  
               

    @property
    def email(self):
        """Property do email do cliente"""
        return self._email

    @email.setter
    def email(self, novo_email):
        """
        Setter do email do cliente, lançamento de exceções:
        levanta um TypeError caso não receba uma string; e
        levanta um ValueError caso não receba um email válido
        (considere o email válido se ele contiver exatamente
        1 símbolo de arroba - @)
        """
        if not isinstance(novo_email, str):
            raise TypeError

      
        tamanho = len(novo_email)
        verifica = False
        for x in range(tamanho):
            if novo_email[x] == '@':
                verifica = True

        if verifica == False:
            raise ValueError
         
        
        self._email = novo_email


class Conta:
    """
    A classe Conta deverá expor os atributos públicos:
    + clientes
    + numero
    + saldo

    E os métodos públicos:
    + sacar()
    + depositar()
    + tirar_extrato()

    --> A lista de clientes, o número da conta e o saldo inicial devem ser
        obrigatoriamente recebidos na inicialização do objeto e guardados
        em atributos não-públicos acessíveis apenas para leitura através dos
        atributos públicos mencionados acima, usando a property para isso.

    --> O saldo só poderá ser alterado pelos métodos sacar e depositar,
        não podendo ser alterado diretamente.

    --> O extrato da conta deverá ser uma lista e todas as operações feitas
        na conta (abertura da conta, saque e deposito) devem aparecer no
        extrato como tuplas, confome os exemplos da tabela a seguir:
        -------------------------------------------------
            operação       |    entrada no extrato
        ---------------------|---------------------------
        * abertura da conta  | ('saldo inicial', 1000)
        * saque              | ('saque', 100)
        * depósito           | ('deposito', 250)
        -------------------------------------------------
        As operações devem aparecer da ordem em que foram feitas, ou seja,
        o primeiro item da lista deverá sempre ser o de abertura da conta.

        DICA: Crie um atributo não-público para guardar as operações
              feitas na conta

    ------------------------------------------------------------------------
    Esta é a lista do que deve ser implementado nesta classe:
        --> o método __init__
        --> 3 def's com property
        --> 3 def's normais

    Implemente os seguintes métodos, properties ou setters,
    de acordo com o que é pedido no enunciado.

    * Inicialização do objeto, com o método especial __init__
        deve receber na inicialização os parâmetros:
            clientes,
            numero,
            saldo_inicial
        obs: clientes será uma lista com objetos do tipo <Clientes>
    * Property da lista de clientes
    * Property do saldo da conta
    * Property do numero da conta
    * Método sacar da classe Conta:
        * Caso o valor do saque seja maior que o saldo da conta,
          deve retornar um ValueError, e não efetuar o saque
        * Se o saque for efetuado, operação deve aparecer no extrato
    * Método depositar da classe Conta:
        * operação deve aparecer no extrato
    * Método tirar_extrato da classe Conta:
        * retorna uma lista com as operações (tuplas) executadas na Conta
    """
    def __init__(self, clientes, numero, saldo_inicial):
        self._clientes = clientes
        self._numero = numero
        self._saldo = saldo_inicial

        self._lista_operacoes = [("saldo inicial",saldo_inicial)]


    #properties

    @property
    def clientes(self):
        """Property de Clientes"""
        return self._clientes
    
    @property
    def numero(self):
        """Property de Numero"""
        return self._numero

    @property
    def saldo(self):
        """Property de Saldo"""
        return self._saldo

    def sacar(self, saque):
        if saque > self._saldo:
            raise ValueError
        else:
            self._saldo -= saque
            self._lista_operacoes.append(("saque",saque))

        
    def depositar(self,deposito):
        self._saldo += deposito
        self._lista_operacoes.append(("deposito",deposito))

    def tirar_extrato(self):
        return self._lista_operacoes

class Banco:
    """
    Classe que modela o banco

    Expõe os atributos públicos:
    + nome
    + contas

    Expõe o método público:
    + abrir_conta()

    --> O nome deve ser recebido na inicialização do objeto e guardado
        em um atributo não-público, acessível apenas para leitura
        através de uma property.

    --> Crie um atributo não-público que irá armazenar a lista das contas
        criadas no banco (os objetos do tipo <Conta>) e utilze esse atributo
        para calcular o número das novas contas do banco. A lista de contas
        deverá ser acessível apenas para leitura através de uma property.

    --> O método abrir_conta deverá abrir uma nova conta, sendo responsável por
        atribuir o numero da conta em ordem crescente, a partir de 1 para a
        primeira conta aberta.

    ----------------------------------------------------------------------------
    Esta é a lista do que deve ser implementado nesta classe:
        --> o método __init__
        --> 2 def's com property
        --> 1 def normal

    Implemente os seguintes métodos, properties ou setters,
    de acordo com o que é pedido no enunciado.

    * Inicialização do objeto, com o método especial __init__
        deve receber na inicialização o parâmetro:
            nome
    * Property do nome do banco.
    * Property da lista de contas do banco.
    * Método abrir_conta da classe Banco:
        recebe como parâmetros:
            --> a lista de clientes e
            --> o saldo inicial da conta,
        caso o saldo inicial seja negativo levanta um ValueError, e
        a conta não é aberta.

        DICA 1: O parâmetro clientes é uma lista com objetos do tipo <Cliente>.
        DICA 2: sobre a lista de contas
        - inicializar (no init) a lista de contas como uma lista vazia
          self._contas = []

        etapas do método abrir_conta():
        - receber os parâmetros pedidos no enunciado
        - se o saldo inicial for negativo, levantar um ValueError
        - calcular o número da conta com base na lista de contas
        - instanciar uma conta e adicioná-la à lista de contas
    """
    def __init__(self, nome):
        self._nome = nome
        self._contas = list()
    
    @property
    def nome(self):
        """Property de Nome"""
        return self._nome

    @property
    def contas(self):
        """Property de Contas"""
        return self._contas

    def abrir_conta(self,clientes,saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError
      
        numero_conta = len(self._contas) + 1
        self._contas.append(Conta(clientes,numero_conta,saldo_inicial))        



