import os
import time
import json
from random import random
from datetime import datetime

import requests


URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'


def extrair_taxa_cdi():
    """Consulta a taxa CDI no Banco Central do Brasil."""
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


def salvar_dados(cdi_base):
    """Gera dez registros e salva em taxa-cdi.csv."""
    for _ in range(10):
        data_e_hora = datetime.now()
        data = datetime.strftime(data_e_hora, '%Y/%m/%d')
        hora = datetime.strftime(data_e_hora, '%H:%M:%S')

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
            fp.write(f'{data},{hora},{cdi}\n')

        time.sleep(1)


if __name__ == '__main__':
    taxa_cdi = extrair_taxa_cdi()
    salvar_dados(taxa_cdi)
    print('Sucesso')
