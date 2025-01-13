import zlib

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

if __name__ == "__main__":
    # Exemplo de uso
    print("--------------------------------------------------------------------------")    
    texto = str(input("Digite um texto para ser compactado: "))
    print(f"Texto digitado: {texto}")
    print("--------------------------------------------------------------------------")
    repeticao_texto = int(input("Digite o numero para a repetição do texto inserido: "))
    print(f"Quantidade de vezes que o texto será repetido: {repeticao_texto}")
    print("--------------------------------------------------------------------------")
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
