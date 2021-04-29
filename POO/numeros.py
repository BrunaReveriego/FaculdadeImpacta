# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: __________@aluno.faculdadeimpacta.com.br


def eh_primo(n):
    """Função que verifica se um número é primo

    Recebe um número natural n, com n >= 2, e retorna verdadeiro se
    n é um número primo e falso caso contrário.

    Exemplos
    --------
    Um número é dito primo se possuir apenas 2 divisores, isto é,
    não possuir nenhum divisor além do 1 e do próprio n.
    29 é primo:
        divisores de 29: 1, 29
    30 NÃO é primo:
        divisores de 30: 1, 2, 3, 5, 6, 10, 15, 30

    Parâmetros
    ----------
    n : int
        Número natural a ser testado.

    Retorno
    -------
    bool
        True se n for um número primo e False caso contrário.
    """
    for i in range (2,n) :
        if n % i == 0:
            return False
        else: 
            return True    


    pass

# print(eh_primo(4))

def lista_primos(n):
    """Função que retorna uma lista de primos até n

    Recebe um número natural n, com n >= 2, e retorna uma
    lista com todos o números primos estritamente menores
    que n, em ordem crescente.

    Parâmetros
    ----------
    n : int
        Número natural que define o limite superior da lista.

    Retorno
    -------
    list
        itens : int
        descrição : Lista com todos os números primos menores
            que n, em ordem crescente.
    """
    


    x=3
    num_list = []
    num_list.append(2)
    while x < n:
        verifica = False
        y = 2
        while y < n:
            if x % y == 0 and y != x:
                verifica = True

            y=y+1
        if verifica == False:
            num_list.append(x)
                
        x=x+1        

    print(num_list)    

pass

# lista_primos(4)

def conta_primos(s):
    """Função que conta a quantidade de primos em uma sequẽncia

    Recebe uma sequência de números naturais s e retorna
    um dicionário com a contagem de ocorrências de cada número
    primo da sequência. Números não primos devem ser ignorados.
    Os números da sequência serão sempre maiores ou iguais a 2.

    Exemplos
    --------
    Caso s = [11, 2, 3, 4, 11, 2, 5, 2]
        O retorno deverá ser: {2: 3, 3: 1, 5: 1, 11: 2}
    Caso s = [1, 4, 8, 10]
        O retorno deverá ser: {}
    Caso s = (111, 191, 202, 306, 239, 579)
        O retorno deverá ser: {191: 1, 239: 1}

    Parâmetros
    ----------
    s : list | tuple
        itens : int
        descrição : Uma sequência arbitrária de números naturais.

    Retorno
    -------
    dict
        chave : int
        valor : int
        descrição : a chave é o número primo e o valor
            o total de ocorrências do número primo na
            sequência s.
    """
    x=0
    num_list = []

    while x < len(s):
        if s[x] == 2:
         num_list.append(s[x])
        else:      
         y = 2
         verifica = False
         while(y < int(s[x])):
            if int(s[x]) % y == 0 and y != int(s[x]):
                verifica = True
            y=y+1    
         if(verifica == False):
          num_list.append(s[x])
        x=x+1      

    print(num_list)

    y=0
    num_list2 = []

    while y < len(num_list):
        tamanho_lista = len(num_list)-1
        contagem = 1
        while tamanho_lista >= 0:
            if y != tamanho_lista:
                if num_list[y] == num_list[tamanho_lista]:
                    contagem = contagem + 1
                    # num_list.remove(num_list[tamanho_lista])
        
            tamanho_lista = tamanho_lista-1      

        num_list2.append(num_list[y] + ':' + str(contagem))
        y = y+1
    
    print(sorted(set(num_list2)))
    
    pass
   

# num_list = []
# sair = False

# while sair != True: 
#     num = input("Digite um número para sua lista : ") 
#     num_list.append(num)
    
#     verifica = input("Deseja sair? S/N")
#     if verifica == 'S':
#         sair = True

# conta_primos(num_list)


