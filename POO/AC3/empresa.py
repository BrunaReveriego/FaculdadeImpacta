# Programação Orientada a Objetos
# AC03 - Herança e polimorfismo
#
# Email Impacta: bruna.reveriego@aluno.faculdadeimpacta.com.br

import re

class Pessoa:
    """
    Expõe apenas para leitura os atributos públicos:
    + nome
    + idade

    e o método público:
    + aniversario()

    --> O nome e a idade da pessoa devem ser recebidos na inicialização
        do objeto e guardados em atributos não públicos.
        * Se nome não for string, levanta um TypeError
        * Se nome for vazio, levanta um ValueError
        * Se idade não for um inteiro, levanta um TypeError
        * Se idade for negativo, levanta um ValueError

    --> A exposição (pública) do nome e da idade deve ser feita através
        de properties, sem setter.

    --> O método aniversário não recebe nenhum argumento e incrementa
        o valor da idade em +1.
    """

    def __init__(self, nome, idade ):

        if not isinstance(nome,str):
            raise TypeError
        if nome == "":
            raise ValueError

        if not isinstance(idade,int):
            raise TypeError

        if idade < 0:
            raise ValueError    



        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
         return self._nome

    @property
    def idade(self):
         return self._idade

    def aniversario(self):
        self._idade = self._idade + 1

class Funcionario(Pessoa):
    """
    Expõe os atributos públicos:
    + email
    + carga_horaria

    E os métodos públicos:
    + calcula_salario()
    + aumenta_salario()

    Métodos (ou properties/setters) que tenham exatamente a mesma
    implementação em todas as classes filhas podem ser editados nesta classe,
    enquanto métodos (ou properties/setters) que tenham uma implementação
    específica devem ser editados nas classes filhas. Lembrando que se for
    necessário sobrescrever um setter, é necessário sobrescrever também a
    property relacionada.

    Exemplos:
    * a property/setter de email podem ser implementados nesta classe,
      pois a implementação não depende do subtipo de funcionários.
    * já a property/setter de carga_horaria deverão ser sobrescritos em cada
      uma das subclasses, pois as regras de validade da carga horária dependem
      do subtipo de funcionário.
    * aumenta_salario() terá a mesma implementação em todas as subclasses,
      pois o dissídio é de 5% sobre o valor da hora para todos os funcionários.
    * calcula_salario() terá uma implementação específica para cada tipo,
      pois dependendo da classe de funcionário, o cálculo segue regras diferentes.

      ATENÇÃO: Esta classe está simulando uma classe abstrata. Em Python isso pode
      ser feito herdando de uma classe chamada ABC, e métodos abstrados podem
      ser decorados com @abstractmethod. No entanto, isso não será cobrado nesta
      atividade e o comportamento está sendo simulado com o erro NotImplementedError,
      pois, caso o método não seja sobrescrito, uma chamada a ele irá levantar um
      erro informando que ele não foi devidamente implementado na classe filha.
      Essa classe não precisa implementar todos os métodos pois uma classe ser abstrata
      significa que ela não terá objetos criados diretamente a partir dela, servindo
      apenas de base para outras classes filhas, que essas sim terão objetos instanciados.

      tl;dr: implementem aqui os métodos com 'pass' e deixem os métodos com 'raise'
      como estão, pois eles serão sobrescritos (implementados) nas classes filhas.
    """
    def __init__(self, nome, idade, email, carga_horaria):
        """
        Construtor da classe Funcionário - lembre-se de usar o super para acessar
        o construtor da classe mãe e criar atributos que já estão definidos lá.
        Para o email e a carga horária, usem a property/setter aqui.

        O valor de carga_horaria é referente ao número de horas trabalhadas por semana
        """
        super().__init__(nome,idade)
        self.email = email
        self.carga_horaria = carga_horaria
   
    @property
    def email(self):
        """
        Retorna email do funcionário
        """
        return self._email

    @email.setter
    def email(self, novo_email):
        """
        Regras de validação:
        - Deve ser uma string, senão levanta um TypeError
        - Deve conter apenas letras, números, pontos e
          exatamente 1 símbolo @, senão levanta um ValueError.
        """
        if not isinstance(novo_email,str):
            raise TypeError

        verifica = re.match("^[a-zA-Z0-9.]*@[a-zA-Z0-9.]*$",novo_email)

        if not verifica:
            raise ValueError

        self._email = novo_email


    @property
    def carga_horaria(self):
        """
        Retorna a carga horária semanal de trabalho do funcionário.

        (não implementar aqui)
        """
        raise NotImplementedError

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        """
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, de acordo com o cargo, levanta um ValueError
        - Este método não possui retorno.

        (não implementar aqui)
        """
        raise NotImplementedError

    def calcula_salario(self):
        """
        Calcula e retorna o salário do mês para o funcionário.

        (não implementar aqui)
        """
        raise NotImplementedError

    def aumenta_salario(self):
        """
        Aplica um aumento de 5% no valor da hora trabalhada para o funcionário
        - Este método não possui retorno;
        """
   
        aumento = self._salario_hora * 5 / 100
        self._salario_hora += aumento

    @property
    def salario_hora(self):
        raise NotImplementedError

    @salario_hora.setter
    def salario_hora(self):
        raise NotImplementedError

