# ===========================================
# TRATAMENTO DE DADOS - AdventureWorks
# ===========================================
# Lê os dados brutos extraídos e aplica
# limpeza e enriquecimento com Pandas

import pandas as pd
import os

# --- LEITURA DOS DADOS BRUTOS ---
df_producao = pd.read_csv("dados_brutos/producao.csv")
df_vendas = pd.read_csv("dados_brutos/vendas.csv")
df_rh = pd.read_csv("dados_brutos/rh.csv")

print("=== DIAGNÓSTICO DOS DADOS ===\n")

# --- PRODUÇÃO ---
print(f"Produção — shape: {df_producao.shape}")
print(f"Nulos:\n{df_producao.isnull().sum()}")
print(f"Duplicatas: {df_producao.duplicated().sum()}\n")

# --- VENDAS ---
print(f"Vendas — shape: {df_vendas.shape}")
print(f"Nulos:\n{df_vendas.isnull().sum()}")
print(f"Duplicatas: {df_vendas.duplicated().sum()}\n")

# --- RH ---
print(f"RH — shape: {df_rh.shape}")
print(f"Nulos:\n{df_rh.isnull().sum()}")
print(f"Duplicatas: {df_rh.duplicated().sum()}\n")

# --- ENRIQUECIMENTO: VENDAS ---
# Converte a data de string para datetime
df_vendas["OrderDate"] = pd.to_datetime(df_vendas["OrderDate"])

# Extrai o ano e o mês separados — útil pra análise de sazonalidade
df_vendas["Ano"] = df_vendas["OrderDate"].dt.year
df_vendas["Mes"] = df_vendas["OrderDate"].dt.month

# --- ENRIQUECIMENTO: RH ---
# Classifica o salário em faixas
df_rh["FaixaSalarial"] = pd.cut(
    df_rh["Salario"],
    bins=[0, 20, 40, 60, 100],
    labels=["Júnior", "Pleno", "Sênior", "Especialista"]
)

# --- SALVANDO DADOS TRATADOS ---
os.makedirs("dados_tratados", exist_ok=True)
df_producao.to_csv("dados_tratados/producao.csv", index=False)
df_vendas.to_csv("dados_tratados/vendas.csv", index=False)
df_rh.to_csv("dados_tratados/rh.csv", index=False)

print("=== DADOS TRATADOS SALVOS ===")
print(df_vendas[["OrderDate", "Ano", "Mes", "TotalDue"]].head())
print(df_rh[["JobTitle", "Salario", "FaixaSalarial"]].head()) 