# src/gerar_dados.py
import pandas as pd
import numpy as np

def gerar_dados_campanha(n_registros=2000, seed=42):
    """
    Gera DataFrame simulado de disparos por canal.
    """
    np.random.seed(seed)
    canais = ['SMS Marketing', 'Voz (Robocall)', 'Email', 'WhatsApp']
    status_lead = ['Sem Resposta', 'Interessado', 'Convertido (Venda)', 'Número Inválido']

    dados = []
    for id_lead in range(1, n_registros + 1):
        canal = np.random.choice(canais, p=[0.4, 0.3, 0.2, 0.1])

        if canal == 'SMS Marketing':
            custo = 0.15
            status = np.random.choice(status_lead, p=[0.6, 0.2, 0.15, 0.05])
        elif canal == 'Voz (Robocall)':
            custo = 0.30
            status = np.random.choice(status_lead, p=[0.5, 0.3, 0.1, 0.1])
        elif canal == 'WhatsApp':
            custo = 0.50
            status = np.random.choice(status_lead, p=[0.2, 0.4, 0.35, 0.05])
        else:  # Email
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