def eh_armstrong(n):
    """Função que verifica se um número é de Armstrong

    Recebe um número natural n, com n >= 0, e retorna
    verdadeiro se n é um número de Armstrong e falso
    caso contrário.

    Exemplos
    --------
    Um número é dito número de Armstrong se a soma de seus digitos
    elevados ao número total de digitos é igual a ele próprio
    53 é número de Armstrong:
        1**3 + 5**3 + 3**3 = 1 + 125 + 27 = 153
    4 é número de Armstrong:
        4 ** 1 = 4

    Parâmetros
    ----------
    n : int
        Número natural a ser testado.

    Retorno
    -------
    bool
        True se n for um número de Armstrong e False caso contrário.
    """
    stringn = str(n)
    tamanho_num = len(stringn)
    x = 0
    y = 0
    cont = 0
    soma = 0
    verifica = False

    while x < tamanho_num :
        cont = cont+1
        x=x+1

    while y < tamanho_num:
        soma = soma + ((int(stringn[y])) ** cont)
        y = y + 1

    if soma == n:
        verifica = True
        
    print(verifica)
    pass

# eh_armstrong(153)

def eh_quase_armstrong(n):
    """Função que verifica se um número é quase de Armstrong

    Recebe um número natural n, com n >= 0, e retorna
    verdadeiro se n atende aos seguintes critérios:

    1) não ser um número de Armstrong;
    2) o resultado da soma de seus digitos elevados ao número total
       de digitos é igual a ele próprio somado ou subtraído de 1.

    Exemplos
    --------
    35 é quase um número de Armstrong:
        3**2 + 5**2 = 9 + 25 = 34
    75 é quase um número de Armstrong:
        7**2 + 5**2 = 49 + 25 = 74

    Parâmetros
    ----------
    n : int
        Número natural a ser testado.

    Retorno
    -------
    bool
        True se n for um número quase de Armstrong e False caso contrário.
    """

    stringn = str(n)
    tamanho_num = len(stringn)
    x = 0
    y = 0
    cont = 0
    soma = 0
    verifica = False

    while x < tamanho_num :
        cont = cont+1
        x=x+1

    while y < tamanho_num:
        soma = soma + ((int(stringn[y])) ** cont)
        y = y + 1

    if soma+1 == n:
        verifica = True
        
    print(verifica)
    
    pass

eh_quase_armstrong(74)


def lista_armstrong(n):
    """Função que lista os números e Armstrong até n

    Recebe um número natural n e retorna uma lista com todos o
    números de Armstrong estritamente menores que n, em ordem crescente.

    Parâmetros
    ----------
    n : int
        Número natural que define o limite superior da lista.

    Retorno
    -------
    list
        itens : int
        descrição : Uma lista contendo todos os números de Armstrong
            menores que n, em ordem crescente.
    """





    
    pass


def eh_perfeito(n):
    """Função que verifica se um número é dito perfeito

    Recebe um número natural n, com n >= 2, e retorna verdadeiro se
    n é dito um número perfeito e falso caso contrário

    Exemplos
    --------
    Um número é dito perfeito se a soma de todos os divisores próprios é
    igual a ele mesmo.
    6 é um número perfeito:
        divisores próprios de 6: 1, 2, 3
        1 + 2 + 3 = 6
    12 NÃO é um número perfeito:
        divisores próprios de 12: 1, 2, 3, 4, 6
        1 + 2 + 3 + 4 + 6 = 16

    Parâmetros
    ----------
    n : int
        Número natural a ser testado.

    Retorno
    -------
    bool
        True se n for um número perfeito e False caso contrário.
    """
    pass


def lista_perfeitos(n):
    """Função que lista os números ditos perfeitos até n

    Recebe um número natural n, com n >= 2, e retorna uma lista
    com todos os números perfeitos estritamente menores que n,
    em ordem crescente.

    Parâmetros
    ----------
    n : int
        Número natural que define o limite superior da lista.

    Retorno
    -------
    list
        itens : int
        descrição : Uma lista contendo todos os números perfeitos
            menores que n em ordem crescente.
    """
    pass