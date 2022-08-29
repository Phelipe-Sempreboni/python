## Instalação de bibliotecas e dependências utilizando o arquivo requirements.txt

---

Tutorial para demonstrar com utilizar um arquivo (requirements.txt) com bibliotecas do Python para instalação.

---

1º - Criar um arquivo chamado (requirements.txt), de preferência em seu projeto, por exemplo, se estiver utilizando um projeto em uma virtualenv.

---

2º - Abrir o arquivo (requirements.txt) e inserir o nome das bibliotecas e dependências, sempre seguindo o modelo do exemplo abaixo.

- nome_biblioteca==versão

- pandas==1.3.5

---

3º - Salvar e fechar o arquivo (requirements.txt).

---

4º - Ir até o local que está seu projeto ou repositório e também seu arquivo (requirements.txt). Exemplo abaixo.

```python

# O primeiro exemplo é se for em um projeto local.
# O segundo exemplo é se estiver em um ambiente virtual e ativado.

C:\User\Zé\Desktop\Projeto>

(venv) C:\User\Zé\Desktop\Projeto>

```

---

5º - Dentro do local que está o arquivo (requirements.txt), digite o comando conforme o exemplo abaixo e aguarde a instalação das bibliotecas e dependências.

```python

(venv) C:\User\Zé\Desktop\Projeto> pip install -r requirements.txt

```

---

6º - Após a finalização, digita o comando conforme o exemplo abaixo e verifique se as bibliotecas foram instaladas. Essa é uma etapa para validar a informação e caso o desenvolvedor queira realizar.

```python

(venv) C:\User\Zé\Desktop\Projeto> pip list

```

---

7º - Caso queira exportar uma lista de bibliotecas ou dependências do ambiente, utilize o comando abaixo e note a observação na descrição.

```python

# Notar que caso o arquivo já exista com certo nome no repositório que for realizar a exportação, então terá que alterar, conforme o exemplo abaixo.

(venv) C:\User\Zé\Desktop\Projeto> pip freeze > requirements_copia.txt

```
---

8º - Caso as biblitocas e dependências tenham sido instalada com sucesso, é só prosseguir com seu desenvolvimento em seu ambiente.

---

Fim do tutorial.

---

_Espero ajudar_ :smiley:
