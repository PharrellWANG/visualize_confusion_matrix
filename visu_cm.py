import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os


def visu_confusion_matrix(file_name, folder_to_save_svg):

    df = pd.read_csv(file_name, sep=',', header=None)
    df_cm = pd.DataFrame(df.values, index=list(range(0, 37)),
                         columns=list(range(0, 37)))
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_cm, annot=True, cmap=sns.color_palette("Greens"))

    svg_basename = os.path.basename(file_name)
    svg_basename_new = os.path.splitext(svg_basename)[0] + '.svg'
    svg_full_path = os.path.join(folder_to_save_svg, svg_basename_new)

    plt.savefig(svg_full_path, format='svg', dpi=1200)
    print('Success! ' + file_name + ' has been visualized to ' + svg_full_path)


if __name__ == "__main__":
    # visu_confusion_matrix('csv/ckpt-10342.csv')
    # visu_confusion_matrix('csv/ckpt-10342.csv')
    # visu_confusion_matrix('csv/ckpt-10342.csv')
    # visu_confusion_matrix('csv/ckpt-10342.csv')
    # visu_confusion_matrix('csv/ckpt-10342.csv')
    # visu_confusion_matrix('csv/ckpt-10342.csv')
    file_names = [
        'csv/ckpt-10342.csv',
        'csv/ckpt-20622.csv',
        'csv/ckpt-30757.csv',
        'csv/ckpt-40884.csv',
        'csv/ckpt-51009.csv',
        'csv/ckpt-61168.csv',
    ]
    for name in file_names:
        visu_confusion_matrix(file_name=name, folder_to_save_svg='figures')