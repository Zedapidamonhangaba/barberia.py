import json
import getpass

class Barbearia:
    def __init__(self):
        self.clientes = []
        self.precos = {
            '1': {'nome': 'Degrade', 'preco': 30},
            '2': {'nome': 'Social', 'preco': 25},
            '3': {'nome': 'Barba', 'preco': 20},
            '4': {'nome': 'Sobrancelha', 'preco': 10},
            '5': {'nome': 'Degrade + Sobrancelha', 'preco': 40}
        }
        self.carregar_clientes()

    def cadastrar_cliente(self, nome, idade, senha, confirmar_senha):
        if senha != confirmar_senha:
            print("As senhas não conferem. Tente novamente.\n")
            return
        cliente = {'nome': nome, 'idade': idade, 'senha': senha, 'agendamentos': []}
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!\n")
        self.salvar_clientes()

    def mostrar_opcoes_corte(self):
        print("\nSelecione o tipo de corte:")
        for num, info in self.precos.items():
            print(f"{num}. {info['nome']} - R${info['preco']}")
        print()  # Linha vazia para separação

    def agendar_corte(self, senha, escolha_corte, hora):
        if escolha_corte in self.precos:
            for cliente in self.clientes:
                if cliente['senha'] == senha:
                    corte_info = self.precos[escolha_corte]
                    agendamento = {'corte': corte_info['nome'], 'hora': hora, 'preco': corte_info['preco']}
                    cliente['agendamentos'].append(agendamento)
                    print(f"Corte {corte_info['nome']} agendado para {hora}!\n")
                    self.salvar_clientes()
                    return
            print("Senha inválida! Cadastre-se primeiro.\n")
        else:
            print("Opção de corte inválida!\n")

    def mostrar_clientes(self):
        if len(self.clientes) == 0:
            print("Nenhum cliente cadastrado.\n")
            return
        for cliente in self.clientes:
            print(f"Nome: {cliente['nome']}, Idade: {cliente['idade']}")
            print("Agendamentos:")
            if len(cliente['agendamentos']) == 0:
                print("  Nenhum agendamento.")
            else:
                for agendamento in cliente['agendamentos']:
                    print(f"  Corte: {agendamento['corte']}, Hora: {agendamento['hora']}, Preço: R${agendamento['preco']}")
            print()  # Linha vazia para separação entre clientes

    def salvar_clientes(self):
        with open('clientes.json', 'w') as f:
            json.dump(self.clientes, f, indent=4)

    def carregar_clientes(self):
        try:
            with open('clientes.json', 'r') as f:
                self.clientes = json.load(f)
        except FileNotFoundError:
            self.clientes = []

    def gerar_relatorio_html(self):
        with open('relatorio_clientes.html', 'w') as f:
            f.write('<html lang="pt-BR">\n')
            f.write('<head>\n')
            f.write('<meta charset="UTF-8">\n')
            f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
            f.write('<title>Relatório de Clientes</title>\n')
            f.write('<style>\n')
            f.write('body { font-family: Arial, sans-serif; margin: 20px; }\n')
            f.write('h1 { color: #333; }\n')
            f.write('table { width: 100%; border-collapse: collapse; margin-top: 20px; }\n')
            f.write('th, td { padding: 10px; border: 1px solid #ccc; text-align: left; }\n')
            f.write('th { background-color: #f2f2f2; }\n')
            f.write('tr:nth-child(even) { background-color: #f9f9f9; }\n')
            f.write('</style>\n')
            f.write('</head>\n')
            f.write('<body>\n')
            f.write('<h1>Relatório de Clientes da Barbearia</h1>\n')

            if len(self.clientes) == 0:
                f.write('<p>Nenhum cliente cadastrado.</p>\n')
            else:
                f.write('<table>\n')
                f.write('<tr><th>Nome</th><th>Idade</th><th>Agendamentos</th></tr>\n')
                for cliente in self.clientes:
                    f.write(f'<tr><td>{cliente["nome"]}</td><td>{cliente["idade"]}</td><td>')
                    if len(cliente['agendamentos']) == 0:
                        f.write('Nenhum agendamento')
                    else:
                        for agendamento in cliente['agendamentos']:
                            f.write(f'{agendamento["corte"]} às {agendamento["hora"]} (R${agendamento["preco"]})<br>')
                    f.write('</td></tr>\n')
                f.write('</table>\n')

            f.write('</body>\n')
            f.write('</html>\n')

        print("Relatório HTML gerado com sucesso: relatorio_clientes.html\n")

def menu():
    barbearia = Barbearia()
    while True:
        print("\nMenu da Barbearia")
        print("1. Cadastrar Cliente")
        print("2. Agendar Corte")
        print("3. Mostrar Clientes")
        print("4. Gerar Relatório HTML")
        print("5. Sair")
        print()  # Linha vazia para separação
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            idade = input("Idade: ")
            senha = getpass.getpass("Crie uma senha: ")
            confirmar_senha = getpass.getpass("Confirme sua senha: ")
            barbearia.cadastrar_cliente(nome, idade, senha, confirmar_senha)
        elif opcao == '2':
            senha = getpass.getpass("Digite sua senha: ")
            barbearia.mostrar_opcoes_corte()
            escolha_corte = input("Escolha o número do corte: ")
            hora = input("Hora Desejada: ")
            barbearia.agendar_corte(senha, escolha_corte, hora)
        elif opcao == '3':
            barbearia.mostrar_clientes()
        elif opcao == '4':
            barbearia.gerar_relatorio_html()  # Chama a função para gerar o HTML
        elif opcao == '5':
            print("Saindo...\n")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    menu()
