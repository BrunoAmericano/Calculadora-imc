# Relatório Completo

## Objetivo

O objetivo deste projeto é desenvolver um programa simples em Python que calcule o Índice de Massa Corpórea (IMC) de um usuário, baseado nos dados de peso e altura fornecidos por ele. O programa deve realizar o cálculo do IMC e apresentar o resultado de forma clara, simplificada e precisa.

## Descrição do Programa

Este programa solicita ao usuário dois valores numéricos: peso (em quilogramas) e altura (em metros), calcula o IMC usando a fórmula padrão e exibe o valor calculado com duas casas decimais. O cálculo do IMC é feito por meio de uma função dedicada, e os dados são inseridos e retornados usando funções simples do Python.

## Código do Programa

Aqui está o código fonte utilizado para calcular o IMC:

```python
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = calcular_imc(peso, altura)

print(f"Seu IMC é: {imc:.2f}")
