import os
import string
# Só usei isso por que não sou fã do terminal cheio de informação(caso esse não funcione no seu, alterar 'cls' para 'clear')


def testar_Seguranca(Senha):
    Erro = 0 # caso a Senha tenha algum caractere que não está no código
    Soma = 0 # Numero medio de possibilidades de Tentativas para acertar a Senha
    letraErro = [] # o caractere que terá feito o Erro, se tiver Erro

    # base para ver quantos desse elemento terá a Senha
    caracterEspecial = 0
    Numero = 0
    letrasMaiusculas = 0
    letrasMinusculas = 0 
    
    # lista dos caracteres que pode conter, (se quiser adicionar mais caracteres especiais, ainda funciona)
    Lista_de_Numeros = ['1','2','3','4','5','6','7','8','9','0']
    lista_de_Caracter_Especial = ['!','@','#','$','%','&','*','(',')','ç',',','+','=','_','-',';',':','.','/',']','[','{','}','<','>']
    lista_de_Letras_Minusculas = ['a','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p','z','x','c','v','b','n','m']
    lista_de_Letras_Maiusculas = ['A','S','D','F','G','H','J','K','L','Q','W','E','R','T','Y','U','I','O','P','Z','X','C','V','B','N','M']
    t = 0 # Um contador de caracteres
    for n in Senha: # pega o Numero de caracteres na Senha
        t += 1 # adiciona um ao contador a cada caractere
        if n in lista_de_Letras_Minusculas: # testa se esta em uma das listas
            letrasMinusculas += 1 # adiciona um ao tipo de caractere que esse estiver
        elif n in lista_de_Letras_Maiusculas:
            letrasMaiusculas += 1
        elif n in Lista_de_Numeros:
            Numero += 1
        elif n in lista_de_Caracter_Especial:
            caracterEspecial += 1
        else: # Se não estiver em nenhuma lista, da Erro
            Erro = 1
            letraErro.append(n) # Adiciona o caractere que deu Erro à lista de Erros
    
    # Segurança básica (Escopo do próprio Google), 8 caracteres, letra maiuscula, caractere especial, Numero.
    if t < 8: 
        print("Sua Senha tem que ter pelo menos 8 caracteres.")
    elif Erro: # Avisa que o codigo nao aceita tal caractere ainda(ex: 'á', ''', '\' e tals)
        print(f'Sinto muito, mas esse código ainda não aceita {letraErro} como caracter especial, altere.')
    elif Numero == 0:
        print('Adicione pelo menos um número a sua Senha.')
    elif letrasMaiusculas == 0:
        print('Adicione pelo menos uma letra maiúscula a sua Senha.')
    elif caracterEspecial == 0:
        print('Adicione pelo menos um caractere especial a sua Senha.')

    if Numero != 0: # Se tiver algum Numero
        Soma += 5 ** Numero # Adiciona a media dos numeros(geralmente computadores começam tentando senhas só com números)
    if letrasMinusculas != 0:
        Soma += 23 ** letrasMinusculas # Se o computador passou todos os numeros(10), tentara as minusculas em seguida, pela media ser 13, tem em media 23 Tentativas de quebrar uma Senha com uma letra
    if letrasMaiusculas != 0:
        Soma += 49 ** letrasMaiusculas # E assim por diante...
    if caracterEspecial != 0:
        apoio = (len(lista_de_Caracter_Especial) // 2) + 62 # (len(lista_de_Caracter_Especial) // 2) foi uma forma de conseguir a media de todos os elementos na lista dde caracteres especiais, sem ficar decimal
        Soma += apoio ** caracterEspecial #Apoio foi para ajudar e nao confundir na hora de mudar no futuro, já tudo aquilo é elevado ao Numero de caracteres desse tipo
    
    if Erro:
        Soma = 'infinitas' #Se der Erro, ou seja, tiver um caractere que não esta no codigo, demorariam infinitas Tentativas para um computador que tem os caracteres, conseguir quebrar a Senha
    return Soma #Retorna o Numero de Tentativas


while True:
    print(26**8)
    Senha = str(input('Senha: ')) # Pede uma Senha para julgar
    Tentativas = testar_Seguranca(Senha) # Chama a função de testar a segurança
    print(f'Um computador levaria cerca de {Tentativas} Tentativas para quebrar sua Senha.') # Textinho pra ficar bonitinho
    a = str(input('...')) # Dá o tempo para raciocinar
    if a == 'exit': #escrever 'exit' para sair do programa
        break

# Só lembrar que mesmo se o computador soubesse que são 8 digitos 
# e que só tem letras minúsculas,
# ainda assim iriam ser 26^8 combinações, ou seja, 208827064576 possibilidades.
# Então não se assuste com os números kkkkk