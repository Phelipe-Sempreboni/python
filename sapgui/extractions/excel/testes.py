import win32com.client

def close_excel():

    excel = win32com.client.Dispatch('Excel.Application')

    workbook_1 = nome_caminho + nome_arquivo_principal

    workbook_2 = nome_caminho + nome_arquivo_complemento

    if workbook_1 == nome_caminho + nome_arquivo_principal:

        excel.Close()