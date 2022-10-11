#Importando as bibliotecas
import plotly.express as plt
import pandas as pd

#Preencha essa variável com o seu path para acessar um arquivo csv:
loc_df ='seu_path/seu_arquivo.csv'

#Fazendo o arquivo csv ser lido pelo pandas:
df = pd.read_csv(loc_df)

#Limitando uma amostra para uso:
new_df = df[3:15]

#Tirando dados que não são variáveis válidas para a respresentação(Not a Numbers):
print(new_df.dropna())

#Criando dicionário à partir do seu csv:
dicionario_do_grafico = {'paises': new_df['country'], 'toneladas de metano por cabeça': new_df['methane_per_capita']}

#Associando o dicionário criado à um gráfico plt(Plotly):
fig = plt.bar(dicionario_do_grafico, x = 'paises', y='toneladas de metano por cabeça', color_discrete_sequence = ['green'])

#Baixando um arquivo html que represente o gŕafico:
fig.write_html('emissions.html')

#Mostrando o gráfico que foi baixado:
fig.show()
