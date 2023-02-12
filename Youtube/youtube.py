import sys
from Video_downloader import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        super().__init__()

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        # QMessageBox oluşturuldu ve text uzunluğuna göre uyarı yapıldı.
        self.message = QMessageBox()

        # Youtube icon.
        self.resim = QLabel()
        self.resim.setPixmap(QPixmap("resim1.png"))
        self.resim.setAlignment(Qt.AlignCenter)

        # Başlık yazısı.
        self.label = QLabel("Video URL' sini Giriniz")
        self.label.setFont(QFont("Times New Roman", 14))
        self.label.setStyleSheet("color: White")
        self.label.setAlignment(Qt.AlignCenter)

        # Text alanı.
        self.line = QLineEdit()
        self.line.setPlaceholderText("Link'i buraya yapıştırınız..")
        self.line.setStyleSheet("QLineEdit {Background-color: White;"
                                " color: Blue; "
                                "font: Bold;"
                                "selection-color: yellow}")     # Seçilen yazının rengini değiştirir.
        self.line.setFixedSize(300, 30)

        # Butonlar.
        self.indir = QPushButton("İndir")
        self.indir.setStyleSheet("QPushButton {Background-color: White}")
        self.temizle = QPushButton("Temizle")
        self.temizle.setStyleSheet("QPushButton {Background-color: White}")

        # Widget yerleştirme.
        vbox.addStretch()
        vbox.addWidget(self.resim)
        vbox.addWidget(self.label)
        vbox.addWidget(self.line)
        vbox.addWidget(self.indir)
        vbox.addWidget(self.temizle)
        vbox.addStretch()

        hbox.addStretch()
        hbox.addLayout(vbox)
        hbox.addStretch()

        # Layoutları pencere üzerine ekleme.
        self.setLayout(hbox)

    # fonksiyonlar
    def click_1(self):
        yazi = self.line.text()
        if len(yazi) == 0:

            self.message.setWindowTitle("Uyarı Mesajı")
            self.message.setWindowIcon(QIcon("Resim1.png"))
            self.message.setIcon(QMessageBox.Warning)
            self.message.setText("Lütfen Link'i giriniz!")
            self.message.setStyleSheet("color: Blue")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()

        else:
            downloader(yazi)
            sys.exit()

    def click_2(self):
        self.line.clear()


class Youtube(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win = Window()
        self.setCentralWidget(self.win)
        self.attributes()

    def attributes(self):

        self.win.indir.clicked.connect(self.win.click_1)
        self.win.temizle.clicked.connect(self.win.click_2)

        # Pencere özellikleri
        self.setGeometry(1200, 250, 600, 400)
        self.setFixedSize(600, 400)
        self.setStyleSheet("Background-color: Black;")
        self.setWindowTitle("Youtube Downloader")
        self.setWindowIcon(QIcon("youtube_icon.png"))
        self.show()


app = QApplication(sys.argv)
you = Youtube()
sys.exit(app.exec())
