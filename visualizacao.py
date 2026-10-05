from sys import argv

import pandas as pd
import seaborn as sns


def gerar_grafico(nome_grafico):
    """Lê taxa-cdi.csv e gera um gráfico em formato PNG."""
    df = pd.read_csv('./taxa-cdi.csv')

    grafico = sns.lineplot(
        x=df['hora'],
        y=df['taxa']
    )

    grafico.set_xticklabels(
        labels=df['hora'],
        rotation=90
    )

    grafico.get_figure().tight_layout()
    grafico.get_figure().savefig(
        f'{nome_grafico}.png'
    )


if __name__ == '__main__':
    if len(argv) < 2:
        raise SystemExit(
            'Uso: python visualizacao.py <nome-do-grafico>'
        )

    gerar_grafico(argv[1])
    print('Gráfico gerado com sucesso')
