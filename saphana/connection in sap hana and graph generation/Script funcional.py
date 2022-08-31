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
def query_exec():
    
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
    resultado = query_exec()
    print('Finish query execution: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
    
    print('')
    print('Total registers: ' + str(len(resultado)))
    print('')
    
    num_intervals = 7
    total_regs = len(resultado)
    
    intervals_size = int(total_regs / num_intervals) + 1
    interval_i = 0
    interval_f = intervals_size 
    
    tmp_df = pd.DataFrame()
    
    #out = csv.writer(open('v3.csv','w'), delimiter=',')
    #out.writerows(resultado)
    
    for i in range (num_intervals):
        if interval_f > total_regs:
            interval_f = total_regs
        print ('Intervalos: ' + str(interval_i) + ' - ' + str(interval_f) + ' ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))

        #print('Start dataframe creation: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
        cabecalho = ['instalacao', 'carga', 'nivel_t', 'classe_subclasse','n_fases', 'classe_calc']
        data_f = pd.DataFrame.from_records(resultado[interval_i:interval_f], columns=cabecalho)
        #print('Finish dataframe creation: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
        interval_i = interval_f 
        interval_f += intervals_size 
        #data_f.to_csv('tmp_df_'+str(i)+'.csv', sep=';')
        #print (len(data_f))
        #print( '' )
        #resultado[:] = [] #Free memory
        #print('Memory cleared: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
    
        #print( '' )
        data_f['padrao_atend'] = ''
        #print('padrao_atend column created: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
    
        data_f['corrente'] = ''
        #print('corrente column created: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
    
        data_f['carga'] = data_f['carga'].str.replace(',','.')
    
        #Nivel de tensao
        #print('Prep nivel de tensao: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
        data_f.loc[ pd.to_numeric(data_f['nivel_t'], errors = 'ignore') == 1 , 'nivel_t' ] = 120/1000
        data_f.loc[ pd.to_numeric(data_f['nivel_t'], errors = 'ignore') == 2 , 'nivel_t' ] = 240/1000
        data_f.loc[ pd.to_numeric(data_f['nivel_t'], errors = 'ignore') == 3 , 'nivel_t' ] = 127/1000
        data_f.loc[ pd.to_numeric(data_f['nivel_t'], errors = 'ignore') == 4 , 'nivel_t' ] = 220/1000
        data_f.loc[ pd.to_numeric(data_f['nivel_t'], errors = 'ignore') == 5 , 'nivel_t' ] = 220/1000
        data_f.loc[ pd.to_numeric(data_f['nivel_t'], errors = 'ignore') == 6 , 'nivel_t' ] = 380/1000
        data_f.loc[ pd.to_numeric(data_f['nivel_t'], errors = 'ignore') == 14 , 'nivel_t' ] = 208/1000
    
        #Corrente   
        #print('Prep corrente: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
        data_f.loc[ data_f['n_fases'] <= 2 , 'corrente'] =  pd.to_numeric(data_f['carga'], errors = 'ignore') / pd.to_numeric(data_f['nivel_t'], errors = 'ignore')    
        data_f.loc[ data_f['n_fases'] == 3 , 'corrente'] =  pd.to_numeric(data_f['carga'], errors = 'ignore') / ( pd.to_numeric(data_f['nivel_t'], errors = 'ignore') * math.sqrt(3))
    
        #Padrao de atendimento
        #print('Prep padrao de atendimento: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
        data_f.loc[ (data_f['classe_calc'] == 'ELGA') & ( pd.to_numeric(data_f['corrente'], errors = 'ignore') <= 50) , 'padrao_atend'] = 'A1'
        data_f.loc[ (data_f['classe_calc'] == 'ELGA') & ( ( pd.to_numeric(data_f['corrente'], errors = 'ignore') > 50 ) & ( pd.to_numeric(data_f['corrente'], errors = 'ignore') <=70 )) , 'padrao_atend'] = 'A2'
        data_f.loc[ (data_f['classe_calc'] == 'ELGA') & ( pd.to_numeric(data_f['corrente'], errors = 'ignore') > 70 ), 'padrao_atend'] = 'ELGA >70 nao tem na LIG2000'
    
        data_f.loc[ (data_f['classe_calc'] == 'ELGB') & ( pd.to_numeric(data_f['corrente'], errors = 'ignore') <= 50) , 'padrao_atend'] = 'B3 e C3'
        data_f.loc[ (data_f['classe_calc'] == 'ELGB') & ( ( pd.to_numeric(data_f['corrente'], errors = 'ignore') > 50 ) & ( pd.to_numeric(data_f['corrente'], errors = 'ignore') <=63 )) , 'padrao_atend'] = 'B4 e C4'
        data_f.loc[ (data_f['classe_calc'] == 'ELGB') & ( ( pd.to_numeric(data_f['corrente'], errors = 'ignore') > 63 ) & ( pd.to_numeric(data_f['corrente'], errors = 'ignore') <=80 )) , 'padrao_atend'] = 'B5 e C5'
        data_f.loc[ (data_f['classe_calc'] == 'ELGB') & ( ( pd.to_numeric(data_f['corrente'], errors = 'ignore') > 80 ) & ( pd.to_numeric(data_f['corrente'], errors = 'ignore') <=100 )) , 'padrao_atend'] = 'B6 e C6'
        data_f.loc[ (data_f['classe_calc'] == 'ELGB') & ( ( pd.to_numeric(data_f['corrente'], errors = 'ignore') > 100 ) & ( pd.to_numeric(data_f['corrente'], errors = 'ignore') <=125 )) , 'padrao_atend'] = 'B7 e C7'
        data_f.loc[ (data_f['classe_calc'] == 'ELGB') & ( ( pd.to_numeric(data_f['corrente'], errors = 'ignore') > 125 ) & ( pd.to_numeric(data_f['corrente'], errors = 'ignore') <=150 )) , 'padrao_atend'] = 'B8 e C8'
        data_f.loc[ (data_f['classe_calc'] == 'ELGB') & ( ( pd.to_numeric(data_f['corrente'], errors = 'ignore') > 150 ) & ( pd.to_numeric(data_f['corrente'], errors = 'ignore') <=200 )) , 'padrao_atend'] = 'B9 e C9'
        data_f.loc[ (data_f['classe_calc'] == 'ELGB') & ( ( pd.to_numeric(data_f['corrente'], errors = 'ignore') > 200 ) & ( pd.to_numeric(data_f['corrente'], errors = 'ignore') <=225 )) , 'padrao_atend'] = 'B10 e C10'
        data_f.loc[ (data_f['classe_calc'] == 'ELGB') & ( ( pd.to_numeric(data_f['corrente'], errors = 'ignore') > 225 ) & ( pd.to_numeric(data_f['corrente'], errors = 'ignore') <=275 )) , 'padrao_atend'] = 'B11 e C11'
        data_f.loc[ (data_f['classe_calc'] == 'ELGB') & ( ( pd.to_numeric(data_f['corrente'], errors = 'ignore') > 275 ) & ( pd.to_numeric(data_f['corrente'], errors = 'ignore') <=300 )) , 'padrao_atend'] = 'B12 e C12'
        data_f.loc[ (data_f['classe_calc'] == 'ELGB') & ( ( pd.to_numeric(data_f['corrente'], errors = 'ignore') > 300 ) & ( pd.to_numeric(data_f['corrente'], errors = 'ignore') <=350 )) , 'padrao_atend'] = 'B13 e C13'
        data_f.loc[ (data_f['classe_calc'] == 'ELGB') & ( pd.to_numeric(data_f['corrente'], errors = 'ignore') > 350 ), 'padrao_atend'] = 'ELGB >350 nao tem na LIG2000'
    
    
        #print( '' )
        #print('Del unnecessary columns' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
        data_f.drop(['carga', 'nivel_t', 'n_fases', 'classe_calc'], axis = 1, inplace = True)
    
        #print('start filter padrao_atend = B3 e C3: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
        data_f = data_f[data_f['padrao_atend'] == 'B3 e C3']
        data_f.drop(['padrao_atend'], axis = 1, inplace = True)
          
        
        #print( '' )
        #print('start groupby by classe_subclasse and corrente: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
        
        ddf = data_f.groupby(['classe_subclasse', 'corrente']).count().reset_index()
        #ddf.to_csv('v3_ddf_'+ str(i)+'.csv', sep=';')
        #print (len(ddf))
        tmp_df = tmp_df.append(ddf ,ignore_index=True)
        
        
    tmp_df2 = tmp_df.groupby(['classe_subclasse', 'corrente']).sum().reset_index()
    
    #tmp_df2.to_csv('v3_tmp_df2_t.csv', sep=';')    
    print ('')
    #tmp_df.to_csv('tmp_df.csv', sep=';')
    print ('')
    print('start graphs: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
    data_f_grouped_classe_sub = tmp_df2.groupby('classe_subclasse')
    for group_name, data in data_f_grouped_classe_sub:
        #plt.figure()
        tmp_df2[tmp_df2['classe_subclasse'] == group_name].sort_values('instalacao').plot(x = 'instalacao', y = 'corrente', title ='Classe '+group_name)
        plt.savefig('plot_'+ group_name + '.png')
        plt.close('all')
    
    print ('')
    print('Finish time: ' + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
    print('Runtime: ' + str(time.time() - start_time) + ' in seconds')
