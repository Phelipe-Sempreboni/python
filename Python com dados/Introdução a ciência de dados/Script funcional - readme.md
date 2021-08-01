# Python para Ciência de Dados - Introducao a Ciência de Dados.

---

#### Abaixo temos um pouco de um dos cursos realizados de Python para Data Science, onde, o intuito é apresentar uma introdução ao data science com Python.

Nota: Os scripts foram executados pelo Jupyter Notebook.
Nota: O arquivo no GitHub (Introducao_a_data_science.ipynb) pode ser baixado e executado diretamente e completo no Jupyter Notebook.

---

Abaixo temos os scripts que podem ser executados no vscode, Jupyter, e outras plataformas.
Também temos o arquivo (logica_de_programacao.py) na extensão Python.

---

```

#A partir deste ponto os códigos podem ser copiados e executados em alguma plataforma de Python para leitura e execução.
#Nota: Os scripts foram executados pelo Jupyter Notebook.

#Script 1
#Nota: O arquivo utilizado para essa análise esta na pasta do GitHub e o nome é "ratings.csv". Utilize esse arquivo para seguir com as analises e insira no script 1.
import pandas as pd
notas = pd.read_csv(r"Insira o caminho que o arquivo estiver em seu computador")
notas.head()

#Script 2
notas.shape

#Script 3
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
notas.head()

#Script 4
notas['nota'].unique()

#Script 5
notas['nota'].value_counts()

#Script 6
print("Media", notas['nota'].mean())
print("Mediana", notas['nota'].median())

#Script 7
notas.nota

#Script 8
notas.nota.head()

#Script 9
notas.nota.plot()

#Script 10
notas.nota.plot(kind='hist')

#Script 11
notas.nota.describe()

#Script 12
import matplotlib.pyplot as plt
plt.figure(figsize=(5,8))

import seaborn as sns
sns.boxplot(y=notas.nota)

#Script 13
#Nota: O arquivo utilizado para essa análise esta na pasta do GitHub e o nome é "tmdb_5000_movies.csv". Utilize esse arquivo para seguir com as analises e insira no script 13.
filmes = pd.read_csv(r"Insira o caminho que o arquivo estiver em seu computador")
filmes.head()

#Script 14
notas.head()

#Script 15
#Analisando algumas notas especificas por filmes.
notas.query("filmeId==1").nota.mean()

#Script 16
notas.query("filmeId==2").nota.mean()

#Script 17
media_por_filme = notas.groupby("filmeId").mean().nota

#Script 18
media_por_filme.head()

#Script 19
media_por_filme.plot(kind = 'hist')

#Script 20
sns.boxplot(media_por_filme)

#Script 21
media_por_filme.describe()

#Script 22
sns.distplot(media_por_filme)

#Script 23
import matplotlib.pyplot as plt
plt.hist(media_por_filme)
plt.title("Histograma das médias dos filmes")

#Script 24
#Nota: O arquivo utilizado para essa análise esta na pasta do GitHub e o nome é "tmdb_5000_movies.csv". Utilize esse arquivo para seguir com as analises e insira no script 24.
tmdb = pd.read_csv(r"Insira o caminho que o arquivo estiver em seu computador")
tmdb.head()

#Script 25
#categorica nominal
tmdb.original_language.unique() 

#Script 26
tmdb.original_language.value_counts().index

#Script 27
tmdb.original_language.value_counts().values

#Script 28
tmdb.original_language.value_counts()

#Script 29
tmdb.original_language.value_counts().to_frame()

#Script 30
contagem_de_lingua = tmdb.original_language.value_counts().to_frame().reset_index()
contagem_de_lingua.columns = ["original_language", "total"]
contagem_de_lingua.head()

#Script 31
sns.barplot(x="original_language", y="total", data = contagem_de_lingua)

#Script 32
sns.catplot(x="original_language", kind = "count", data = tmdb)

#Script 33
print(sns.__version__)
print(pd.__version__)

#Script 34
plt.pie(contagem_de_lingua["total"], labels = contagem_de_lingua["original_language"])

#Script 35
total_por_lingua = tmdb["original_language"].value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc["en"]
total_do_resto = total_geral - total_de_ingles
print(total_de_ingles, total_do_resto)

#Script 36
dados = {
    'lingua': ['ingles', 'outros'],
    'total': [total_de_ingles, total_do_resto]
}
dados = pd.DataFrame(dados)
sns.barplot(x = "lingua", y="total",data = dados)

#Script 37
plt.pie(dados["total"], labels = dados["lingua"])

#Script 38
total_por_lingua_de_outros_filmes = tmdb.query("original_language != 'en'").original_language.value_counts()
total_por_lingua_de_outros_filmes

#Script 39
filmes_sem_lingua_original_em_ingles = tmdb.query("original_language != 'en'")

sns.catplot(x = "original_language", kind = "count", 
            data = filmes_sem_lingua_original_em_ingles,
            aspect = 2,
            palette = "GnBu_d",
            order = total_por_lingua_de_outros_filmes.index)

#Script 40
import seaborn as sns
sns.set(style="ticks")

# Load the example dataset for Anscombe's quartet
df = sns.load_dataset("anscombe")

# Show the results of a linear regression within each dataset
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=None, palette="muted", height=4,
           scatter_kws={"s": 50, "alpha": 1})

#Script 41
#Nota: O arquivo utilizado para essa análise esta na pasta do GitHub e o nome é "movies.csv". Utilize esse arquivo para seguir com as analises e insira no script 41.
filmes_aula1 = pd.read_csv(r"Insira o caminho que o arquivo estiver em seu computador")
filmes_aula1

#Script 42
filmes_aula1.columns = ["filmeId", "titulo", "genero"]
filmes_aula1

#Script 43
filmes_aula1.head(2)

#Script 44
notas_do_toy_story = notas.query("filmeId == 1")
notas_do_jumanji = notas.query("filmeId == 2")

print(len(notas_do_toy_story), len(notas_do_jumanji))


#Script 45
print("Nota mediana do Toy Story %.2f" % notas_do_toy_story.nota.median())
print("Nota mediana do Toy Story %.2f" % notas_do_jumanji.nota.median())

#Script 46
import numpy as np
filme1 = np.append(np.array([2.5] * 10 ),np.array([3.5] * 10 ))
filme2 = np.append(np.array([5] * 10), np.array([1] * 10))

#Script 47
print(filme1.mean(), filme2.mean())
print(np.median(filme1), np.median(filme2))
print(np.std(filme1), np.std(filme2))

#Script 48
sns.distplot(filme1)
sns.distplot(filme2)

#Script 49
plt.hist(filme1)
plt.hist(filme2)

#Script 50
sns.boxplot(filme1)

#Script 51
plt.boxplot([filme1, filme2])

#Script 52
sns.boxplot(notas_do_toy_story.nota)
sns.boxplot(notas_do_jumanji.nota)

#Script 53
plt.boxplot([notas_do_toy_story.nota, notas_do_jumanji.nota])

#Script 54
sns.boxplot(x = "filmeId", y ="nota", data = notas.query("filmeId in [1,2,3,4,5]"))

#Script 55
print(notas_do_toy_story.nota.std())
print(notas_do_jumanji.nota.std())

#Script 56
print(np.std(filme1), np.std(filme2))

print(f'Projeto finalizado com sucesso')