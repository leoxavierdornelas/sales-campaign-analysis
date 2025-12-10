import pandas as pd
from src.gerar_dados import gerar_dados_campanha

print("--- SUMÁRIO ---")

# 1. Gerar os dados
df = gerar_dados_campanha(2000)

# 2. Calcular KPIs
conversoes = df[df["status"] == "Convertido (Venda)"].groupby("canal")["lead_id"].count()
total = df.groupby("canal")["lead_id"].count()
taxa_conv = (conversoes / total * 100).round(2)

custo_total = df.groupby("canal")["custo_disparo"].sum()
receita_total = df.groupby("canal")["valor_venda"].sum()
roi = ((receita_total - custo_total) / custo_total).round(2)

invalidos = df[df["status"] == "Número Inválido"].groupby("canal")["lead_id"].count()

# 3. Criar o dataframe resumo
summary = pd.DataFrame({
    "total_leads": total,
    "conversoes": conversoes,
    "taxa_conversao_pct": taxa_conv,
    "custo_total": custo_total,
    "receita_total": receita_total,
    "roi": roi,
    "invalidos": invalidos
}).fillna(0)

print(summary)

# 4. Exportar arquivos
df.to_csv("data/dados_campanha.csv", index=False)
summary.to_csv("outputs/summary.csv", index=False)
summary.to_json("outputs/summary.json", orient="records")

print("Arquivos gerados em data/ e outputs/")
