#!/usr/bin/env python
# coding: utf-8

# # Tarefa 01
# 
# - Leia os enunciados com atenção
# - Saiba que pode haver mais de uma resposta correta
# - Insira novas células de código sempre que achar necessário
# - Em caso de dúvidas, procure os tutores
# - Divirta-se :)

# ### 01 - Teste de gravidez
# Escreva uma célula com controle de fluxos que tem como premissa a existência das seguintes variáveis:
# 
# - ```sexo``` como ```str``` indicando os valores '**M**' para masculino e '**F**' para feminino  
# - ```beta_hcg``` que indica a quantidade do beta-HCG no sangue em mUI/mL.
# 
# A sua tarefa é escrever um código que imprima como resultado "indivíduo do sexo masculino" quando sexo = 'M', caso sexo = 'F', se o valor de beta-HCG for maior que 5, retorne "Positivo" indicando que a paciente está grávida, e retorne "Negativo" caso contrário.
# 
# Não mexa nos valores da variável ```sexo``` nem em ```beta_hcg```, e escreva um código que funcione para quaisquer valores possíveis de ambos: ```sexo``` = '**M**' ou '**F**' e ```beta_hcg``` assumindo valores inteiros positivos.

# In[27]:


sexo = 'M'
beta_hcg = 0

# seu código vem abaixo desta linha

sexo = sexo.upper()
if sexo == "M":
    print('indivíduo do sexo masculino')
elif sexo == "F" and beta_hcg > 5:
    print("Positivo")
else:
    print("Negativo")


# ### 02 - Renomeando variáveis
# 
# Vamos ver adiante que uma forma de renomear variáveis de um conjunto de dados é através de dicionários - o dicionário deve conter como chave o nome original, associando a cada chave um único valor (tipo *str*) que contenha o nome novo.
# 
# A sua tarefa é escrever um dicionário que possa ser utilizado para traduzir as variáveis ```name``` (nome), ```age``` (idade) e ```income``` (renda). Ou seja, esse dicionário deve relacionar as chaves *name, age* e *income* às suas respectivas traduções.

# In[32]:


dic_renomeacao = {'name': 'nome', 'age': 'idade', 'income': 'renda'}
dic_renomeacao


# ### 03 - É divisível?
# A sua tarefa é escrever um código que indique se um número ```N``` é divisível por um número P. Escreva um programa que faça essa verificação para quaisquer combinações de ```N``` e ```M``` e devolva uma mensagem indicativa no output.

# In[41]:


N = 42
M = 7

#Seu código

# Função para verificar se N é divisível por M
def verifica_divisibilidade(N, M):
    if N % M == 0:
        return f"{N} é divisível por {M}."
    else:
        return f"{N} não é divisível por {M}."

# Usando os valores dados
N = 42
M = 7
resultado = verifica_divisibilidade(N, M)
print(resultado)


# ### 04 - Números primos
# > Um número **N** é primo se e somente se é divisível por 1, -1, por **N** e por -**N**.  
# 
# Escreva um script que verifica se ```N``` é um número primo, verificando se ```N``` é divisível por todos os números de ```1``` a ```N-1```. Você vai precisar usar alguma ferramenta de *loop* que você aprendeu para isto. No final, devolva uma mensagem no output indicando se o número é primo ou não.

# In[43]:


N = 47

# seu código abaixo

def verifica_primalidade(N):
    # Caso especial para 1, que não é primo
    if N == 1:
        return f"{N} não é um número primo."

    # Loop para verificar divisibilidade por números de 2 até N-1
    for i in range(2, N):
        if N % i == 0:
            return f"{N} não é um número primo, pois é divisível por {i}."

    # Se não foi encontrado nenhum divisor, então é primo
    return f"{N} é um número primo."

# Exemplo de uso
numero_N = 47
resultado = verifica_primalidade(numero_N)
print(resultado)


# ### 05 - Desafio
# O algorítmo do exercício anterior não é o mais eficiente. O que você pode fazer para deixá-lo mais eficiente? Ou seja, executar menos comparações, portanto consumir menos tempo.
# 1. Será que precisamos correr o loop até o final sempre?
# 2. Será que precisamos mesmo verificar **todos** os números?
# 3. Será que precisamos ir até N-1?
# 
# Essas perguntas levam ao tipo de pensamento voltado a deixar um algoritmo mais eficiente. Veja se você consegue melhorar o seu.

# In[44]:


N = 98

# seu código aqui

import math

def verifica_primalidade_otimizado(N):
    # Caso especial para 1, que não é primo
    if N == 1:
        return f"{N} não é um número primo."

    # Caso especial para 2, que é primo
    if N == 2:
        return f"{N} é um número primo."

    # Se N for par (exceto 2), não é primo
    if N % 2 == 0:
        return f"{N} não é um número primo, pois é divisível por 2."

    # Loop para verificar divisibilidade por números ímpares até a raiz quadrada de N
    limite = int(math.sqrt(N)) + 1
    for i in range(3, limite, 2):
        if N % i == 0:
            return f"{N} não é um número primo, pois é divisível por {i}."

    # Se não foi encontrado nenhum divisor, então é primo
    return f"{N} é um número primo."

