def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        categoria = "Peso normal"
    elif 25 <= imc < 29.9:
        categoria = "Sobrepeso"
    elif 30 <= imc < 34.9:
        categoria = "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        categoria = "Obesidade grau 2"
    else:
        categoria = "Obesidade grau 3"
    
    return imc, categoria

if __name__ == "__main__":
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))
        imc, categoria = calcular_imc(peso, altura)
        print(f"Seu IMC é {imc:.2f}. Categoria: {categoria}.")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
