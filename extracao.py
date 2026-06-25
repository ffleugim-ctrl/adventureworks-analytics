# ===========================================
# EXTRAÇÃO DE DADOS - AdventureWorks
# ===========================================
# Esse script conecta no SQL Server e extrai
# dados das 3 áreas: Produção, Vendas e RH

import pyodbc
import pandas as pd

# --- CONEXÃO ---
# Aqui a gente define como o Python vai se conectar ao SQL Server
# Trusted_Connection=yes significa autenticação do Windows (sem senha)
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost\\SQLEXPRESS01;"
  "DATABASE=AdventureWorks2025;"
    "Trusted_Connection=yes;"
)

print("Conexão estabelecida com sucesso!")

# --- EXTRAÇÃO: PRODUÇÃO ---
# Puxa dados de ordens de trabalho com motivo de descarte
query_producao = """
SELECT 
    wo.WorkOrderID,
    wo.ProductID,
    wo.ScrappedQty,
    sr.Name AS MotivoDescarte
FROM Production.WorkOrder wo
INNER JOIN Production.ScrapReason sr ON wo.ScrapReasonID = sr.ScrapReasonID
WHERE wo.ScrappedQty > 0
"""

df_producao = pd.read_sql(query_producao, conn)
print(f"Produção: {len(df_producao)} registros extraídos")

# --- EXTRAÇÃO: VENDAS ---
query_vendas = """
SELECT 
    soh.SalesOrderID,
    soh.OrderDate,
    soh.TotalDue,
    st.Name AS Territorio
FROM Sales.SalesOrderHeader soh
INNER JOIN Sales.SalesTerritory st ON soh.TerritoryID = st.TerritoryID
"""

df_vendas = pd.read_sql(query_vendas, conn)
print(f"Vendas: {len(df_vendas)} registros extraídos")

# --- EXTRAÇÃO: RH ---
query_rh = """
SELECT 
    e.BusinessEntityID,
    e.JobTitle,
    eph.Rate AS Salario,
    d.Name AS Departamento
FROM HumanResources.Employee e
INNER JOIN HumanResources.EmployeePayHistory eph ON e.BusinessEntityID = eph.BusinessEntityID
INNER JOIN HumanResources.EmployeeDepartmentHistory edh ON e.BusinessEntityID = edh.BusinessEntityID
INNER JOIN HumanResources.Department d ON edh.DepartmentID = d.DepartmentID
WHERE edh.EndDate IS NULL
"""

df_rh = pd.read_sql(query_rh, conn)
print(f"RH: {len(df_rh)} registros extraídos")

conn.close()
print("Extração concluída!")