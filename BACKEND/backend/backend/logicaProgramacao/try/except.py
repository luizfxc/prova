#Em Python, a estrutura try/except é usada para tratar
# exceções, que são erros que podem ocorrer durante a execução do código. O bloco try contém o código que pode gerar um erro.
# Se uma exceção ocorrer nesse bloco, o código dentro do except correspondente é executado para lidar com a situação,
# evitando que o programa interrompa abruptamente sua execução

#Em Python, a estrutura try-except é usada para tratar erros e exceções durante a execução do código.
# O bloco try contém o código que pode gerar um erro. Se um erro ocorrer dentro do bloco try,
# o controle é transferido para o bloco except, que lida com a exceção. Se nenhum erro ocorrer, o bloco except é ignorado.

def ler_arquivo(nome_arquivo):
    """
    Lê o conteúdo de um arquivo e retorna uma lista de linhas.
    Trata erros de arquivo não encontrado ou permissão de leitura.
    """
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.readlines()
            return [linha.strip() for linha in conteudo]  # Remove espaços em branco extras
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return None
    except PermissionError:
        print(f"Erro: Permissão negada para ler o arquivo '{nome_arquivo}'.")
        return None
    except Exception as e:
        print(f"Erro inesperado ao ler o arquivo: {e}")
        return None

# Exemplo de uso
nome_do_arquivo = "meu_arquivo.txt"
linhas = ler_arquivo(nome_do_arquivo)

if linhas:
    print("Conteúdo do arquivo:")
    for linha in linhas:
        print(linha)

def escrever_arquivo(nome_arquivo, conteudo):
    """
    Escreve o conteúdo fornecido em um arquivo.
    Trata erros de escrita, como permissão negada.
    """
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(conteudo)
        print(f"Conteúdo escrito com sucesso em '{nome_arquivo}'.")
    except PermissionError:
        print(f"Erro: Permissão negada para escrever no arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"Erro inesperado ao escrever no arquivo: {e}")

# Exemplo de uso
nome_do_arquivo = "meu_arquivo.txt"
texto = "Este é um texto de exemplo.\nEscrevendo em várias linhas."
escrever_arquivo(nome_do_arquivo, texto)

#try: Envolve o código que pode gerar exceções. Neste exemplo, a divisão por zero e a conversão para inteiro podem lançar erros.;

#except ZeroDivisionError:Captura especificamente o erro de divisão por zero. Se ocorrer ZeroDivisionError no bloco try, este bloco except será executado.

#except ValueError:Captura o erro de valor inválido (por exemplo, se o usuário inserir texto em vez de um número).

#except Exception as e:Captura qualquer outro tipo de exceção não especificado anteriormente. O as e permite acessar informações sobre a exceção.

#else:O código dentro do bloco else é executado apenas se nenhuma exceção ocorrer no bloco try

#finally :O código dentro do bloco finally é sempre executado, independentemente de ocorrer ou não uma exceção. É usado para ações de limpeza, como fechar arquivos, liberar recursos, etc. 