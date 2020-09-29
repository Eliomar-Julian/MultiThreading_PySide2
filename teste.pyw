from PySide2.QtCore import QThread, QObject, Signal, Qt
from PySide2.QtWidgets import QWidget, QApplication, QLabel, QGridLayout
from time import sleep

# // implementando os sinais que serão emitidos via thread
class Sinal(QObject):
    sinal_str = Signal(str)
    sinal_int = Signal(int)


# // classe de theading
class MyThread(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self)
        self.meu_sinal = Sinal()

    # // emitindo o sinal
    def run(self):
        self.lista = ['jose', 'maria', 'joao', 'leo']
        self.conta = self.inte = 0
        while True:
            sleep(1)
            self.meu_sinal.sinal_str.emit(str(self.lista[self.inte]))
            self.meu_sinal.sinal_int.emit(self.conta)
            self.inte += 1
            self.conta += 1
            if self.inte >= 4:
                self.inte = 0


# // aplicação principal
class MyApp:
    def __init__(self, parent=None):
        self.app = QApplication([])
        self.form = QWidget()
        self.form.resize(200,200)

        self.layout = QGridLayout(self.form)
        
        self.lb = QLabel()
        self.lb.setStyleSheet('font: 500 20pt "Arial"; color: red;')
        self.lb.resize(200, 20)
        self.lb.setAlignment(Qt.AlignCenter)

        self.lb2 = QLabel()
        self.lb2.setStyleSheet('font: 500 20pt "Arial"; color: blue;')
        self.lb2.resize(200, 20)
        self.lb2.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.lb)
        self.layout.addWidget(self.lb2)

        self.th = MyThread()
        self.th.start()
        self.th.meu_sinal.sinal_str.connect(self.teste)
        self.th.meu_sinal.sinal_int.connect(self.teste2)
    
    def teste(self, valor):
        self.lb.setText(str(valor))

    def teste2(self, valor):
        self.lb2.setText(str(valor))




if __name__ == '__main__':
    app = MyApp()
    app.form.show()
    app.app.exec_()