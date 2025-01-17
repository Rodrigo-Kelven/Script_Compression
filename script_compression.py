import zlib
import os

def compactar_dados(dados):
    """Compacta os dados usando zlib."""
    # Converte os dados para bytes, se necessário
    if isinstance(dados, str):
        dados = dados.encode('utf-8')
    
    # Compacta os dados
    dados_compactados = zlib.compress(dados)
    return dados_compactados

def descompactar_dados(dados_compactados):
    """Descompacta os dados usando zlib."""
    # Descompacta os dados
    dados_descompactados = zlib.decompress(dados_compactados)
    return dados_descompactados.decode('utf-8')

def compactar_arquivo(caminho_arquivo):
    """Compacta o conteúdo de um arquivo."""
    with open(caminho_arquivo, 'rb') as arquivo:
        dados = arquivo.read()
    return compactar_dados(dados)

def descompactar_arquivo(dados_compactados, caminho_destino):
    """Descompacta os dados e salva em um arquivo."""
    dados_descompactados = zlib.decompress(dados_compactados)
    with open(caminho_destino, 'wb') as arquivo:
        arquivo.write(dados_descompactados)

if __name__ == "__main__":
    print("--------------------------------------------------------------------------")
    escolha = input("Você deseja (1) compactar texto ou (2) compactar arquivo? (Digite 1 ou 2): ")

    if escolha == '1':
        texto = input("Digite um texto para ser compactado: ")
        print(f"Texto digitado: {texto}")
        repeticao_texto = int(input("Digite o número para a repetição do texto inserido: "))
        texto_original = f"{texto}" * repeticao_texto  # Texto repetido para aumentar o tamanho
        print(f"Tamanho original: {len(texto_original.encode('utf-8'))} bytes")

        # Compacta os dados
        dados_compactados = compactar_dados(texto_original)
        print(f"Tamanho compactado: {len(dados_compactados)} bytes")

        # Descompacta os dados
        texto_descompactado = descompactar_dados(dados_compactados)
        print(f"Tamanho após descompactação: {len(texto_descompactado.encode('utf-8'))} bytes")
        print("--------------------------------------------------------------------------")
        print(f"Texto descompactado: {texto_descompactado}")

    elif escolha == '2':
        caminho_arquivo = input("Digite o caminho do arquivo que deseja compactar: ")
        if os.path.isfile(caminho_arquivo):
            dados_compactados = compactar_arquivo(caminho_arquivo)
            print(f"Arquivo compactado com sucesso! Tamanho compactado: {len(dados_compactados)} bytes")

            caminho_destino = input("Digite o caminho para salvar o arquivo descompactado: ")
            descompactar_arquivo(dados_compactados, caminho_destino)
            print(f"Arquivo descompactado e salvo em: {caminho_destino}")
        else:
            print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")
