'''

created by: Luiz Phelipe Utiama Sempreboni

Script para:
- Conexão com o SAP GUI com solicitação de usuário e senha para o usuário.
- Limpeza e/ou exclusão de arquivos anteriores do repositório atual que os arquivos serão salvos, onde, este repositório sempre será limpo no início do script.
- Entrar na transação do SAP GUI para iniciar o processo, onde neste caso é uma transação ficticia.
- Executar os comandos automatizados do SAP GUI pelo script.
- Realizar a extração das bases de dados.
- Salvar as bases de dados.
- Finalizar o script.

'''

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Importação de módulos

import win32com.client  # Módulo para criação de componentes COM (Common Object Model) em Python. Pode-se tanto criar componentes para serem utilizados por outras linguagens/aplicações (servidores) quanto criar objetos previamente existentes (clientes) criados em outras linguagens.
import sys  # Módulo para fornecer funções e variáveis usadas para manipular diferentes partes do ambiente de tempo de execução do Python e apesar de serem completamente diferentes, muitas pessoas confundem o módulo sys e o módulo os (módulo para manipular o sistema operacional).
import os  # Módulo para fornecer acesso a funções específicas do sistema para lidar com o sistema de arquivos, processos, planejador, etc.
import glob  # Módulo usado para retornar todos os caminhos de arquivo que correspondem a um padrão específico.
import subprocess  # Módulo subprocess permite que você execute programas externos e inspecione suas saídas com facilidade.
import time  # Módulo provê várias funções relacionadas à tempo, onde neste caso estamos utilizando para a função (sleep).
from datetime import datetime  # Módulo fornece classes para manipular datas e tempo de forma simples ou complexas. Apesar de cálculos aritméticos com data e tempo serem suportados, o foco da implementação está na extração eficiente de atributo para formatar resultados e manipulação.
import getpass  # Módulo para mascarar a senha quando é inserida no terminal.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável da data atual para inserção nos campos do SAP GUI, neste caso a variável (data).
# Variável (data_atual) formata o padrão da data.
# Essa data fica pré definida para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
data = datetime.now()
data_atual = data.strftime('%d.%m.%Y')

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável da hora atual para inserção nos campos do SAP GUI, neste caso a variável (hora_atual).
# Essa hora fica pré definida para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
hora_atual = time.strftime('%Hh%M', time.localtime())

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável com o endereço do caminho onde as bases de dados extraídas do SAP GUI serão salvas.
# Esse caminho fica pré definido para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
nome_caminho = r'C:\Windows\Temp\testes'

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável com o nome do arquivo que será salvo na extração do SAP GUI.
# Esse caminho fica pré definido para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
nome_arquivo_principal = r'\Notas - Principal.xlsx'

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável com o nome do arquivo que será salvo na extração do SAP GUI. Neste caso, seria por exemplo, um arquivo complementar da extração ou um segundo arquivo de extração.
# Esse caminho fica pré definido para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
nome_arquivo_complemento = r'\Notas - Complemento.xlsx'

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável (nome_txt) que monta o nome de um arquivo no formato (txt) para indicar no final do script, a data e hora da atualização.
# Variável (nome_txt_caminho) que concatena o caminho dos arquivos da extração do SAP GUI e o arquivo montado com a informação da da variável (nome_txt).
nome_txt = r'\Atualização em ' + data_atual + ' às ' + hora_atual + '.txt'
nome_txt_caminho = nome_caminho + nome_txt

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Bloco de try para tentar realizar a execução abaixo.
try:

    # 1º nível de verificação de (locais - root), (repositórios - dirs), (arquivos - files).
    for root, dirs, files in os.walk(nome_caminho):

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# 2º nível de verificação de (locais - root), (repositórios - dirs), (arquivos - files).
# Este (if) verifica se o (local - root) é o mesmo do repositório (nome_caminho), visto que os arquivos utilizados estão neste repositório.
# Também certifica que o script não percorra outros repositórios dentro do repositório principal da variável (nome_caminho).
        if root == nome_caminho:

            # Imprimir mensagem de validação do repositório atual ao usuário.
            print('Validação do repositório atual: ' + root + '.\n')

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

