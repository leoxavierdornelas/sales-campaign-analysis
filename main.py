import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. SIMULAÇÃO DE DADOS (CENÁRIO LIGUE LEAD/TOTVS) ---
# Simulando dados de disparos de campanhas de marketing (Voz e SMS)
# Para demonstrar capacidade analítica focada em conversão de leads.

def gerar_dados_campanha(n_registros=1000):
    np.random.seed(42)
    
    canais = ['SMS Marketing', 'Voz (Robocall)', 'Email', 'WhatsApp']
    status_lead = ['Sem Resposta', 'Interessado', 'Convertido (Venda)', 'Número Inválido']
    
    dados = []
    
    for id_lead in range(1, n_registros + 1):
        canal = np.random.choice(canais, p=[0.4, 0.3, 0.2, 0.1])
        custo = 0.0
        
        # Definição de custos e taxas de sucesso por canal
        if canal == 'SMS Marketing':
            custo = 0.15
            status = np.random.choice(status_lead, p=[0.6, 0.2, 0.15, 0.05])
        elif canal == 'Voz (Robocall)':
            custo = 0.30
            status = np.random.choice(status_lead, p=[0.5, 0.3, 0.1, 0.1])
        elif canal == 'WhatsApp':
            custo = 0.50
            status = np.random.choice(status_lead, p=[0.2, 0.4, 0.35, 0.05]) # Alta conversão
        else:
            custo = 0.05
            status = np.random.choice(status_lead, p=[0.8, 0.1, 0.05, 0.05])
            
        dados.append({
            'lead_id': id_lead,
            'canal': canal,
            'custo_disparo': custo,
            'status': status,
            'valor_venda': np.random.randint(200, 1500) if status == 'Convertido (Venda)' else 0
        })
        
    return pd.DataFrame(dados)

# --- 2. ANÁLISE DE KPI (BUSINESS INTELLIGENCE) ---

print("--- RELATÓRIO DE PERFORMANCE DE CAMPANHAS ---")
df = gerar_dados_campanha(2000)

# KPI 1: Taxa de Conversão por Canal
conversao = df[df['status'] == 'Convertido (Venda)'].groupby('canal')['lead_id'].count()
total_por_canal = df.groupby('canal')['lead_id'].count()
taxa_conversao = (conversao / total_por_canal * 100).round(2)

print("\n1. Taxa de Conversão por Canal (%):")
print(taxa_conversao.sort_values(ascending=False))

# KPI 2: ROI (Retorno sobre Investimento)
# ROI = (Receita - Custo) / Custo
custo_total = df.groupby('canal')['custo_disparo'].sum()
receita_total = df.groupby('canal')['valor_venda'].sum()
roi = ((receita_total - custo_total) / custo_total).round(2)

print("\n2. ROI estimado por Canal (x vezes o investimento):")
print(roi.sort_values(ascending=False))

# KPI 3: Higiene da Base (Leads Inválidos)
invalidos = df[df['status'] == 'Número Inválido'].groupby('canal')['lead_id'].count()
print("\n3. Volume de Leads Inválidos (Desperdício de Budget):")
print(invalidos)

# --- 3. EXPORTAÇÃO ---
df.to_csv('relatorio_performance_leads.csv', index=False)
print("\nArquivo 'relatorio_performance_leads.csv' gerado para Dashboard.")