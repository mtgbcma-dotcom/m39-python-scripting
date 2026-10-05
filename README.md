# Exercício — Python: Scripting

Projeto desenvolvido para o exercício da EBAC sobre scripts Python.

## Objetivos

1. Extrair a taxa CDI da API do Banco Central.
2. Salvar dez registros no arquivo `taxa-cdi.csv`.
3. Gerar um gráfico de linha a partir dos dados.
4. Combinar extração e visualização no arquivo `analise.py`.

## Arquivos

- `extracao.py`: consulta a API e gera o CSV.
- `visualizacao.py`: lê o CSV e gera um gráfico PNG.
- `analise.py`: combina os dois processos.
- `requirements.txt`: dependências do projeto.
- `Profissao_Analista_de_dados_M9_Exercicio_PREENCHIDO.ipynb`: notebook com a resposta da atividade.

## Instalação

```bash
pip install -r requirements.txt
```

## Execução da extração

```bash
python extracao.py
```

Resultado esperado:

```text
taxa-cdi.csv
```

## Execução da visualização

```bash
python visualizacao.py grafico-cdi
```

Resultado esperado:

```text
grafico-cdi.png
```

## Execução da análise completa

```bash
python analise.py grafico-cdi
```

Resultados esperados:

```text
taxa-cdi.csv
grafico-cdi.png
```

O nome `grafico-cdi` pode ser substituído por outro nome desejado.
