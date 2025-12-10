# Sales Campaign Performance Analysis (CRM)

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Status](https://img.shields.io/badge/Status-Completo-green)

## Descrição
Projeto de análise de performance de campanhas de aquisição de leads (SMS, Voz, Email, WhatsApp), simulando cenários reais de empresas de CRM e automação de marketing.  
Foco: medir **eficiência, ROI e qualidade da base**, identificando desperdício de budget e canais mais eficazes.

## Objetivo do Projeto
- Gerar dados simulados de campanhas de marketing com diferentes canais e custos.
- Calcular KPIs de conversão, ROI e leads inválidos.
- Produzir arquivos CSV e gráficos que auxiliem decisões estratégicas.
- Simular o workflow de um Analista de Dados em empresas de CRM.

## Contexto de Negócio
Empresas de automação de marketing (TOTVS, Ligue Lead, RD Station, Zenvia) precisam identificar rapidamente qual canal gera **mais leads qualificados pelo menor custo**. Este projeto reproduz esse cenário de forma realista.

## Tecnologias e Dependências
- **Python 3.8+**  
- **Pandas** e **NumPy** → manipulação de dados  
- **Matplotlib** → visualizações  
- **Jupyter Notebook** → análise exploratória e gráficos  
- **CSV** → exportação de KPIs  

Instalação das dependências:

```bash
pip install -r requirements.txt
```

## Estrutura do Projeto

```
sales-campaign-analysis/
├── data/                # CSVs gerados (raw e KPIs)
├── notebooks/           # Notebooks de análise exploratória
├── outputs/             # Gráficos gerados (PNG)
├── src/                 # Funções Python (gerar_dados.py, analise_kpis.py)
├── run_analysis.py      # Script principal para gerar KPIs e gráficos
├── requirements.txt
└── README.md
```

## Como Executar

1. Abra o terminal na pasta do projeto.  
2. Execute o script principal:

```bash
python run_analysis.py
```

Saídas geradas:  
- `data/relatorio_performance_leads_raw.csv`  
- `data/kpis_por_canal.csv`  
- gráficos em `outputs/`

3. Para análise interativa no Jupyter Notebook:

```bash
jupyter notebook notebooks/analise_campanhas.ipynb
```

---

## Resultados Esperados

### Exemplo de KPIs
| Canal            | Total Leads | Conversões | Taxa Conversão (%) | Custo Total | Receita Total | ROI | Leads Inválidos |
|-----------------|------------|------------|------------------|------------|---------------|-----|----------------|
| WhatsApp        | 200        | 79         | 39.5             | 100.0      | 13500.0       | 134 | 5              |
| SMS Marketing   | 800        | 110        | 13.8             | 120.0      | 15000.0       | 124 | 44             |
| Voz (Robocall)  | 600        | 58         | 9.7              | 180.0      | 9000.0        | 49  | 51             |
| Email           | 400        | 18         | 4.5              | 20.0       | 3000.0        | 149 | 18             |

> Os números são simulados e servem como exemplo.

### Gráficos
- `outputs/taxa_conversao_por_canal.png` → barras de taxa de conversão  
- `outputs/roi_por_canal.png` → ROI por canal  

---

## Melhorias Futuras
- Análise temporal (semanal/mensal)  
- Comparar custo por lead convertido (CPL)  
- Incluir segmentação demográfica  
- Gerar relatório HTML/PDF automaticamente com nbconvert  
- Testes unitários para funções de cálculo de KPI  

---

## Contato / Referência
- Leonardo Xavier Dornelas  
- [LinkedIn](https://www.linkedin.com/in/leonardo-xavier-a93344375)  
- Email: leonardo_dornelas@icloud.com

---

## ✅ Passo a Passo de Uso

1. Abra **VS Code** e navegue até o arquivo `README.md`.  
2. Apague qualquer conteúdo antigo e cole este README completo.  
3. Salve o arquivo (`Ctrl+S`).  
4. Commit e push para o GitHub:

```bash
git add README.md
git commit -m "docs: README.md avançado completo"
git push origin main
```'''

with open('/mnt/data/README_complete.txt', 'w', encoding='utf-8') as f:
    f.write(conteudo)

'/mnt/data/README_complete.txt'
