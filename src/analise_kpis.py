# src/analise_kpis.py
import pandas as pd
import numpy as np

def calcular_kpis(df):
    """
    Retorna:
      - taxa_conversao: Series (%) por canal
      - roi: Series (float) por canal (tratamento de divisão por zero)
      - invalidos: Series (count) por canal
      - resumo_df: DataFrame com KPIs consolidado
    """
    # Totais
    total_por_canal = df.groupby('canal')['lead_id'].count()

    # Conversões
    conversao = df[df['status'] == 'Convertido (Venda)'].groupby('canal')['lead_id'].count()
    taxa_conversao = (conversao / total_por_canal * 100).round(2).fillna(0)

    # Custo e receita
    custo_total = df.groupby('canal')['custo_disparo'].sum()
    receita_total = df.groupby('canal')['valor_venda'].sum()

    # Proteção contra divisão por zero
    roi = pd.Series(index=custo_total.index, dtype=float)
    for canal in custo_total.index:
        custo = custo_total.loc[canal]
        receita = receita_total.loc[canal]
        if custo == 0:
            roi.loc[canal] = np.nan
        else:
            roi.loc[canal] = round((receita - custo) / custo, 2)

    # Leads inválidos
    invalidos = df[df['status'] == 'Número Inválido'].groupby('canal')['lead_id'].count().reindex(total_por_canal.index, fill_value=0)

    # Resumo em DataFrame
    resumo = pd.DataFrame({
        'total_leads': total_por_canal,
        'conversoes': conversao.reindex(total_por_canal.index, fill_value=0),
        'taxa_conversao_pct': taxa_conversao,
        'custo_total': custo_total,
        'receita_total': receita_total,
        'roi': roi,
        'invalidos': invalidos
    })

    # Ordenar por taxa de conversão desc
    resumo = resumo.sort_values(by='taxa_conversao_pct', ascending=False)

    return taxa_conversao, roi, invalidos, resumo
