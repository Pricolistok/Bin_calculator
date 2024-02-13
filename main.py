import sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from logic import work_with_row


class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.answer = ''
        self.window = QWidget()
        toolbar = QToolBar()
        self.addToolbar(toolbar)
        self.window.setWindowTitle('NEW')

        self.grid = QGridLayout(self.window)

        self.row_for_calc = ''

        self.row_input = QLineEdit()
        self.grid.addWidget(self.row_input, 1, 0, 1, 4)

        self.btn_0 = QPushButton('0')
        self.grid.addWidget(self.btn_0, 5, 0, 5, 2, alignment=Qt.AlignTop)
        self.btn_0.clicked.connect(lambda: self.create_row('0'))

        self.btn_1 = QPushButton('1')
        self.grid.addWidget(self.btn_1, 2, 0)
        self.btn_1.clicked.connect(lambda: self.create_row('1'))

        self.btn_2 = QPushButton('2')
        self.grid.addWidget(self.btn_2, 2, 1)
        self.btn_2.clicked.connect(lambda: self.create_row('2'))

        self.btn_3 = QPushButton('3')
        self.grid.addWidget(self.btn_3, 2, 2)
        self.btn_3.clicked.connect(lambda: self.create_row('3'))

        self.btn_4 = QPushButton('4')
        self.grid.addWidget(self.btn_4, 3, 0)
        self.btn_4.clicked.connect(lambda: self.create_row('4'))

        self.btn_5 = QPushButton('5')
        self.grid.addWidget(self.btn_5, 3, 1)
        self.btn_5.clicked.connect(lambda: self.create_row('5'))

        self.btn_6 = QPushButton('6')
        self.grid.addWidget(self.btn_6, 3, 2)
        self.btn_6.clicked.connect(lambda: self.create_row('6'))

        self.btn_7 = QPushButton('7')
        self.grid.addWidget(self.btn_7, 4, 0)
        self.btn_7.clicked.connect(lambda: self.create_row('7'))

        self.btn_8 = QPushButton('8')
        self.grid.addWidget(self.btn_8, 4, 1)
        self.btn_8.clicked.connect(lambda: self.create_row('8'))

        self.btn_9 = QPushButton('9')
        self.grid.addWidget(self.btn_9, 4, 2)
        self.btn_9.clicked.connect(lambda: self.create_row('9'))

        self.btn_dot = QPushButton('.')
        self.grid.addWidget(self.btn_dot, 5, 2)
        self.btn_dot.clicked.connect(lambda: self.create_row('.'))

        self.btn_enter = QPushButton('Enter')
        self.grid.addWidget(self.btn_enter, 6, 1, 6, 2, alignment=Qt.AlignTop)
        self.btn_enter.clicked.connect(self.enter)

        self.btn_plus = QPushButton('+')
        self.grid.addWidget(self.btn_plus, 2, 3)
        self.btn_plus.clicked.connect(lambda: self.create_row('+'))

        self.btn_minus = QPushButton('-')
        self.grid.addWidget(self.btn_minus, 3, 3)
        self.btn_minus.clicked.connect(lambda: self.create_row('-'))

        self.btn_ac = QPushButton('*')
        self.grid.addWidget(self.btn_ac, 4, 3)
        self.btn_ac.clicked.connect(lambda: self.create_row('*'))

        self.btn_ac = QPushButton('AC')
        self.grid.addWidget(self.btn_ac, 5, 3)
        self.btn_ac.clicked.connect(lambda: self.clean_row())

        self.btn_delete = QPushButton('<=')
        self.grid.addWidget(self.btn_delete, 6, 3)
        self.btn_delete.clicked.connect(lambda: self.delete_last())
        self.window.show()

    def enter(self):
        from_line = self.row_input.text()
        try:
            if self.row_for_calc != from_line:
                self.answer = work_with_row(from_line)
            else:
                if self.row_for_calc == '':
                    self.answer = 'Error'
                    self.row_for_calc = ''
                else:
                    self.answer = work_with_row(self.row_for_calc)
        except ValueError:
            self.answer = 'Error'
            self.row_for_calc = ''
        self.row_input.setText(self.answer)

    def create_row(self, elem):
        self.row_for_calc = self.row_input.text() + elem
        self.row_input.setText(self.row_for_calc)

    def clean_row(self):
        self.row_for_calc = ''
        self.row_input.setText(self.row_for_calc)

    def delete_last(self):
        self.row_for_calc = self.row_input.text()[0:-1]
        self.row_input.setText(self.row_for_calc)


def main():
    # Create app and window
    app = QApplication([])
    ex = App()
    ex.setStyle(QStyleFactory.create('CDEstyle'))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
