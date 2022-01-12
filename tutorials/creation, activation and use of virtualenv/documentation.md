## Criando, ativando e utilizando o ambiente virtual (virtualenv) do Python no Windows

---

Podemos utilizar esse método no Windows com:

- Visual Studio Code
- PyCharm
- Prompt de Comando

---

Certifique-se de ter o Python instalado em sua máquina corretamente.

Para verificar siga os passos abaixo:

1º - Abra o Prompt de Comando.

2º - Digite o comando (python --version).

3º - Caso seja apontado a versão do Python no Prompt de Comando, logo você tem o Python instalado e pode continuar com o tutorial.

---

1º - Abrir a ferramenta que será realizado a criação, ativação e utilização da virtualenv do Python.

---

2º - Criar em algum local do seu computador ou server, uma repositório (pasta), por exemplo, o repositório (Projeto). Aconselho criar para treinamento no (Desktop).

---

3º - Criação do ambiente virtual no repositório que foi criado anteriormente.

```python

# Digitar e entrar no caminho do repositório que foi criado anteriormente. Faça isso pela ferramente que está utilizando como terminal.

# Digite o comando (cd), seguido de espaço, e procure pelo local do repositório criado anteriormente.

# Exemplo abaixo para entrar no repositório criado.

C:\User\Zé>cd Desktop\Projeto> 

```
4º - Digitar o comando abaixo do Python para criar a virtualenv. Notar que este passo é realizado assim que conseguir entrar no repositório origem que foi criado anteriormente.

```python

# Com o comando é realizado a criação do ambiente virtual.

# Notar que quando digitamos o primeiro (venv), é referente ao comando do Python, não podendo ser alterado.

# Notar que quando digitamos o segundo (venv), é referente ao nome que você pode dar a seu ambiente virtual. Pode ser qualquer coisa, mas por padrão, criarei como (venv).

# Digite o comando, aperte enter e aguarde a criação. Pode ser verificado entrando diretamente no repositório que foi criado anteriormente.

C:\User\Zé\Desktop\Projeto> python -m venv venv 

```

5º - Digitar o comando abaixo do Python para ativar a virtualenv que foi criada no repositório.

```python

# Digite o comando para ativar a virtualenv e conseguir utilizar o ambiente virtual.

# Após ativação do ambiente virtual, o caminho ficará parecido com isso "(venv) C:\User\Zé\Desktop\Projeto>"

# Notar que caso você tenha nomeado, sua virtualenv com outro nome, como (teste_env), então, o comando abaixo ficaria (C:\User\Zé\Desktop\Projeto> .\teste_env\Scripts\activate.bat), então, depende da nomeação que você deu na criação do seu ambiente virtual.

C:\User\Zé\Desktop\Projeto> .\venv\Scripts\activate.bat

```

6º - Para testar a virtualenv, digite o comando o abaixo para instalar a biblioteca, e caso seja instalada corretamente, a virtualenv está funcionando e é possível utilizar o ambiente virtual com segurança e em seus projetos.

```python

# Digamos que esteja ativada o ambiente, digite o comando (pip install pandas).

(venv) C:\User\Zé\Desktop\Projeto> pip install pandas

```

Ambiente virtual criado, ativado e pronto para utilização.

---

Fim do tutorial.

---

_Espero ajudar_ :smiley:

