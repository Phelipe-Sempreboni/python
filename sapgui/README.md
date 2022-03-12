---

## Métodos de exclusão de arquivos do tipo Excel com Python

---

### LEIA-ME

---

- Este repositório foi criado para alocação de scripts que realizam exclusões de arquivos do tipo Excel com Python.

- Neste repositório explicaremos como cada script funciona de acordo com o seu repositório.

- Dessa maneira as buscas por scripts e suas utilidades ficam mais claras e fáceis para compartilhar com nossa comunidade.

---

- [x] Como é realizada a divisão ?

- Sempre iremos indicar o nome do repositório, pois, todos os scripts terão o nome padrão (script) e em casos especificis pode mudar, mas para maioria dos casos sempre será este nome.

- Então sempre atente que será o nome do repositório e em seguida a descrição do que o script executa.

---

- [x] 1 - delete method:

- #### Função principal do script:

  - Realizar a exclusão de arquivos do repositório e/ou servidor e mantém o arquivo do tipo Excel.

- #### O que esse script faz ?:

  - Verifica se o nome arquivo setado pelo usuário manualmente é igual ao nome do arquivo que o loop for está percorrendo pela variável (file).

  - Se ambos nomes forem iguais, então este arquivo do tipo Excel é ignorado com o comando (continue), ou seja, o arquivo é mantido no repositório.

  - Caso ambos nomes sejam diferentes, então é executado o (else), e os demais arquivos serão excluídos, inclusive se no repositório haver arquivos do tipo Excel, porém, com o nome diferente do que foi setado manualmente pelo usuário.

- #### Pontos para atentar ao utilizar o script:

  - Este é um script de (caminho fixo), ou seja, o usuário necessita realizar a alteração manualmente do local que ele necessita que seja executado este script.

  - É necessário realizar a inserção do caminho manualmente do repositório e/ou servidor onde se deseja realizar a exclusão do arquivo.

  - É necessário realizar a inserção do nome do arquivo do tipo Excel, onde este arquivo do tipo Excel será ignorado pelo script e os demais arquivos serão todos excluídos do repositório e/ou servidor.

  - Para este caso não é necessário a instalação de novos módulos novos, pois, os módulos utilizados são nativos do Python. Caso ocorra algum erro relacionado a módulos, por favor, verifique se o seu Python realmente tem o módulo instalado.

---

- [x] 2 - delete method:

- #### Função principal do script:

  - Realizar a exclusão do arquivo do tipo Excel do repositório e/ou servidor e manter os demais arquivos com qualquer tipo de extensão.

- #### O que esse script faz ?:

  - Verifica se o nome arquivo setado pelo usuário manualmente é igual ao nome do arquivo que o loop for está percorrendo pela variável (file).

  - Se ambos nomes forem iguais, então este arquivo do tipo Excel é excluído do repositório e/ou servidor.

  - Caso ambos nomes sejam diferentes, então é executado o (else), e os demais arquivos serão mantidos, pois é executado o comando (continue) que ignora e mantém esses arquivos. Notar que podemos ter arquivos da extensão do tipo Excel no repositório e/ou servidor, porém, se esses arquivos não forem o mesmo do nome setado pelo usuário manualmente, então, esse arquivo será mantido.

- #### Pontos para atentar ao utilizar o script:

  - Este é um script de (caminho fixo), ou seja, o usuário necessita realizar a alteração manualmente do local que ele necessita que seja executado este script.

  - É necessário realizar a inserção do caminho manualmente do repositório e/ou servidor onde se deseja realizar a exclusão do arquivo.

  - É necessário realizar a inserção do nome do arquivo do tipo Excel, onde este arquivo do tipo Excel será ignorado pelo script e os demais arquivos serão todos excluídos do repositório e/ou servidor.

  - Para este caso não é necessário a instalação de novos módulos novos, pois, os módulos utilizados são nativos do Python. Caso ocorra algum erro relacionado a módulos, por favor, verifique se o seu Python realmente tem o módulo instalado.
  
---

- [x] 3 - delete method:

- #### Função principal do script:

  - Realizar a exclusão de arquivos do repositório e/ou servidor e mantém o arquivo do tipo Excel.

