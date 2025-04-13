# Projeto de Compactação de Arquivos
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

Este projeto fornece um script que permite ao usuário criar um arquivo de texto contendo um texto repetido um número especificado de vezes e, em seguida, compactar esse arquivo em um formato ZIP.
O script exibe o tamanho do arquivo original e o tamanho do arquivo compactado, permitindo que o usuário veja a eficiência da compactação.
Ainda está bem ***cru***, será usado em outros futuros projetos como uma alternativa open-source criada por mim.

## Funcionalidades

- **Entrada do Usuário**: O usuário pode ***inserir*** um texto e o número de vezes que deseja que esse texto seja repetido.
- **Compactação**: O arquivo de texto é compactado em um arquivo ZIP, e o tamanho do arquivo original e do arquivo compactado é exibido.

## Novas Funcionalidades:

   - Compactação de Arquivos:
        - A função compactar_arquivo lê o conteúdo de um arquivo e o compacta.
        - A função descompactar_arquivo descompacta os dados e os salva em um novo arquivo.

   - Escolha do Usuário:
        - O usuário pode escolher entre compactar texto ou um arquivo. Dependendo da escolha, o programa executa a lógica apropriada.

   - Verificação de Arquivo:
        - O código verifica se o caminho do arquivo fornecido pelo usuário é válido antes de tentar compactá-lo.

## Como Usar:
   - Execute o script e escolha se deseja compactar um texto ou um arquivo.
   - Para a opção de texto, insira o texto e o número de repetições.
   - Para a opção de arquivo, forneça o caminho do arquivo que deseja compactar e o caminho onde deseja salvar o arquivo descompactado.


## Melhorias

- Interface: talvez tenha uma interface simples para melhorar a usuabilidade do usuário
- Funções: compactaçoes mais seguras (***criptografar e depois compactar***)

## Instalação e execução

   ```bash
   git clone https://github.com/Rodrigo-Kelven/Script_Compression
   cd Script_Compression
   python script_compression.py
   ```
# Contribuições

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir um issue ou enviar um pull request.;)

## Autores

- [@Rodrigo_Kelven](https://github.com/Rodrigo-Kelven)
