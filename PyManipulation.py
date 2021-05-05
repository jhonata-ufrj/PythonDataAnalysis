import pandas as pd
import os

#Direcionamento para o diretório dos arquivos de Faturamento de 2019
os.chdir("C:\\Users\\jhonatasilva\\Desktop\\python\\LightFaturamento\\Notas2019\\")

#Definindo o local no qual os arquivos finais irão ficar salvos
base = "C:\\Users\\jhonatasilva\\Desktop\\python\\LightFaturamento\\Notas2019\\"

#Listando os arquivos e adicionando em uma variável
arquivos = os.listdir()

#Nome das colunas do Data Frame
colunas = ["Classe", "DescricaoClasse", "Parceiro", "NomeParceiro", "CPF/CNPJ", "Instalacao", "Logradouro",
"Numero", "Complemento", "Bairro", "CEP", "Municipio", "DataReferencia", "DocumentoReferencia", "QtdConsumo",
"ValorCIP", "NumeroEquipamento"]

#Criação de Data Frame vazio
dframe_final = pd.DataFrame()

#Laço de repetição para carregar os arquivos, separando e tratando 50 mil linhas por vez
#com o intuito de poupar memória
for i in range(len(arquivos)):
    endereco = base + arquivos[i]
    for chunk in pd.read_csv(endereco, sep = ";", header = None, names = colunas, chunksize = 50000):
        chunk = chunk[chunk.DescricaoClasse.isin(["Res Baixa Renda"])]
        dframefinal = dframefinal.append(chunk, ignore_index = True)
    #convertendo e salvando o data frame em um arquivo que possa ser lido pelo excel
    dframe_final.to_excel(base + "BaixaRenda2019_" + str(i) + ".xlsx", index = False)
    dframe_final = pd.DataFrame() #limpando o data frame
    


