---

## Expressões Lambda

---

- [x] Neste repositório falaremos e utilizaremos exemplos de _expressões e/ou funções anônimas_, conhecida como _funções lambda_.

---

- [x] Um pouco sobre _lambda_:

Uma das características mais úteis em Python, onde talvez para iniciantes fique um pouco confuso, é a _expressão lambda_.

_Expressões lambda_ nos pemirtem criar funções anônimas. Isto siginifica que podemos fazer rapidamente funções ad-hoc sem a necessidade de definir uma função usando a palavra reservada _def_.

Objetos de função desenvolvidos executando _expressões lambda_ funcionam exatamente da mesma forma como aqueles criados atribuídos pela palavra reservada _def_. Mas há algumas diferenças fundamentais que fazem _lambda_ útil em funções especializadas:

- O corpo do lambda é uma única expressão, não um bloco de instruções como um criado com a palavra reservada _def_.
- O corpo do lambda é semelhante a uma instrução de retorno (return) do corpo _def_.

---

_Expressões lambda_ realmente são úteis quando usadas em conjunto comas funções _map()_, _filter()_ e _reduce()_.

---

Expressões lambda são usadas para criar funções simples.

São também funções _in-line_ ou apenas _funções anônimas_.

---

Exemplo:

```Python

# Uma função criada com def para calcular a potência de um numero elevado à 2.

def potencia(num):
  resultado = num ** 2
  return resultado
  
print(potencia(5))

Resultado: 25

```

```Python

# Uma função criada com expressão e/ou função anônima e/ou função lambda para calcula a potência de um número elevado à 2.

potencia = lambda num: num ** 2

print(potencia(5))

```

Notar acima que temos a mesma função, porém uma escrita com uma função declarada com _def_ e uma com _função lambda_.

---









