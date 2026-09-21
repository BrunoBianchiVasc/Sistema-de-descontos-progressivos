# 🛒 Sistema de Desconto Progressivo

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
![Loja](https://img.shields.io/badge/Loja-Online-FF6F00?style=flat&logo=shopify&logoColor=white)

Programa em **Python** que calcula o desconto e o valor final de uma
compra em uma loja online, aplicando percentuais diferentes de acordo
com o valor total da compra. 🛍️

## 🧮 Regras de desconto

\`\`\`
valor < R$ 200,00                      → 5% de desconto
R$ 200,00 <= valor < R$ 300,00         → 10% de desconto
valor >= R$ 300,00                     → 15% de desconto

valorDesconto = valorCompra * percentualDesconto
valorFinal    = valorCompra - valorDesconto
\`\`\`

## ▶️ Como executar

\`\`\`bash
python desconto_progressivo.py
\`\`\`

Digite o valor total da compra 💰 e o programa exibe o percentual e o
valor do desconto aplicado, além do total final a pagar.

### Exemplo de saída

\`\`\`
Valor da compra: R$ 250.00
Desconto aplicado: 10% (R$ 25.00)
Valor final a pagar: R$ 225.00
\`\`\`
