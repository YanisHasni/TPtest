import sys
import socket
import threading
from PyQt5.QtWidgets import *

#Pour lance le serveur il faut se mettre dans le répertoir dans le terminal
#et faire la commande python avec le nom du fichier

#

class ServerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.setWindowTitle("Serveur de Chat")
        self.server_socket = None
        self.is_running = False
        self.clients = []
        self.label_address = QLabel("Serveur :")
        self.input_address = QLineEdit("localhost")
        self.label_port = QLabel("Port :")
        self.input_port = QLineEdit("4200")
        self.label_max = QLabel("Nombre de clients maximum")
        self.input_max = QLineEdit("5")
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.button_start = QPushButton("Démarrer le serveur")
        self.button_start.clicked.connect(self.__demarrage)
        grid.addWidget(self.label_address, 0, 0)
        grid.addWidget(self.input_address, 0, 2)
        grid.addWidget(self.label_port, 1, 0)
        grid.addWidget(self.input_port, 1, 2)
        grid.addWidget(self.label_max, 2, 0)
        grid.addWidget(self.input_max, 2, 2)
        grid.addWidget(self.button_start, 3 , 0)
        grid.addWidget(self.log, 3, 2)

    def __demarrage(self):
        if self.is_running:
            self.stop_server()
        else:
            self.start_server()



    def __accept(self):
        server_socket = socket.socket()
        server_socket.bind(('localhost', 4000))
        server_socket.listen(5)
        print("Serveur en attente de connexions...")

    def log_message(self, message):
        self.log.append(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ServerApp()
    window.show()
    app.exec()
