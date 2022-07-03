from pybliometrics.scopus import AbstractRetrieval

import pandas as pd
xlsx = pd.ExcelFile('candidatos.xlsx', engine='openpyxl')  
df = pd.read_excel(xlsx) # Read an Excel file into a pandas DataFrame.

from pybliometrics.scopus import AuthorRetrieval

Fator_H = []
n_citacoes = []
n_documentos = []
x = 0
for x in range(df['ID'].count()):
    auau = AuthorRetrieval(df['ID'][x])
    print("ID Number of author: ", df['ID'][x])
    print("Índice H: ", auau.h_index)
    Fator_H.append(auau.h_index)
    print("Número de citações: ", auau.citation_count)
    n_citacoes.append(auau.citation_count)
    print("Número de documentos publicados: ", auau.document_count)
    n_documentos.append(auau.document_count)

df1 = pd.DataFrame(columns=['ID', 'Candidato', 'Indice H', 'Numero de citacoes', 'i10', 'i20', 'Numero de documentos'])
df1['ID'] = df['ID']
df1['Candidato'] = df['Nome']
df1['Indice H'] = Fator_H
df1['Numero de citacoes'] = n_citacoes
df1['Numero de documentos'] = n_documentos

# Create the function to obtain the index i10
def i10(): 
    from pybliometrics.scopus import AuthorRetrieval
    from pybliometrics.scopus import AbstractRetrieval
    from pybliometrics.scopus import ScopusSearch

    f=0
    for f in range(df['ID'].count()):
        auau = AuthorRetrieval(df['ID'][f])
        ID_number = df['ID'][f]
        ne = 'AU-ID('+str(ID_number)+')' 
        s = ScopusSearch(ne, integrity_fields=["eid"], integrity_action="warn")
        print("s: ", s)
        print("get_eids: ", s.get_eids())
        x = 0 
        z = 0
        print("número de documentos: ", auau.document_count)
        for x in range(auau.document_count):
            print("artigo : ", s.get_eids()[x]) 
            ab = AbstractRetrieval(s.get_eids()[x], view='FULL')
            print(ab.citedby_count) 
            if ab.citedby_count > 10 or ab.citedby_count == 10:
                z+=1 
        print("Índice i10 = ", z)       
        df1['i10'][f] = z
    
# Create the function to obtain the index i20
def i20():
    from pybliometrics.scopus import AuthorRetrieval
    from pybliometrics.scopus import AbstractRetrieval
    from pybliometrics.scopus import ScopusSearch

    f=0
    for f in range(df['ID'].count()):
        auau = AuthorRetrieval(df['ID'][f])
        ID_number = df['ID'][f]
        ne = 'AU-ID('+str(ID_number)+')' 
        s = ScopusSearch(ne, integrity_fields=["eid"], integrity_action="warn")
        print("s: ", s)
        print("get_eids: ", s.get_eids())
        x = 0 
        z = 0
        print("número de documentos: ", auau.document_count)
        for x in range(auau.document_count):
            print("artigo : ", s.get_eids()[x]) 
            ab = AbstractRetrieval(s.get_eids()[x], view='FULL')
            print(ab.citedby_count) 
            if ab.citedby_count > 20 or ab.citedby_count == 20:
                z+=1 
        print("Índice i20 = ", z)       
        df1['i20'][f] = z
    
i10()
i20()

# Organizes selection according to metrics ranking
df1.sort_values(by=['Indice H','Numero de citacoes', 'i10', 'i20', 'Numero de documentos'],ascending=False).to_csv('results.csv')

print(df1)