# Exemplo de uso
numero_N = 98
resultado = verifica_primalidade_otimizado(numero_N)
print(resultado)



# ### 06 - Peso ideal 1
# O IMC (índice de massa corpórea) é um indicador de saúde mais bem aceito que o peso. Ele é calculado como:
# 
# $$ IMC = \dfrac{peso}{altura^2}$$
# 
# Segundo a OMS, valores *normais* são entre 18.5 e 24.9.
# 
# Sua tarefa é encontrar o ponto médio dessa faixa.

# In[46]:


# Valores extremos da faixa normal do IMC
valor_minimo_imc = 18.5
valor_maximo_imc = 24.9

# Calcula o ponto médio
ponto_medio_imc = (valor_minimo_imc + valor_maximo_imc) / 2

# Imprime o resultado
print(f"O ponto médio da faixa normal do IMC é: {ponto_medio_imc}")


# ### 07 - Peso ideal 2
# Recebendo um valor de altura, encontre o peso '*ideal*' dessa pessoa, que fornece o IMC encontrado acima

# In[48]:


altura = 1.70

# Seu código

# Ponto médio da faixa normal do IMC
ponto_medio_imc = (18.5 + 24.9) / 2

# Calcula o peso "ideal" usando a fórmula do IMC
peso_ideal = ponto_medio_imc * altura**2

# Imprime o resultado
print(f"O peso 'ideal' para uma altura de {altura} m é aproximadamente {peso_ideal:.2f} kg.")


# ### 08 - Peso ideal 3
# Dada uma lista contendo as alturas de pacientes, crie uma nova lista que contenha o peso '*ideal*' (que fornece o IMC calculado em **Peso ideal 1**) desses pacientes.

# In[50]:


lista_alturas = [1.95, 2.05, 1.70, 1.65]

lista_peso_ideal = []

# seu código
def calcular_peso_ideal(altura):
    # Ponto médio da faixa normal do IMC
    ponto_medio_imc = (18.5 + 24.9) / 2 
    
# Calcula o peso "ideal" usando a fórmula do IMC
    peso_ideal = ponto_medio_imc * altura**2
    
    return peso_ideal

# Lista de alturas dos pacientes
lista_alturas = [1.95, 2.05, 1.70, 1.65]

# Lista para armazenar os pesos "ideais"
lista_peso_ideal = []

# Calcula o peso "ideal" para cada altura na lista
for altura in lista_alturas:
    peso_ideal = calcular_peso_ideal(altura)
    lista_peso_ideal.append(peso_ideal)

# Imprime a lista de pesos "ideais"
print("Lista de pesos 'ideais':", lista_peso_ideal)


# ### 09 - Peso ideal 4
# Dada uma lista de tuplas - cada elemento da lista é uma tupla contendo altura e peso de um paciente - crie uma nova lista com o IMC desses pacientes.

# In[51]:


altura_peso = [(1.80, 90), (1.65, 75), (1.91, 70)]

imc = []

# seu código

# Função para calcular o IMC
def calcular_imc(altura, peso):
    return peso / altura**2

# Calcula o IMC para cada par (altura, peso) na lista
for altura, peso in altura_peso:
    imc_atual = calcular_imc(altura, peso)
    imc.append(imc_atual)

# Imprime a lista de IMC
print("Lista de IMC:", imc)


# ### 10 - Peso ideal 5
# Dada uma lista de **listas** - cada elemento da lista é uma **lista** contendo altura e peso de um paciente, adicione mais um elemento à lista de cada paciente contendo o IMC do paciente. Verifique também se é 'baixo', 'normal' ou 'alto' segundo os padrões da OMS em que normal é entre 18.5 e 24.9.
# 
# Reflexão: por que no problema anterior temos que criar uma nova lista, e não podemos adicionar os dados de cada indivíduo à tupla?

# In[53]:


altura_peso = [[1.80, 90], [1.65, 75], [1.91, 70]]

# seu código

# Função para calcular o IMC
def calcular_imc(altura, peso):
    return peso / altura**2

# Itera sobre a lista de listas
for paciente in altura_peso:
    altura, peso = paciente[0], paciente[1]
    
    # Calcula o IMC
    imc = calcular_imc(altura, peso)
    
    # Adiciona o IMC à lista do paciente
    paciente.append(imc)
    
    # Verifica se o IMC é 'baixo', 'normal' ou 'alto'
    if 18.5 <= imc <= 24.9:
        classificacao = 'normal'
    elif imc < 18.5:
        classificacao = 'baixo'
    else:
        classificacao = 'alto'
    
    # Adiciona a classificação à lista do paciente
    paciente.append(classificacao)

# Imprime a lista de listas atualizada
print("Lista de listas com IMC e classificação:")
for paciente in altura_peso:
    print(paciente)


# In[ ]:




