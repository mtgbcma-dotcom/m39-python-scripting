import os
import time
import json
from random import random
from datetime import datetime
from sys import argv

import pandas as pd
import requests
import seaborn as sns


URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'


def extrair_taxa_cdi():
    """Consulta a taxa CDI mais recente no Banco Central do Brasil."""
    try:
        response = requests.get(url=URL, timeout=30)
        response.raise_for_status()
    except requests.HTTPError as exc:
        print('Dado não encontrado, continuando.')
        raise exc
    except Exception as exc:
        print('Erro, parando a execução.')
        raise exc
    else:
        dado = json.loads(response.text)[-1]['valor']
        return float(dado)


def gerar_base_de_dados(cdi_base):
    """Cria dez registros de CDI e salva em taxa-cdi.csv."""
    for _ in range(10):
        data_e_hora = datetime.now()
        data = datetime.strftime(
            data_e_hora,
            '%Y/%m/%d'
        )
        hora = datetime.strftime(
            data_e_hora,
            '%H:%M:%S'
        )

        cdi = cdi_base + (random() - 0.5)

        if not os.path.exists('./taxa-cdi.csv'):
            with open(
                file='./taxa-cdi.csv',
                mode='w',
                encoding='utf8'
            ) as fp:
                fp.write('data,hora,taxa\n')

        with open(
            file='./taxa-cdi.csv',
            mode='a',
            encoding='utf8'
        ) as fp:
            fp.write(
                f'{data},{hora},{cdi}\n'
            )

        time.sleep(1)


def gerar_grafico(nome_grafico):
    """Gera um gráfico de linha a partir do arquivo taxa-cdi.csv."""
    df = pd.read_csv('./taxa-cdi.csv')

    grafico = sns.lineplot(
        x=df['hora'],
        y=df['taxa']
    )

    grafico.set_xticklabels(
        labels=df['hora'],
        rotation=90
    )

    figura = grafico.get_figure()
    figura.tight_layout()
    figura.savefig(
        f'{nome_grafico}.png'
    )


def main():
    """Executa a extração, geração do CSV e criação do gráfico."""
    if len(argv) < 2:
        raise SystemExit(
            'Uso: python analise.py <nome-do-grafico>'
        )

    nome_grafico = argv[1]

    cdi_base = extrair_taxa_cdi()
    gerar_base_de_dados(cdi_base)
    gerar_grafico(nome_grafico)

    print('Sucesso')


if __name__ == '__main__':
    main()
