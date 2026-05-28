"""
Visualização 3D de Dupla Hélice de DNA
Autor: @Mr-LeonardoGomes
Descrição: Gera uma representação 3D interativa da estrutura do DNA usando a biblioteca Vedo
"""

from vedo import *
import numpy as np

def create_dna_helix(turns=4, points=400, radius=0.30, tube_radius=0.30):
    """
    Cria uma representação 3D da dupla hélice do DNA
    
    Args:
        turns (int): Número de voltas completas da hélice
        points (int): Número de pontos para gerar a curva
        radius (float): Raio da hélice
        tube_radius (float): Raio dos tubos das fitas
    
    Returns:
        tuple: (fita1, fita2, barras_conexao)
    """
    # Gerar os pontos ao longo da hélice
    t = np.linspace(0, turns * 2 * np.pi, points)
    
    # Primeira fita (ângulo 0)
    strand1 = np.c_[radius * np.cos(t), radius * np.sin(t), t/4]
    
    # Segunda fita (defasada em 180 graus)
    strand2 = np.c_[radius * np.cos(t + np.pi), radius * np.sin(t + np.pi), t/4]
    
    # Criar os tubos (as fitas do DNA)
    dna_strand1 = Tube(strand1, r=tube_radius, c="red5", alpha=1)
    dna_strand2 = Tube(strand2, r=tube_radius, c="cyan5", alpha=1)
    
    # Criar as barras de conexão (pares de bases)
    connection_bars = []
    step = max(1, points // (turns * 15))  # Ajusta automaticamente a densidade das barras
    
    for i in range(0, len(t), step):
        bar = Line(strand1[i], strand2[i], c="white", lw=2)
        connection_bars.append(bar)
    
    return dna_strand1, dna_strand2, connection_bars

def visualize_dna():
    """Função principal para visualizar o DNA"""
    print("🎨 Gerando visualização 3D do DNA...")
    
    # Criar o DNA
    strand1, strand2, bars = create_dna_helix()
    
    # Configurar e mostrar a visualização
    show(
        strand1, 
        strand2, 
        *bars,
        bg="black",
        axes={
            "grid": True,
            "xy_grid": False,
            "xz_grid": False,
            "yz_grid": False,
            "font": "courier",
            "axes_linewidth": 1
        },
        viewup="z",
        title="DNA Double Helix - 3D Visualization",
        interactive=True
    )
    
    print("✅ Visualização concluída!")

if __name__ == "__main__":
    visualize_dna()