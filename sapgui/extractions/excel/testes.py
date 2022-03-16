import win32com.client

# Variável que cria a aplicação do excel para utilização.
excel = win32com.client.Dispatch('Excel.Application')

# Comando para desativar os possíveis alertas quando fechar o excel.
excel.DisplayAlerts = False

# Comando para sair do excel.
excel.Quit()