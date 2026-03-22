import pandas as pd
import re
import os
from datetime import datetime


ARQUIVO_ENTRADA = "entrada_bruta.txt"
registros = []

def limpar_placa(texto):
    
    encontrados = re.findall(r'[A-Z0-9]{7}', texto.upper().replace("-", "").replace(" ", ""))
    
    return [p for p in encontrados if sum(c.isdigit() for c in p) >= 2]

print("="*50)
print("SISTEMA HÍBRIDO DE LOGÍSTICA - AMV")
print("="*50)


if os.path.exists(ARQUIVO_ENTRADA):
    print(f"📂 Arquivo '{ARQUIVO_ENTRADA}' detectado! Processando massa...")
    with open(ARQUIVO_ENTRADA, "r", encoding="utf-8") as f:
        conteudo = f.read()
    
    placas_f = limpar_placa(conteudo)
    for p in placas_f:
        registros.append({'Placa': p, 'Tipo': 'MASSA', 'Hora': datetime.now().strftime("%H:%M:%S")})
    
    print(f"✅ {len(placas_f)} placas importadas do arquivo.")
    
    
   
    with open(ARQUIVO_ENTRADA, "w") as f:
        f.write("") 
    print(f"🧹 Arquivo '{ARQUIVO_ENTRADA}' limpo para o próximo uso.")

else:
    print("ℹ️ Nenhum arquivo de massa encontrado. Iniciando MODO MANUAL.")


print("\n[Digite novas placas ou 'S' para salvar e gerar o Excel final]")
while True:
    placa_input = input("Placa (ou 'S'): ").strip().upper()
    
    if placa_input == 'S':
        break
    
    if len(placa_input) >= 7:
        placas_manuais = limpar_placa(placa_input)
        for p in placas_manuais:
            registros.append({'Placa': p, 'Tipo': 'MANUAL', 'Hora': datetime.now().strftime("%H:%M:%S")})
            print(f"👍 {p} adicionada à lista.")
    else:
        print("⚠️ Placa inválida ou curta demais.")


if registros:
    df = pd.DataFrame(registros)
    data_hoje = datetime.now().strftime("%Y-%m-%d_%H%M")
    nome_saida = f"Relatorio_Consolidado_{data_hoje}.xlsx"
    
    df.to_excel(nome_saida, index=False)
    print("\n" + "="*50)
    print(f"🚀 EXCEL GERADO: {nome_saida}")
    print(f"📊 Total: {len(registros)} veículos registrados.")
    print("="*50)
else:
    print("\nNada foi registrado, nenhum arquivo criado.")

