import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def heatmap(dataset,
            nome,
            title=None,
            tamanho='Médio',
            color='Vermelho',
            corr_method='Pearson',
            plot_corr=False, *args, **kwargs):

    df = pd.read_excel(dataset)
    fig_size = set_size(tamanho)
    corr_method = corr_method.lower()
    color_map = set_colormap(color)

    plt.figure(figsize=fig_size)
    sns.heatmap(df.corr(method=corr_method).round(3),
                cmap=color_map, annot=plot_corr)
    plt.title(title, fontdict={'family': 'sans', 'size': 20, 'weight': 'bold'})
    return plt.savefig(nome)


def set_colormap(color):
    if color == 'Cinza':
        return 'Greys'
    elif color == 'Roxo':
        return 'Purples'
    elif color == 'Laranja':
        return 'Oranges'
    elif color == 'Azul':
        return 'Blues'
    elif color == 'Verde':
        return 'Greens'
    elif color == 'Vermelho':
        return 'Reds'


def set_size(tamanho):
    if tamanho == 'Pequeno':
        return (9, 6)
    elif tamanho == 'Médio':
        return (12, 8)
    elif tamanho == 'Grande':
        return (21, 14)
