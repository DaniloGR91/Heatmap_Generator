from mainwindow import Ui_MainWindow
from preview import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
import generator
import sys


class Heatmap_generator(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.dataset_opened = False

        self.label_status.setText(f'Escolha um arquivo')

        self.btn_preview.clicked.connect(self.preview)
        self.btn_open.clicked.connect(self.open_dataset)
        self.btn_salvar.clicked.connect(self.save_heatmap)

    def preview(self):
        if self.dataset_opened:
            self.set_config()
            preview = Preview(arquivo=self.filename, config=self.config)
            preview.exec_()
        else:
            self.label_status.setText(
                'Escolha um arquivo antes de solicitar o Preview')

    def save_heatmap(self):
        if self.dataset_opened:
            savefilename, _ = QFileDialog.getSaveFileName(self,
                                                          'Save Heatmap',
                                                          self.filename,
                                                          'Image files (*.jpg)')

            self.set_config()
            generator.heatmap(dataset=self.filename,
                              nome=savefilename,
                              title=self.config['title'],
                              tamanho=self.config['tamanho'],
                              color=self.config['color'],
                              corr_method=self.config['correlation_type'],
                              plot_corr=self.config['plotar_corr'])

            self.label_status.setText(savefilename)

        else:
            self.label_status.setText('Você deve abrir um data set.')

    def set_config(self):
        self.tamanho = str(self.comboBox_tamanho.currentText())
        self.color_pallete = str(self.comboBox_cor.currentText())
        self.correlation_type = str(
            self.comboBox_correlation_type.currentText())
        self.first_column_id = self.checkBox_ID_firstcolumn.isChecked()
        self.plotar_corr = self.checkBox_plotar_correalacao.isChecked()
        self.title = self.input_title.text()
        self.config = {
            'tamanho': self.tamanho,
            'color': self.color_pallete,
            'correlation_type': self.correlation_type,
            'first_column_id': self.first_column_id,
            'plotar_corr': self.plotar_corr,
            'title': self.title,
        }

    def open_dataset(self):
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  'Open Dataset',
                                                  os.path.expanduser(
                                                      '~/Documents'),
                                                  'Excel files (*.xls *.xlsx)')
        if filename != '':
            self.label_status.setText('Arquivo selecionado')
            self.filename = filename
            self.dataset_opened = True
            self.label_status.setText(
                f'Arquivo selecionado: \n{self.filename}')
        else:
            self.label_status.setText('Nenhum arquivo selecionado')


class Preview(Ui_Dialog, QDialog):
    def __init__(self, arquivo, config, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.arquivo = arquivo
        self.config = config

        generator.heatmap(dataset=self.arquivo,
                          nome='temp.jpg',
                          title=self.config['title'],
                          tamanho=self.config['tamanho'],
                          color=self.config['color'],
                          corr_method=self.config['correlation_type'],
                          plot_corr=self.config['plotar_corr'])

        imagem = QPixmap('temp.jpg').scaled(1024, 768, Qt.KeepAspectRatio)
        self.label_img.setPixmap(imagem)

    def closeEvent(self, event):
        os.remove('temp.jpg')


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    heatmap_generator = Heatmap_generator()
    heatmap_generator.show()
    qt.exec_()
