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

7º - Caso as biblitocas e dependências tenham sido instalada com sucesso, é só prosseguir com seu desenvolvimento em seu ambiente.

---

Fim do tutorial.

---

_Espero ajudar_ :smiley:
