#Código que requisita a entrada de data de nascimento do usuário, para retornar seu signo e horóscopodo do dia.

#Define a função "remover_acentos" para fazer o seguinte:
def remover_acentos(texto):
    #Importa a função "normalize", para concertar palavras com acentos.
    from unicodedata import normalize

    #Usa o "normalize" para tirar acentos do texto e corrige com o padrão ASCII(American Standar Code for Information Interchange)
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

#Define a função "separa_data" para obter a data de nascimento inserida pelo usuário no formato requirido para funcionamento do código.
def separar_data(dma):
    #Adquire o ano da data inserida, usando os últimos 4 digitos.
    a = dma % 10000
    dma //= 10000

    #Adquire o mês da data inserida, usando os 2 digitos antes do ano.
    m = dma % 100
    dma //= 100

    #Adquire o dia da data inserida, usando os primeiros dois dígitos.
    d = dma

    #Retorna dia, mês e ano, respectivamente, da data inserida, no formato necessário pro funcionamento do código.
    return d, m, a

#Define a função "signo", que usa dia e mês inseridos para retornar o signo do usuário.
def signo(dia, mes):
    if mes == 3:
        return 'Peixes' if dia < 21 else 'Áries'
    if mes == 4:
        return 'Áries' if dia < 20 else 'Touro'
    if mes == 5:
        return 'Touro' if dia < 22 else 'Gêmeos'
    if mes == 6:
        return 'Gêmeos' if dia < 23 else 'Câncer'
    if mes == 7:
        return 'Câncer' if dia < 23 else 'Leão'
    if mes == 8:
        return 'Leão' if dia < 23 else 'Virgem'
    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
    if mes == 11:
        return 'Escorpião' if dia < 22 else 'Sagitário'
    if mes == 12:
        return 'Sagitário' if dia < 22 else 'Capricórnio'
    if mes == 1:
        return 'Capricórnio' if dia < 20 else 'Aquário'
    if mes == 2:
        return 'Aquário' if dia < 19 else 'Peixes'

#Define a função "horoscopo", que busca o horóscopo do dia, do signo do usuário.
def horoscopo(signo_desejado):
    #Importa o módulo que define funções e classes que ajudam a abrir URLs.
    import urllib.request

    #Remove os acentos do signo e transforma a string em minúsculo.
    signo_formatado = remover_acentos(signo_desejado).lower()

    #Define o site que vai ser buscado o horóscopo, adicionando o signo ao link, para obter o horóscopo do signo do usuário.
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado

    #Estabelece um header HTTP personalizado para o pedido enviado ao servidor.
    requisicao = urllib.request.Request(
        url = minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
        )

    #Abre o link definido anteriormente.
    resposta = urllib.request.urlopen(requisicao)

    #Lê o conteúdo da página em UTF-8.
    pagina = resposta.read().decode('utf-8')

    #Procura o início e final do texto.
    marcador_inicio = '<p class="text-pred">'
    marcador_final = '</p>'

    #Procura o início e final da página.
    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    #Retorna o signo e o texto do horóscopo da página.
    return signo_desejado + ': ' + pagina[inicio:final]

#Define a função "main" para requisitar ao usuário a data de nascimento e seu horóscopo.
def main():
    # Entrada de dados
    nascimento = int(input("Digite sua data de nascimento no formato DDMMAAAA: "))

    # Processamento
    dia, mes, _ = separar_data(nascimento)
    meu_signo = signo(dia, mes)
    horoscopo_de_hoje = horoscopo(meu_signo)

    # Saída de dados
    print((horoscopo_de_hoje))

#Código para ajudar a proteger o usuário de invocar o script quando não for a intenção.
if __name__ == '__main__':
    main()