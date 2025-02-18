import os
import pandas as pd

def processar_dados(dados):
    if dados:
        
        
        #usamos o zip para tranformar a lista de tuplas coletadas no método "coletarDados" em um dataframe
        nomes_produtos, avaliacoes_produtos, links_produtos = zip(*dados)
        dataFrame = {
            'PRODUTO': nomes_produtos,
            'AVALIACAO': avaliacoes_produtos,
            'URL': links_produtos
        }

        df = pd.DataFrame(dataFrame)
        
        #filtro no dataframe para remoser os produtos com avaliação vazia
        df = df[df['AVALIACAO'] != '']
        #regex para pegar o número de avaliações
        
        df['QTD_AVAL'] = df['AVALIACAO'].str.extract(r'\((\d+)\)')[0].astype(int)
        
        #filtro para separar as maiores e menores avaliações
        df = df[['PRODUTO', 'QTD_AVAL', 'URL']]
        piores_df = df[df['QTD_AVAL'] < 100]
        melhores_df = df[df['QTD_AVAL'] >= 100]
        
        #verificação para criar pastas se necessário
        if not os.path.exists('Output'):
            os.makedirs('Output') #cria a pasta    
        
        with pd.ExcelWriter('Output/Notebooks.xlsx') as writer:
            piores_df.to_excel(writer, sheet_name='Piores', index=False)
            melhores_df.to_excel(writer, sheet_name='Melhores', index=False)

        print("Dados salvos com sucesso em Output/Notebooks.xlsx")
    else:
        print("Nenhum dado foi coletado.")