- #### O que esse script faz ?:

  - Verifica se o repositório setado manualmente pelo usuário realmente existe. Caso não exista o script apresentará uma mensagem e será encerrado.
  
  - Verifica os arquivos existentes no repositório e/ou servidor setado manualmente pelo usuário.

  - Verifica se o repositório setado manualmente pelo usuário é o mesmo que o loop for está realmente percorrendo.

  - Verifica se o nome arquivo setado pelo usuário manualmente é igual ao nome do arquivo que o loop for está percorrendo pela variável (file).

  - Se ambos nomes forem iguais, então este arquivo do tipo Excel é ignorado com o comando (continue), ou seja, o arquivo é mantido no repositório.

  - Caso ambos nomes sejam diferentes, então é executado o (else), e os demais arquivos serão excluídos, inclusive se no repositório haver arquivos do tipo Excel, porém, com o nome diferente do que foi setado manualmente pelo usuário.

  - Todo esse bloco está dentro de um bloco principal (try) com (except). Caso o programa não consiga executar o processo de exclusão, então o (except) do (try) é acionado e exibida uma mensagem para o usuário que não foi possível realizar o processo de exclusão de arquivos.

- #### Pontos para atentar ao utilizar o script:

  - Este é um script de (caminho fixo), ou seja, o usuário necessita realizar a alteração manualmente do local que ele necessita que seja executado este script.

  - É necessário realizar a inserção do caminho manualmente do repositório e/ou servidor onde se deseja realizar a exclusão do arquivo.

  - É necessário realizar a inserção do nome do arquivo do tipo Excel, onde este arquivo do tipo Excel será ignorado pelo script e os demais arquivos serão todos excluídos do repositório e/ou servidor.

  - Para este caso não é necessário a instalação de novos módulos novos, pois, os módulos utilizados são nativos do Python. Caso ocorra algum erro relacionado a módulos, por favor, verifique se o seu Python realmente tem o módulo instalado.

---

- [x] 4 - delete method:

- #### Função principal do script:

  - Realizar a exclusão do arquivo do tipo Excel do repositório e/ou servidor e manter os demais arquivos com qualquer tipo de extensão.

- #### O que esse script faz ?:

  - Verifica se o repositório setado manualmente pelo usuário realmente existe. Caso não exista o script apresentará uma mensagem e será encerrado.
  
  - Verifica os arquivos existentes no repositório e/ou servidor setado manualmente pelo usuário.

  - Verifica se o repositório setado manualmente pelo usuário é o mesmo que o loop for está realmente percorrendo.

  - Verifica se o nome arquivo setado pelo usuário manualmente é igual ao nome do arquivo que o loop for está percorrendo pela variável (file).

  - Se ambos nomes forem iguais, então este arquivo do tipo Excel é excluído do repositório e/ou servidor.

  - Caso ambos nomes sejam diferentes, então é executado o (else), e os demais arquivos serão mantidos, pois é executado o comando (continue) que ignora e mantém esses arquivos. Notar que podemos ter arquivos da extensão do tipo Excel no repositório e/ou servidor, porém, se esses arquivos não forem o mesmo do nome setado pelo usuário manualmente, então, esse arquivo será mantido.

  - Todo esse bloco está dentro de um bloco principal (try) com (except). Caso o programa não consiga executar o processo de exclusão, então o (except) do (try) é acionado e exibida uma mensagem para o usuário que não foi possível realizar o processo de exclusão de arquivos.

- #### Pontos para atentar ao utilizar o script:

  - Este é um script de (caminho fixo), ou seja, o usuário necessita realizar a alteração manualmente do local que ele necessita que seja executado este script.

  - É necessário realizar a inserção do caminho manualmente do repositório e/ou servidor onde se deseja realizar a exclusão do arquivo.

  - É necessário realizar a inserção do nome do arquivo do tipo Excel, onde este arquivo do tipo Excel será ignorado pelo script e os demais arquivos serão todos excluídos do repositório e/ou servidor.

  - Para este caso não é necessário a instalação de novos módulos novos, pois, os módulos utilizados são nativos do Python. Caso ocorra algum erro relacionado a módulos, por favor, verifique se o seu Python realmente tem o módulo instalado.

---

[Acesse meu GitHub :cat:](https://github.com/Phelipe-Sempreboni)

[Acesse meu LinkedIn :computer:](https://www.linkedin.com/in/luiz-phelipe-utiama-sempreboni-319902169/)

---

_Espero ajudar_ :smiley:

---


