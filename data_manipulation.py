# encoding: utf-8
import pandas as pd
import os

os.chdir("C:\\Users\\jhona\\OneDrive\\Área de Trabalho\\SEMEF\\Faturamento\\")
arquivos = os.listdir()

base = "C:\\Users\\jhona\\OneDrive\\Área de Trabalho\\SEMEF\\Faturamento\\"

colunas = ["Classe", "DescricaoClasse", "Parceiro", "NomeParceiro", "CPF/CNPJ", "Instalacao", "Logradouro",
"Numero", "Complemento", "Bairro", "CEP", "Municipio", "DataReferencia", "DocumentoReferencia", "QtdConsumo",
"ValorCIP", "NumeroEquipamento"]

dframe = pd.DataFrame()

for i in range(len(arquivos)): #For que vai varrer cada arquivo da base de dados
    endereco = base + arquivos[i] 
    for chunk in pd.read_csv(endereco, sep = ";", header = None, names = colunas, chunksize = 50000):
        chunk["DataReferencia"] = chunk["DataReferencia"].astype("str")#Mudando o tipo de dados para String
        chunk = chunk[chunk["DescricaoClasse"] == "Res Baixa Renda"] #filtrando por classe
        chunk = chunk[chunk["DataReferencia"].apply(lambda x: x[0:4] == "2019")]#filtrando por data
        dframe = dframe.append(chunk, ignore_index = True)#adicionando ao dataframe final
        print(dframe.shape)
    print("{} de {}\n---------------------------".format(i,len(arquivos)))

#print(dframe.groupby("DataReferencia").describe())#verificando se os dados estão corretos com relação ao ano
#print(dframe.groupby("DescricaoClasse").describe())#verificando se os dados estão corretos com relação à classe

dframe.to_csv("C:\\Users\\jhona\\OneDrive\\Área de Trabalho\\SEMEF\\Faturamento\\MPBaixaRenda2019.csv")


#Rascunhos:
"""
#Mais raschunhos
dfano = dframe["DataReferencia"].apply(lambda x: x[0:4] == "2016") #função lambda aplicada para filtrar por ano
dfano#booleano retornado
dfano2016 = dframe[dfano]#passando o booleano no dataframe
dfano2016 #visualização do dataframe
#FOI O QUE DEU MAIS CERTO
df_2019 = dframe[dframe["DescricaoClasse"] == 'Res Baixa Renda'] #Filtrando por Classe igual à Baixa Renda
df_2019 = df_2019[df_2019["DataReferencia"].apply(lambda x: x[0:4] == "2019")] #Filtrando por ano
df_2019
Salvando o que deu certo kkkkk
df_2019 = dframe[dframe["DescricaoClasse"] == 'Res Baixa Renda']
df_2019 = df_2019[df_2019["DataReferencia"] == "2016/02"]
df_2019
dfano = dframe["DataReferencia"].apply(lambda x: x[0:4] == "2015")
"""