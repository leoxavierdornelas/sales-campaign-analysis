# run_analysis.py
from src.gerar_dados import gerar_dados_campanha
from src.analise_kpis import calcular_kpis
import matplotlib.pyplot as plt
import pandas as pd
import os

def main():
    # Gerar dados
    df = gerar_dados_campanha(n_registros=2000, seed=42)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/relatorio_performance_leads_raw.csv', index=False)

    # Calcular KPIs
    taxa, roi, invalidos, resumo = calcular_kpis(df)
    resumo.to_csv('data/kpis_por_canal.csv', index=True)

    # Imprimir sumário rápido
    print("--- SUMÁRIO ---")
    print(resumo)

    # Plot: taxa de conversão
    plt.figure(figsize=(8,5))
    plt.bar(resumo.index, resumo['taxa_conversao_pct'])
    plt.title('Taxa de Conversão (%) por Canal')
    plt.ylabel('Taxa (%)')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('outputs/taxa_conversao_por_canal.png')
    plt.close()

    # Plot: ROI (tratando NaN)
    plt.figure(figsize=(8,5))
    roi_plot = resumo['roi'].fillna(0)
    plt.bar(resumo.index, roi_plot)
    plt.title('ROI (x) por Canal — NaN convertido para 0 no gráfico')
    plt.ylabel('ROI')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('outputs/roi_por_canal.png')
    plt.close()

    print("Arquivos gerados em data/ e outputs/")

if __name__ == "__main__":
    main()