"""
DICAS:

Se uma classe não possui um método definido, mas este método é definido em
alguma classe mãe acima, a classe irá herdar e usar tal método exatamente como
ele está definido na classe acima.

Isto também se aplica ao construtor, se Programador não define um __init__, então
esta classe está automaticamente usando o __init__ da classe Funcionário (se
funcionário tampouco definisse um __init__, então seria usado o de Pessoa, e se
pessoa tampouco o fizesse, seria usado o de `object`, que é a classe base do Python
herdada automaticamente por todas as classes que criamos, para garantir que tenham
os métodos básicos que se espera de um objeto em Python).

Caso você queira ou precise adicionar atributos extras na classe Programador
(ou qualquer outra classe filha de Funcionário), defina o método construtor,
faça a utilização do super e adicione os atributos extra que serão específicos
daquela classe, sejam eles recebidos por parâmetros ou não.

Lembrando que o enunciado define quais são os parâmetros obrigatórios
de uma classe, então se forem criados parâmetros obrigatórios extras, isso
irá gerar erros nos testes de correção.
"""


class Programador(Funcionario):
    """
    Funcionário do tipo Programador:
    - não recebe nenhum parâmetro extra;
    - salario base por hora: R$ 35.00;
    - regime de trabalho permitido: de 20h a 40h semanais (inclusive),
      caso contrário levanta um ValueError;
    - cálculo do sálario mensal, considere:
        * número de horas trabalhadas na semana;
        * sálario base (por hora);
        * o mês possui 4.5 semanas para efeitos desse cálculo.
    """
    def __init__(self,nome,idade,email,carga_horaria):
        super().__init__(nome,idade,email,carga_horaria)
        self._salario_hora = 35
        self.carga_horaria = carga_horaria

    @property
    def carga_horaria(self):
        return self._carga_horaria

    @carga_horaria.setter
    def carga_horaria(self,nova_carga_horaria):
        if nova_carga_horaria < 20 or nova_carga_horaria > 40:
            raise ValueError
        self._carga_horaria = nova_carga_horaria

   
    def calcula_salario(self):         
        return self._salario_hora * self.carga_horaria * 4.5

class Estagiario(Funcionario):
    """
    Funcionário do tipo Estagiario:
    - não recebe nenhum parâmetro extra;
    - salario base por hora: R$ 15.50;
    - auxilio alimentação mensal: R$ de 250.00;
    - regime de trabalho permitido: de 16h a 30h semanais (inclusive),
      caso contrário levanta um ValueError;
    - cálculo do sálario mensal, considere:
        * número de horas trabalhadas na semana;
        * sálario base (por hora);
        * o mês possui 4.5 semanas para efeitos desse cálculo;
        * auxílio alimentação mensal fixo;
    """
    def __init__(self,nome,idade,email,carga_horaria):
        super().__init__(nome,idade,email,carga_horaria)
        self._salario_hora = 15.5
        self._aux_alimentacao = 250
        self.carga_horaria = carga_horaria


    @property
    def carga_horaria(self):
        return self._carga_horaria

    @carga_horaria.setter
    def carga_horaria(self,nova_carga_horaria):
        if nova_carga_horaria < 16 or nova_carga_horaria > 30:
            raise ValueError

        self._carga_horaria = nova_carga_horaria

    def calcula_salario(self):         
        return (self._salario_hora * self.carga_horaria * 4.5 + self._aux_alimentacao)
        


