# 🧬 DNA 3D Visualization

Uma visualização interativa e elegante da dupla hélice do DNA em 3D, desenvolvida com Python.

![DNA Visualization](https://img.shields.io/badge/Python-3.8+-blue)
![Vedo](https://img.shields.io/badge/Vedo-3D-red)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Características

- 🎨 Visualização 3D realista da dupla hélice
- 🔴 Fitas coloridas (vermelha e ciano) para distinção clara
- ⚪ Barras brancas representando os pares de bases
- 🖱️ Interface interativa (zoom, rotação,平移)
- ⚡ Performance otimizada com ajuste automático de densidade

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes Python)

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/MR-LeonardoGomes/DNA-3D-Visualization.git
cd DNA-3D-Visualization

🎮 Como usar
Execute o script principal:

bash
python src/dna_visualization.py
Controles da visualização:
Mouse esquerdo: Rotacionar a visualização

Mouse direito: Zoom

Scroll: Aproximar/afastar

Mouse médio: Mover a cena

🎨 Personalização
Você pode ajustar os parâmetros da hélice modificando a função create_dna_helix():

python
# Exemplo: DNA com 6 voltas e tubos mais grossos
dna = create_dna_helix(
    turns=6,           # Número de voltas
    points=600,        # Pontos da curva (mais = mais suave)
    radius=0.40,       # Raio da hélice
    tube_radius=0.35   # Espessura das fitas
)
📁 Estrutura do Projeto
text
DNA-3D-Visualization/
│
├── src/
│   └── dna_visualization.py   # Código principal
├── requirements.txt            # Dependências
├── README.md                   # Documentação
└── .gitignore                  # Arquivos ignorados pelo Git
🛠️ Tecnologias Utilizadas
Vedo - Biblioteca para visualização 3D científica

NumPy - Computação numérica e manipulação de arrays

📸 Exemplo Visual
A visualização gera uma janela interativa mostrando:

Duas fitas helicoidais (vermelha e ciano)

Conexões transversais brancas (pares de bases)

Eixos de coordenadas para referência

Fundo preto para melhor contraste

🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para:

Reportar bugs

Sugerir novas funcionalidades

Enviar pull requests

📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

👤 Autor
@Mr-LeonardoGomes

GitHub: @Mr-LeonardoGomes

🌟 Agradecimentos
Biblioteca Vedo pela excelente ferramenta de visualização 3D


⭐️ Não esqueça de dar uma estrela se este projeto foi útil para você!


