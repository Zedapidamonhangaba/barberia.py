class Barbearia:
    def __init__(self):
        self.cadastros = []
        self.precos = {
            'degrade': 30,
            'social': 25,
            'barba': 20,
            'sobrancelha': 5
        }

    def adicionar_cliente(self, nome, hora, corte):
        corte = corte.lower()  # Transforma a entrada para minúsculas
        if corte in self.precos:
            cliente = {'nome': nome, 'hora': hora, 'corte': corte.capitalize(), 'preco': self.precos[corte]}
            self.cadastros.append(cliente)
            print(f"Cliente {nome} cadastrado com sucesso!")
        else:
            print("Corte inválido!")

    def mostrar_cadastros(self):
        if len(self.cadastros) == 0:
            print("Nenhum cliente cadastrado.")
            return
        for cliente in self.cadastros:
            print(f"Nome: {cliente['nome']}, Hora: {cliente['hora']}, Corte: {cliente['corte']}, Preço: R${cliente['preco']}")

def menu():
    barbearia = Barbearia()
    while True:
        print("Menu da Barbearia")
        print("1. Cadastrar Cliente")
        print("2. Mostrar Clientes")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do Cliente: ")
            hora = input("Hora Desejada: ")
            corte = input("Tipo de Corte (Degrade, Social, Barba, Sobrancelha): ")
            barbearia.adicionar_cliente(nome, hora, corte)
        elif opcao == '2':
            barbearia.mostrar_cadastros()
        elif opcao == '3':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
