# Define a classe Tabuada, responsável por gerar a tabuada de um número entre 1 e 10
class Tabuada:
    # Construtor da classe: executado ao criar um novo objeto
    def __init__(self, numero: int):
        # Valida se o número está entre 1 e 10; se não estiver, lança um erro
        if not 1 <= numero <= 10:
            raise ValueError("Número fora do intervalo permitido (1 a 10).")
        # Armazena o número como um atributo do objeto
        self.numero = numero

    # Método que gera a tabuada do número armazenado
    def gerar(self):
        # Retorna uma lista com as expressões da tabuada de 1 a 10
        return list(map(
            lambda x: f"{self.numero} x {x} = {self.numero * x}",  # Cria cada linha formatada da tabuada
            range(1, 11)  # Gera os valores de 1 a 10
        ))

# Função que solicita ao usuário um número entre 1 e 10, tratando possíveis erros de entrada
def solicitar_numero():
    try:
        # Solicita ao usuário um número inteiro com uma mensagem explicativa
        numero = int(input("\nDigite um número entre 1 e 10 para ver sua tabuada: "))
        return numero  # Retorna o número digitado
    except ValueError:
        # Caso o usuário digite algo inválido (ex: texto), exibe uma mensagem de erro
        print("Por favor, digite um número inteiro válido.")
        return solicitar_numero()  # Reexecuta a função até o usuário inserir um número válido

# Função principal que controla o fluxo do programa
def main():
    while True:  # Executa continuamente até o usuário encerrar manualmente (Ctrl+C, por exemplo)
        numero = solicitar_numero()  # Solicita um número ao usuário
        try:
            # Cria um objeto da classe Tabuada com o número fornecido
            tabuada = Tabuada(numero)
            print(f"\nTabuada do {numero}")
            # Imprime cada linha da tabuada gerada
            for linha in tabuada.gerar():
                print(linha)
        except ValueError as e:
            # Caso o número esteja fora do intervalo, exibe a mensagem de erro
            print(e)
            continue  # Volta ao início do loop

# Ponto de entrada do programa: executa a função principal se o script for rodado diretamente
if __name__ == "__main__":
    main()






