# Calculadora-imc
LINGUAGEM DE PROGRAMAÇÃO CALCULO IMC
# 📊 Calculadora de IMC - Índice de Massa Corpórea

Bem-vindo ao repositório da **Calculadora de IMC**! Este projeto foi desenvolvido em **Python** com o objetivo de calcular o **Índice de Massa Corpórea (IMC)** de um usuário com base em seu peso e altura.

---

## 🎯 Objetivo
O objetivo deste projeto é criar um programa simples, eficiente e intuitivo que permita aos usuários calcular seu **IMC** e verificar sua classificação com base nos padrões da **Organização Mundial da Saúde (OMS)**.

## 🏆 Funcionalidades

✅ Entrada de dados do usuário (peso e altura)\
✅ Cálculo automático do IMC\
✅ Classificação do IMC segundo a tabela da OMS\
✅ Exibição do resultado formatado

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python 3**

## 📌 Descrição do Programa
O programa solicita que o usuário informe seu **peso (kg)** e sua **altura (m)**, realiza o cálculo do IMC utilizando a fórmula padrão e retorna o resultado junto com a classificação correspondente.

## ⚙️ Como Funciona?
1. O usuário insere seu **peso** e **altura**.
2. O programa calcula o **IMC** usando a fórmula:
   \[ IMC = \frac{peso}{altura^2} \]
3. O resultado é exibido na tela com sua respectiva classificação:

| IMC          | Classificação        |
|-------------|----------------|
| Menor que 18.5 | Abaixo do peso |
| 18.5 - 24.9   | Peso normal     |
| 25 - 29.9     | Sobrepeso       |
| 30 - 34.9     | Obesidade Grau I |
| 35 - 39.9     | Obesidade Grau II |
| Acima de 40   | Obesidade Grau III |

---

## 🖥️ Código-Fonte
Aqui está a implementação principal do código em Python:

```python
# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Entrada de dados
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Exibição do resultado
print(f"Seu IMC é: {imc:.2f}")
```
## 📥 Como Baixar e Executar o Projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/calculadora-imc.git
```

2. **Entre na pasta do projeto:**

```bash
cd calculadora-imc
```

3. **Execute o programa:**

```bash
python imc_calculadora.py
```
---

## 🚀 Etapas de Execução
### 1️⃣ Entrada de Dados
- O programa solicita ao usuário os valores de **peso** e **altura**.

### 2️⃣ Cálculo do IMC
- A fórmula é aplicada e o **IMC** é calculado automaticamente.

### 3️⃣ Saída de Dados
- O programa exibe o resultado formatado com **duas casas decimais**.

---

## 📌 Exemplo de Execução
### 📝 Entrada:
```
Digite seu peso (kg): 70
Digite sua altura (m): 1.75
```
### 📊 Saída:
```
Seu IMC é: 22.86
Classificação: Peso normal
```

---

## 🔍 Análise do Código
- **Simplicidade**: O código é enxuto e direto.
- **Eficiência**: O cálculo do IMC é feito rapidamente.
- **Interatividade**: A interação ocorre por meio da função `input()`.
- **Formatação**: O uso de `f-strings` melhora a legibilidade da saída.

---

## 🏁 Conclusão
Este projeto demonstra como um **cálculo matemático simples** pode ser implementado de maneira clara e acessível com Python.



Quer contribuir? Sinta-se à vontade para sugerir melhorias! 😃

