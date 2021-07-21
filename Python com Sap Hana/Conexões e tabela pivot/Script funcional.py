# Importação da biblioteca. 
# Certifique-se de ter as bibliotecas instaladas.
import pyhdb
import time
import datetime
import math
import pandas as pd
import matplotlib.pyplot as plt
import csv

# Essa função traz/chama outro arquivo que contém a senha, visando não deixar exposta na aplicação.
# Caso não queira utilizar esse método e inserir diretamente a senha na conexão, exclua esse bloco e insira a senha diretamente no bloco (def connect) em (passoword).
def pass_location():
    pass_file = "" # Insira o caminho do arquivo com a senha.
    file = open(pass_file, 'r') # Leiteura do arquivo com read.
    return file.read()

# Realiza a conexão com o Sap Hana.
def connect():
    try:
        connection = pyhdb.connect(
            host = "", # Insira o server.
            port=,  # Insira a porta, normalmente númerica, caso não seja, utilize o ("") para digitar a localidade da porta.
            user="", # Insira o usuário.
            password=pass_location() # Aqui estamos utilizando o bloco (pass_location) que busca a senha em outro arquivo, caso não queira exclua o bloco e insira a senha.
            )
        return connection.cursor()
    except:
        return 1

# Executa a query no Sap Hana.
def query_exec(i_ini, i_fim):

    #A query de exemplo abaixo lista 10 instalacoes da tabela de dados mestres de instalacao
    cursor = connect()
    cursor.execute("SET SCHEMA SAPBP1") # Insira o schema do banco de dados.
    cursor.execute("SELECT top 10 "'"/BIC/EPINSTALA"'" \
                    from "'"SAPBP1"'"."'"/BIC/PEPINSTALA"'" ") # Insira a query.
  
    result = cursor.fetchall() # Retorna todos os resultados.
    cursor.close() # Encerra o cursor.
    return result

# Executa a query no Sap Hana.
def query_get_objetos():

    #A query de exemplo abaixo lista 10 instalacoes da tabela de dados mestres de instalacao
    cursor = connect()
    cursor.execute("SET SCHEMA SAPBP1") # Insira o schema do banco de dados.
    cursor.execute("SELECT top 10 "'"/BIC/EPINSTALA"'" \
                    from "'"SAPBP1"'"."'"/BIC/PEPINSTALA"'" ") # Insira a query.
  
    result = cursor.fetchall() # Retorna todos os resultados.
    cursor.close() # Encerra o cursor.
    return result

# Executa a query no Sap Hana.
def query_get_consumos(i_ini, i_fim):
    
    #A query de exemplo abaixo lista 10 instalacoes da tabela de dados mestres de instalacao
    cursor = connect()
    cursor.execute("SET SCHEMA SAPBP1") # Insira o schema do banco de dados.
    cursor.execute("SELECT top 10 "'"/BIC/EPINSTALA"'" \
                    from "'"SAPBP1"'"."'"/BIC/PEPINSTALA"'" ") # Insira a query.
  
    result = cursor.fetchall() # Retorna todos os resultados.
    cursor.close() # Encerra o cursor.
    return result


if __name__ == '__main__':
    
    start_time = time.time()
    print ('Start time: ' + datetime.datetime.fromtimestamp(start_time).strftime('%c'))
    print ('')
    connect()
    objetos = query_get_objetos()
    print('Finish query execution: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
    total_regs = len(objetos)
    print('')
    print('Total registers: ' + str(len(objetos)))
    print('')
    
    #Ordenar objetos
    print('Inicio ordenacao: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
    objetos.sort()
    print('Fim ordenacao: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
    print ('')
    num_intervals = 21
    intervals_size = int(total_regs / num_intervals) + 1
    interval_i = 0
    interval_f = intervals_size 

    for i in range (num_intervals):
        if interval_f > total_regs:
            interval_f = total_regs - 1

        
        inicio_intervalo = objetos[interval_i][0]
        fim_intervalo = objetos[interval_f][0]
        
        print ('Intervalo: ' + str(inicio_intervalo) + ' - ' + str(fim_intervalo) + ' ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
         
        print ('Inicio query do intervalo : ' + str(i) +' - '+ datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
        resultado = query_exec(inicio_intervalo, fim_intervalo)
        total_regs_intervalo = len(resultado)
        print ('Fim query do intervalo : ' + str(i) +' - '+ datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
        print('Total de registros do intervalo: ' + str(total_regs_intervalo))
        print ('')
        
        if (total_regs_intervalo>0):
            cabecalho = ['instalacao' , 'status_instalacao' , 'unidade_leitura (local pos 2 ate 4) (lote pos 5 e 6)' ,'endereco_completo', 'numero_fases', 
                     'classe_subclasse' , 'coordenada_x' ,'coordenada_y', 'cnae' , 'area_risco', 'regional', 
                     'localidade', 'bairro' , 'parceiro_nome', 'localidade_texto','regional_texto','categoria_tarifa']
        
            data_f = pd.DataFrame.from_records(resultado, columns=cabecalho)

            data_f['municipio'], data_f['endereco'] = data_f['endereco_completo'].str.split(',', 1).str
            
            consumos = query_get_consumos(inicio_intervalo, fim_intervalo)
            cabecalho_c = ['instalacao' , 'periodo','consumos']
            data_f_c = pd.DataFrame.from_records(consumos, columns=cabecalho_c)

            pivot = data_f_c.pivot('instalacao', 'periodo', 'consumos')
            
            data_full = data_f.merge(pivot, how='left', left_on = 'instalacao', right_index = True)
            
            if (i == 0):
                data_full.to_csv('elgb.txt', sep = ';', index=False) # Primeiro arquivo gera com cebecalho
                data_full.to_csv('elgb_check.txt', sep = ';', index=False) # Primeiro arquivo gera com cebecalho
            else:
                data_full.to_csv('elgb.txt', mode = 'a', sep = ';', index=False, header=False) # Depois so acrescenta dados no arquivo
                
            print ('')
        
        interval_i = interval_f 
        interval_f += intervals_size 

        
    print ('')
    print('Finish time: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
    print('Runtime: ' + str(time.time() - start_time) + ' in seconds')
    
    
    
    
    
    
    
    
    
    
    
    
    #resultado = query_exec(0,0)
    #total_regs_intervalo = len(resultado)
    
    #cabecalho = ['instalacao' , 'status_instalacao' , 'unidade_leitura (local pos 2 ate 4) (lote pos 5 e 6)' ,'endereco_completo', 'numero_fases', 
     #                'classe_subclasse' , 'coordenada_x' ,'coordenada_y', 'cnae' , 'area_risco', 'regional', 
     #                'localidade', 'bairro' , 'parceiro_nome', 'localidade_texto','regional_texto','categoria_tarifa']
        
    #data_f = pd.DataFrame.from_records(resultado, columns=cabecalho)
    
    
    #consumos = query_get_consumos()
    
    #cabecalho_c = ['instalacao' , 'periodo','consumos']
    #data_f_c = pd.DataFrame.from_records(consumos, columns=cabecalho_c)
   
    #pivot = data_f_c.pivot('instalacao', 'periodo', 'consumos')
    
    #data_full = data_f.merge(pivot, how='left', left_on = 'instalacao', right_index = True)
    
    #data_full.to_csv('elgb_check.txt', sep = ';', index=False)
    
    #print ('ffff')
    
    #print (data_f_c['consumos'].loc[(data_f_c['instalacao']=='0200728569') & (data_f_c['periodo'] == '201609')])
    
    
    
    