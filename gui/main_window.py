import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout

from pdf import pdf_scraper
from web import web_scraper


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        tokenize_local_button = QPushButton('Tokenizar PDFs locais', self)
        tokenize_local_button.clicked.connect(self.tokenize_local)

        search_web_button = QPushButton('Pesquisar na web', self)
        search_web_button.clicked.connect(self.search_web)

        vbox = QVBoxLayout()
        vbox.addWidget(tokenize_local_button)
        vbox.addWidget(search_web_button)

        self.setLayout(vbox)
        self.setWindowTitle('Tokenizador de dados')
        self.show()

    from pdf import pdf_scraper

    def tokenize_local(self):
        pdf_scraper.tokenize_pdfs()

    from web import web_scraper

    def search_web(self):
        web_scraper.search_web()

    def mainloop(self):
        pass


app = QApplication(sys.argv)
main_window = MainWindow()
sys.exit(app.exec_())