class Vendedor(Funcionario):
    """
    Funcionário do tipo Vendedor:
    - não recebe nenhum parâmetro extra;

    - além dos métodos e atributos de Funcionário, deve:
      expor o atributo público, acessível apenas para leitura:
      + visitas
      e os métodos públicos:
      + realizar_visita()
      + zerar_visitas()

    - deve possuir um atributo não público que guarda o número de visitas
      realizadas no mês, começando sempre em zero no momento da criação do
      objeto. Esse atributo deve ser exposto publicamente pelo atributo `visitas`

    - salario base por hora: R$ 30.00;
    - auxilio alimentação mensal: R$ 350.00;
    - auxilio transporte por visita realizada: R$ 30.00;
    - regime de trabalho permitido: de 15h a 45h semanais (inclusive),
      caso contrário levanta um ValueError;

    - cálculo do sálario mensal, considere:
        * número de horas trabalhadas na semana;
        * sálario base (por hora);
        * o mês possui 4.5 semanas para efeitos desse cálculo;
        * auxílio alimentação mensal fixo;
        * auxilio transporte mensal variável, em função do número de visitas;
    """
    def __init__(self,nome,idade,email,carga_horaria):
        super().__init__(nome,idade,email,carga_horaria)
        self._salario_hora = 30
        self._aux_alimentacao = 350
        self._aux_transporte = 30
        self.carga_horaria = carga_horaria
        self.zerar_visitas()

    @property
    def carga_horaria(self):
        return self._carga_horaria

    @carga_horaria.setter
    def carga_horaria(self,nova_carga_horaria):
        if nova_carga_horaria < 15 or nova_carga_horaria > 45:
            raise ValueError
        self._carga_horaria = nova_carga_horaria

    def calcula_salario(self):
        return self._salario_hora * self.carga_horaria * 4.5 + self._aux_alimentacao + self.visitas * self._aux_transporte    


    @property
    def visitas(self):
        """
        Retorna o número de visitas realizadas pelo vendedor até o momento
        """
        return self._visitas

    def realizar_visita(self, n_visitas):
        """
        Recebe um número inteiro e incrementa o número de visitas realizadas no mês
        com o valor recebido. Antes de fazer a alteração, verifique:
        * se n_visitas é um número inteiro e levante um TypeError caso contrário;
        * se n_visitas está no intervalo de 0 a 10 (inclusive), levantando um ValueError caso contrário.

        - Este método não possui retorno;
        """
        if not isinstance(n_visitas,int):
            raise TypeError
        if n_visitas < 0 or n_visitas > 10:
            raise ValueError

        self._visitas = self._visitas + n_visitas

    def zerar_visitas(self):
        """
        Quando chamado deve redefinir o número de visitas realizadas pelo vendedor para zero,
        de modo a começar a contagem para o mês seguinte.
        - Este método não possui retorno;
        """
        self._visitas = 0


class EmpresaCreationError(Exception):
    """ Classe de erro personalizada, não editar"""
    pass


