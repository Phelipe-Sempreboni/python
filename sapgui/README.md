---

## Métodos de login no SAP GUI com Python

---

### LEIA-ME

---

- Este repositório foi criado para alocação de scripts que realizam o login no SAP GUI com Python.

- Neste repositório explicaremos como cada script funciona de acordo com o seu repositório.

- Dessa maneira as buscas por scripts e suas utilidades ficam mais claras e fáceis para compartilhar com nossa comunidade.

---

- [x] Como é realizada a divisão ?

- Sempre iremos indicar o nome do repositório, pois, todos os scripts terão o nome padrão (script) e em casos especificis pode mudar, mas para maioria dos casos sempre será este nome.

- Então sempre atente que será o nome do repositório e em seguida a descrição do que o script executa.

---

- [x] 1 - connection method:

- #### Função principal do script:

  - Realizar o login no SAP GUI com usuário e senha fixas com Python.

- #### O que esse script faz ?:

  - Verificar a possibilidade de um erro de forma geral desde a abertura das telas do SAP GUI até o login com o usuário e senha. Essa verificação fica em um bloco (try) com (except).

  - Insere o usuário e senha na tela do SAP GUI e entra na próxima tela, que seria a inicial.

- #### Pontos para atentar ao utilizar o script:

  - É necessário realizar a alteração da variável (path), que indica o caminho do executável (.exe) do Python na máquina que estiver alocado.

  - É necessário alterar a variável (connection = application.OpenConnection("SAP", True)), onde o ("SAP") deve ser o módulo que você deseja entrar, por exemplo ("CCS PRODUTIVO"). Altere este local para seu módulo do SAP GUI.

  - Realize a alteração de usuário e senha de acordo com suas necessidades.

  - Para este caso é necessário a instalação de um módulo, que está no arquivo (requirements.txt). É possível instalar diretamente pelo Prompt de Comando se for Windows, ou também é possível instalar diretamente pelo arquivo (requirements.txt). Consulte este tutorial: https://github.com/Phelipe-Sempreboni/python/blob/main/tutorials/installing%20or%20exporting%20libraries%20with%20requirements.txt/documentation.md

---

[Acesse meu GitHub :cat:](https://github.com/Phelipe-Sempreboni)

[Acesse meu LinkedIn :computer:](https://www.linkedin.com/in/luiz-phelipe-utiama-sempreboni-319902169/)

---

_Espero ajudar_ :smiley:

---


