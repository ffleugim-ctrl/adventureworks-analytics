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