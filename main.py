import zipfile
import os
import numpy as np
import json
import pandas as pd

arquivo_zip = "data/HIST_PAINEL_COVIDBR_18nov2020.zip"
arquivo_csv = "data/HIST_PAINEL_COVIDBR_18nov2020.csv"

def extrair_dados_zip(zip):
  print("Extraindo arquivo ZIP...")
  data = zipfile.ZipFile(zip, "r")
  data = data.extractall("data") 

def ler_dados_csv(csv):
  print("Lendo a planilha...")
  data = pd.read_csv(csv, encoding="utf-8",delimiter=";")
  return data

if not os.path.exists(f"{arquivo_csv}"):
  extrair_dados_zip(f"{arquivo_zip}")

data = ler_dados_csv(arquivo_csv)
data_brasil = data[data["regiao"] == "Brasil"]
print(data_brasil.iloc[0])
print(data_brasil.iloc[0].dtypes)