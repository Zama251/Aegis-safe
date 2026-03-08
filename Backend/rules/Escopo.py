import os
os.system('cls') # Só usei isso por que não sou fã do terminal cheio de informação(caso esse não funcione no seu, alterar 'cls' para 'clear')


def TestarSeguranca(senha):
    erro = 0 # caso a senha tenha algum caractere que não está no código
    soma = 0 # numero medio de possibilidades de tentativas para acertar a senha
    letraErro = [] # o caractere que terá feito o erro, se tiver erro

    # base para ver quantos desse elemento terá a senha
    caracEsp = 0
    numero = 0
    letraMaiu = 0
    letraMin = 0 
    
    # lista dos caracteres que pode conter, (se quiser adicionar mais caracteres especiais, ainda funciona)
    ListNumero = ['1','2','3','4','5','6','7','8','9','0']
    ListCaracEsp = ['!','@','#','$','%','&','*','(',')','ç',',','+','=','_','-',';',':','.','/',']','[','{','}','<','>']
    ListLetraMin = ['a','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p','z','x','c','v','b','n','m']
    ListLetraMaiu = ['A','S','D','F','G','H','J','K','L','Q','W','E','R','T','Y','U','I','O','P','Z','X','C','V','B','N','M']
    t = 0 # Um contador de caracteres
    for n in senha: # pega o numero de caracteres na senha
        t += 1 # adiciona um ao contador a cada caractere
        if n in ListLetraMin: # testa se esta em uma das listas
            letraMin += 1 # adiciona um ao tipo de caractere que esse estiver
        elif n in ListLetraMaiu:
            letraMaiu += 1
        elif n in ListNumero:
            numero += 1
        elif n in ListCaracEsp:
            caracEsp += 1
        else: # Se não estiver em nenhuma lista, da erro
            erro = 1
            letraErro.append(n) # Adiciona o caractere que deu erro à lista de erros
    
    # Segurança básica (Escopo do próprio Google), 8 caracteres, letra maiuscula, caractere especial, numero.
    if t < 8: 
        print("Sua senha tem que ter pelo menos 8 caracteres.")
    elif erro: # Avisa que o codigo nao aceita tal caractere ainda(ex: 'á', ''', '\' e tals)
        print(f'Sinto muito, mas esse código ainda não aceita {letraErro} como caracter especial, altere.')
    elif numero == 0:
        print('Adicione pelo menos um número a sua senha.')
    elif letraMaiu == 0:
        print('Adicione pelo menos uma letra maiúscula a sua senha.')
    elif caracEsp == 0:
        print('Adicione pelo menos um caractere especial a sua senha.')

    if numero != 0: # Se tiver algum numero
        soma += 5 ** numero # Adiciona a media dos numeros(geralmente computadores começam tentando senhas só com números)
    if letraMin != 0:
        soma += 23 ** letraMin # Se o computador passou todos os numeros(10), tentara as minusculas em seguida, pela media ser 13, tem em media 23 tentativas de quebrar uma senha com uma letra
    if letraMaiu != 0:
        soma += 49 ** letraMaiu # E assim por diante...
    if caracEsp != 0:
        apoio = (len(ListCaracEsp) // 2) + 62 # (len(ListCaracEsp) // 2) foi uma forma de conseguir a media de todos os elementos na lista dde caracteres especiais, sem ficar decimal
        soma += apoio ** caracEsp #Apoio foi para ajudar e nao confundir na hora de mudar no futuro, já tudo aquilo é elevado ao numero de caracteres desse tipo
    
    if erro:
        soma = 'infinitas' #Se der erro, ou seja, tiver um caractere que não esta no codigo, demorariam infinitas tentativas para um computador que tem os caracteres, conseguir quebrar a senha
    return soma #Retorna o numero de tentativas


while True:
    print(26**8)
    senha = str(input('Senha: ')) # Pede uma senha para julgar
    tentativas = TestarSeguranca(senha) # Chama a função de testar a segurança
    print(f'Um computador levaria cerca de {tentativas} tentativas para quebrar sua senha.') # Textinho pra ficar bonitinho
    a = str(input('...')) # Dá o tempo para raciocinar
    if a == 'exit': #escrever 'exit' para sair do programa
        break

# Só lembrar que mesmo se o computador soubesse que são 8 digitos 
# e que só tem letras minúsculas,
# ainda assim iriam ser 26^8 combinações, ou seja, 208827064576 possibilidades.
# Então não se assuste com os números kkkkk