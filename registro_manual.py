import pandas as pd
from datetime import datetime
import re

print("--- MODO COPIAR E COLAR (AMV) ---")
print("1. Cole TODA a sua lista abaixo (pode ter várias linhas).")
print("2. Quando terminar de colar, aperte ENTER, depois CTRL+Z (no Windows) e ENTER de novo para processar.\n")

import sys
entrada_usuario = sys.stdin.read() 


placas_extraidas = re.findall(r'[A-Z0-9]{7}', entrada_usuario.upper().replace("-", "").replace(" ", ""))

if placas_extraidas:
    df = pd.DataFrame(placas_extraidas, columns=['Placa'])
    df['Data'] = datetime.now().strftime("%d/%m/%Y")
    df['Horario_Processamento'] = datetime.now().strftime("%H:%M:%S")
    
    nome_arquivo = f"Relatorio_Massa_{datetime.now().strftime('%H%M%S')}.xlsx"
    df.to_excel(nome_arquivo, index=False)
    
    print(f"\n✅ SUCESSO! {len(placas_extraidas)} placas processadas.")
else:
    print("❌ Nenhuma placa encontrada.")
