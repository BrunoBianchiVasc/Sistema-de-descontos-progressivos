"""
Sistema de Desconto Progressivo - Loja Online

Aplica um percentual de desconto sobre o valor da compra, de acordo
com faixas de valor, e exibe o total a pagar.
"""

valor_compra = float(input("Digite o valor total da compra (R$): "))

# Define o percentual de desconto conforme a faixa de valor da compra
if valor_compra < 200:
    percentual_desconto = 0.05
elif valor_compra < 300:
    percentual_desconto = 0.10
else:
    percentual_desconto = 0.15

valor_desconto = valor_compra * percentual_desconto
valor_final = valor_compra - valor_desconto

print(f"\nValor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {percentual_desconto * 100:.0f}% (R$ {valor_desconto:.2f})")
print(f"Valor final a pagar: R$ {valor_final:.2f}")