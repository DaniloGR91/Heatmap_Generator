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
    fig_size = set_size(tamanho)[0]
    title_size = set_size(tamanho)[1]
    label_size = set_size(tamanho)[2]
    corr_method = corr_method.lower()
    color_map = set_colormap(color)

    plt.figure(figsize=fig_size)
    sns.set(font_scale=label_size)
    sns.heatmap(df.corr(method=corr_method).round(3),
                cmap=color_map, annot=plot_corr)
    plt.title(title, fontdict={'family': 'sans',
                               'size': title_size, 'weight': 'bold'})
    return plt.savefig(nome, dpi=600, bbox_inches='tight', pad_inches=0.2)


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
        return (9, 6), 15, 1
    elif tamanho == 'Médio':
        return (12, 8), 20, 1.3
    elif tamanho == 'Grande':
        return (21, 14), 35, 2.3
