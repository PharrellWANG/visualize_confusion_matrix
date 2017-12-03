import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os


def visu_confusion_matrix(file_name, folder, target_format, num_classes):

    df = pd.read_csv(file_name, sep=',', header=None)
    df_cm = pd.DataFrame(df.values, index=list(range(0, num_classes)),
                         columns=list(range(0, num_classes)))
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_cm, annot=False, cmap=sns.color_palette("Blues"))

    svg_basename = os.path.basename(file_name)
    svg_basename_new = os.path.splitext(svg_basename)[0] + '.' + target_format
    svg_full_path = os.path.join(folder, svg_basename_new)

    plt.savefig(svg_full_path, format=target_format, dpi=1200)
    print('Success! ' + file_name + ' has been visualized to ' + svg_full_path)


if __name__ == "__main__":
    # visu_confusion_matrix('csv/ckpt-10342.csv')
    # visu_confusion_matrix('csv/ckpt-10342.csv')
    # visu_confusion_matrix('csv/ckpt-10342.csv')
    # visu_confusion_matrix('csv/ckpt-10342.csv')
    # visu_confusion_matrix('csv/ckpt-10342.csv')
    # visu_confusion_matrix('csv/ckpt-10342.csv')
    file_names = [
        # 'csv/ckpt-10342.csv',
        # 'csv/ckpt-20622.csv',
        # 'csv/ckpt-30757.csv',
        # 'csv/ckpt-40884.csv',
        # 'csv/ckpt-51009.csv',
        # 'csv/ckpt-61168.csv',
        'csv/08-kpt-133049.csv',
        'csv/16-kpt-304857.csv'
    ]
    for name in file_names:
        visu_confusion_matrix(file_name=name,
                              folder='figures',
                              target_format='eps',
                              num_classes=32,
                              )
