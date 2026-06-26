# ===========================================
# VISUALIZAÇÕES - AdventureWorks
# ===========================================
# Gera gráficos das 3 áreas e salva como imagem

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Estilo visual dos gráficos
sns.set_theme(style="darkgrid")

# Cria pasta pra salvar os gráficos
os.makedirs("graficos", exist_ok=True)

# --- LÊ OS DADOS TRATADOS ---
df_producao = pd.read_csv("dados_tratados/producao.csv")
df_vendas = pd.read_csv("dados_tratados/vendas.csv")
df_rh = pd.read_csv("dados_tratados/rh.csv")

# --- GRÁFICO 1: PRODUÇÃO ---
# Top 10 motivos de descarte
top_motivos = df_producao.groupby("MotivoDescarte")["ScrappedQty"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_motivos.values, y=top_motivos.index, palette="Reds_r")
plt.title("Top 10 Motivos de Descarte — Produção")
plt.xlabel("Quantidade Descartada")
plt.ylabel("Motivo")
plt.tight_layout()
plt.savefig("graficos/producao_motivos_descarte.png")
plt.close()
print("Gráfico 1 salvo!")

# --- GRÁFICO 2: VENDAS ---
# Vendas totais por território
vendas_territorio = df_vendas.groupby("Territorio")["TotalDue"].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=vendas_territorio.values, y=vendas_territorio.index, palette="Blues_r")
plt.title("Vendas Totais por Território")
plt.xlabel("Total de Vendas (USD)")
plt.ylabel("Território")
plt.tight_layout()
plt.savefig("graficos/vendas_por_territorio.png")
plt.savefig("graficos/vendas_por_territorio.png")

# Adicione isso para o gráfico abrir na sua tela na hora:
plt.show() 

plt.close()
print("Gráfico 2 salvo!")

# --- GRÁFICO 3: RH ---
# Distribuição por faixa salarial
plt.figure(figsize=(8, 6))
df_rh["FaixaSalarial"].value_counts().plot(kind="bar", color=["#2ecc71", "#3498db", "#e74c3c", "#9b59b6"])
plt.title("Distribuição de Funcionários por Faixa Salarial")
plt.xlabel("Faixa Salarial")
plt.ylabel("Quantidade de Funcionários")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("graficos/rh_faixa_salarial.png")
plt.close()
print("Gráfico 3 salvo!")

print("\nTodos os gráficos gerados em /graficos!")