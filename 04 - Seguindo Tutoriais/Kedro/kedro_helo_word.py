# Importações
from kedro.io import DataCatalog, MemoryDataSet
from kedro.pipeline import node, Pipeline
from kedro.runner import SequentialRunner

# criando o catálogo de Dados
catalago_dados = DataCatalog({"dados_exemplo": MemoryDataSet()})

# Nó nº 1
def saudacao_de_retorno():
    return "Olá"

noh_saudacao_de_retorno = node(saudacao_de_retorno, inputs=None, outputs='minha_saudacao')

# Nó nº 2
def juntar_declaracao(saudacao):
    return f'{saudacao} meu amigo Kedro!'

noh_juntar_declaracao = node(juntar_declaracao, inputs='minha_saudacao', outputs='minha_mensagem')

# inbserindo nós ao pipeline
pipeline = Pipeline([noh_saudacao_de_retorno, noh_juntar_declaracao])

# Criando o runer para rodar o pipeline
runner = SequentialRunner()

# Rodar o Pipeline
print(runner.run(pipeline, catalago_dados))

