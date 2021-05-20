# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: bruna.reveriego@aluno.faculdadeimpacta.com.br


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
        
    return True    


    pass



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

    return num_list    

pass



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
    num_list2 = {}

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

    # print(num_list)

    y=0
  

    while y < len(num_list):
        tamanho_lista = len(num_list)-1
        contagem = 1
        while tamanho_lista >= 0:
            if y != tamanho_lista:
                if num_list[y] == num_list[tamanho_lista]:
                    contagem = contagem + 1
                    # num_list.remove(num_list[tamanho_lista])
        
            tamanho_lista = tamanho_lista-1      

        num_list2[num_list[y]] = contagem
       
        # num_list2.append(num_list[y] + ':' + str(contagem))
        y = y+1
    
    # return (sorted(set(num_list2)))
    
    return num_list2

    pass
   

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
        
    return verifica
    pass


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
        
    return verifica
    
    pass



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
    x = 0
    num_list = []
    while x < n:
        stringn = str(x)
        tamanho_num = len(stringn)
    
        z = 0
        y = 0
        cont = 0
        soma = 0
  

        while z < tamanho_num :
            cont = cont+1
            z=z+1

        while y < tamanho_num:
            soma = soma + ((int(stringn[y])) ** cont)
            y = y + 1

        if soma == x:
            num_list.append(x)

        x=x+1 

    return num_list


    
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
    lista_num = []
    x = 1
    y = 0
    soma = 0
    verifica = False

    while x < n:
        if n % x == 0:
            lista_num.append(x)
        x = x+1

    tamanho_lista = len(lista_num)

    while y < tamanho_lista:
        soma = soma + lista_num[y]
        y = y + 1

    if soma == n:
        verifica = True

    return verifica

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
    x = 2
    num_perfeitos = []
    while x < n:
        y = 1
        z=0
        soma = 0
        num_list = []
        while y < x:
            if x % y == 0:
                num_list.append(y)
            y = y + 1

        tamanho_lista = len(num_list)

        while z < tamanho_lista:
            soma = soma + num_list[z]
            z = z + 1
               
        if soma == x:
            num_perfeitos.append(x)

        x = x + 1


    return num_perfeitos


    pass

