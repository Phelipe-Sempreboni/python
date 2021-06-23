import cx_Oracle

uid = 'SYSTEM'
pwd = 'LP23420v*' 
db = 'localhost:1521/xe'
 
connection = cx_Oracle.connect(uid+'/'+pwd+'@'+db)

cursor = connection.cursor() # cria um cursor

cursor.execute('SELECT * FROM TBL_PRODUTOS') # consulta sql
result = cursor.fetchall()  # busca o resultado da consulta
if result == None:
    print ('Nenhum Resultado')
    exit
else:
    while result:
        print (result[0])
        result = cursor.fetchone()
cursor.close()
connection.close()


import cx_Oracle

uid = "SYSTEM"
pwd = "LP23420v*" 
db = 'localhost:1521/xe'
 
connection = cx_Oracle.connect(uid+"/"+pwd+"@"+db)
print (connection.version)
connection.close()