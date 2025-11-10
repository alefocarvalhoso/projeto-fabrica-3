import datetime

# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura * altura)

# Função para determinar a classificação do IMC
def classificacao_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Função para adicionar registros ao histórico
def adicionar_registro(historico, peso, altura):
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
    imc = calcular_imc(peso, altura)
    classificacao = classificacao_imc(imc)
    historico.append({
        "data": data_atual,
        "peso": peso,
        "altura": altura,
        "imc": round(imc, 2),
        "classificacao": classificacao
    })

# Função para exibir o histórico
def exibir_historico(historico):
    if not historico:
        print("Ainda não há registros de IMC.")
        return
    
    print("\nHistórico de IMC:")
    print(f"{'Data':<12} {'Peso (kg)':<10} {'Altura (m)':<12} {'IMC':<6} {'Classificação'}")
    print("-" * 50)
    
    for registro in historico:
        print(f"{registro['data']:<12} {registro['peso']:<10} {registro['altura']:<12} {registro['imc']:<6} {registro['classificacao']}")

# Função principal para rodar o programa
def main():
    historico = []

    while True:
        print("\nMenu:")
        print("1. Calcular IMC e adicionar registro")
        print("2. Ver histórico de registros")
        print("3. Sair")
        opcao = input("Escolha uma opção (1/2/3): ")

        if opcao == '1':
            try:
                peso = float(input("Digite o peso em kg: "))
                altura = float(input("Digite a altura em metros: "))
                adicionar_registro(historico, peso, altura)
                print("\nIMC calculado com sucesso!")
            except ValueError:
                print("Por favor, insira valores numéricos válidos.")
        
        elif opcao == '2':
            exibir_historico(historico)
        
        elif opcao == '3':
            print("Saindo... Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Rodar o programa
if __name__ == "__main__":
    main()