class Empresa:
    """
    Classe empresa, gerencia diversos funcionários

    Expõe os atributos públicos:
    + nome
    + cnpj
    + area_atuacao
    + equipe

    e os métodos públicos:
    + contrata()
    + folha_pagamento()
    + dissidio_anual()
    + listar_visitas()
    + zerar_visitas_vendedores()

    """
    def __init__(self, nome, cnpj, area_atuacao, equipe):
        """
        Construtor da classe empresa
        - nome, cnpj e area_atuação são strings
        - equipe é uma lista de funcionários (que podem ser de qualquer subtipo)
          e deve ser guardada em um atributo não público acessível apenas para leitura
          pelo atributo público `equipe`

        - Verifique as condições acima, isto é, se os parâmetros nome, cnpj e
          area_atuação são strings e se a lista de objetos passada no parâmetro equipe
          contem apenas objetos de algum tipo de funcionário. Caso ocorra qualquer
          problema na criação da empresa, devido a essas verificações, levante um
          EmpresaCreationError.

        DICA: a verificação da lista de funcionários pode ser feita usando o método
        público `contrata` e tratando para TypeError em um bloco try-except, e levantando
        o erro adequado.
        """
        self.nome = nome
        self.cnpj = cnpj
        self.area_atuacao = area_atuacao
        self._equipe = []
        
        try:
            for f in equipe:
                self.contrata(f)
        except TypeError:
            raise EmpresaCreationError


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,novo_nome):
        if not isinstance(novo_nome,str):
            raise EmpresaCreationError
        
        self._nome = novo_nome

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self,novo_cnpj):
        if not isinstance(novo_cnpj,str):
            raise EmpresaCreationError
        
        self._cnpj = novo_cnpj

    @property
    def area_atuacao(self):
        return self._area_atuacao

    @area_atuacao.setter
    def area_atuacao(self,novo_area_atuacao):
        if not isinstance(novo_area_atuacao,str):
            raise EmpresaCreationError
        
        self._area_atuacao = novo_area_atuacao    



    @property
    def equipe(self):
        """
        Retorna a lista com todos os funcionarios da empresa
        """
        return self._equipe

    def contrata(self, novo_funcionario):
        """
        Contrata um novo funcionário para a empresa (adicionando ele à lista de funcionários)

        - Verifica se novo_funcionario é um objeto de um dos subtipos de Funcionario,
          caso contrário levanta um TypeError

        DICA: Essa verificação pode ser feita usando o método isinstance(obj, cls) do Python,
        com a classe Funcionario, pois todas os objetos de uma subclasse de Funcionario também
        serão considerados instâncias de Funcionario.

        - Este método não possui retorno;
        """
        if not isinstance(novo_funcionario,Funcionario):
            raise TypeError

        self._equipe.append(novo_funcionario)


    def folha_pagamento(self):
        """
        Retorna o valor total gasto com o pagamento de todos os funcionários
        para o mês vigente

        DICA: Itere sobre a lista de funcionários, fazendo cada objeto do tipo
        Funcionário calcular seu próprio salário, acumule e retorne o resultado.
        """
        total_salario = 0

        for f in self.equipe:
            total_salario = total_salario + f.calcula_salario()

        return total_salario


    def dissidio_anual(self):
        """
        Aumenta o salário base por hora trabalhada com o dissídio padrão
        para todos os funcionários da empresa.
        - Este método não possui retorno;

        DICA: idem ao método de folha de pagamento, percorra a lista de funcionários e
        faça cada objeto funcionário aumentar o próprio salário base por hora.
        """
        for f in self.equipe:
            f.aumenta_salario()

    def listar_visitas(self):
        """
        Retorna um dicionário com as visitas realizadas por cada vendedor;
        Como a chave do dicionário precisa ser única, deve ser usado o email do vendedor
        e o valor deve ser o número de visitas realizadas por aquele funcionário.
        Exemplo:
            {
                'email_vendedor_1@email.ocm': <número de visitas aqui>,
                'email_vendedor_2@email.ocm': <número de visitas aqui>,
                'email_vendedor_3@email.ocm': <número de visitas aqui>
            }

        DICA: percorra a lista de funcionários e use a função `isinstance()` para verificar se
        o funcionário é um vendedor, em caso positivo, adicione as informações pedidas
        ao dicionário, e por fim retorne esse dicionário (não precisa guardar em um atributo).
        """
        for f in self.equipe:
            if isinstance(f,Vendedor):
                return {f.email : f.visitas}


    def zerar_visitas_vendedores(self):
        """
        Zera as visitas de todos os funcionário, use a dica do método listar_visitas e
        para cada vendedor, chame o método de zerar visitas do vendedor.
        - Este método não possui retorno;
        """
        for f in self.equipe:
            if isinstance(f,Vendedor):
                f.zerar_visitas()
