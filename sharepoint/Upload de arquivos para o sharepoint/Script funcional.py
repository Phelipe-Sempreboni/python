'''

O script abaixo é para realizar o upload de arquivos locais para o SharePoint.

Lembre-se de realizar a leitura dos comentários e alterar os links, usuário e senha nos locais indicados.

'''

# Importação de bibliotecas.
import os
from office365.sharepoint.client_context import ClientContext

# Variáveis com alocação das urls conforme abaixo.
# Os nomes das variáveis podem ser alteradas, porém, será necessário alterar as demais que possuem os mesmos nomes/chamadas no script.
gov_site_url ='https://empresa_ficticia.sharepoint.com/sites/empresa_ficticia_docs/' # Insira a url de acordo com o exemplo. 
gov_doc_repositorio ='Documentos%20Compartilhados/PERSONAL' # Insira a url de acordo com o exemplo. 
gov_doc_repositorio_pasta_principal ='ARQUIVOS' # Insira a url de acordo com o exemplo. 

# Variáveis com as credenciais.
# Insira suas credenciais.
u ='Insira aqui o usuário'
s ='Insira aqui a senha'

# Localidade do arquivo que será realizado o upload para o Sharepoint.
arquivos =r"C:\Users\teste.xlsx"
nome_arquivo =os.path.basename(arquivos)

# Criando a conexão por um client que irá conectar no Sharepoint com as variáveis de credenciais.
conexao = ClientContext(gov_site_url).with_user_credentials(u, s)

# Acessando o repositório do Sharepoint, onde será verificado se o repositório existe e senão existir, será criado.
caminho_repositorios ="/{0}/{1}".format(gov_doc_repositorio, gov_doc_repositorio_pasta_principal)
repositorios  =  conexao.web.ensure_folder_path(caminho_repositorios).execute_query()

# 4. Realiza a leitura do arquivo, onde faz a leitura pela variável de arquivos.
with open(arquivos,'rb') as objeto_arquivo:
  conteudo_arquivo = objeto_arquivo.read()

# Realiza o upload do arquivo no repositório de desstino.
arquivo = repositorios.upload_file(nome_arquivo, conteudo_arquivo)
conexao.execute_query()

# Finalizado.