import sys
from PyQt5.Qt import *
from logic import work_with_row


class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.answer = ''
        self.window = QWidget()
        self.window.setWindowTitle('NEW')
        type_font = 'Comfortaa'
        self.grid = QGridLayout(self.window)
        self.menubar = QMenuBar(self.window)
        self.menubar.setGeometry(0, 0, 500, 25)
        file = self.menubar.addMenu('orjej')
        file.addAction('ewou')
        font_size = 18
        self.row_for_calc = ''
        size_x, size_y = 60, 60
        self.row_input = QLineEdit()
        self.row_input.setFixedSize(260, 40)
        self.row_input.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.row_input, 1, 0, 1, 4, alignment=Qt.AlignCenter)

        self.btn_0 = QPushButton('0')
        self.grid.addWidget(self.btn_0, 5, 0, 5, 2, alignment=Qt.AlignTop)
        self.btn_0.clicked.connect(lambda: self.create_row('0'))
        self.btn_0.setFixedSize(size_x, size_y)
        self.btn_0.setFont(QFont(type_font, font_size))

        self.btn_1 = QPushButton('1')
        self.grid.addWidget(self.btn_1, 2, 0)
        self.btn_1.clicked.connect(lambda: self.create_row('1'))
        self.btn_1.setFixedSize(size_x, size_y)
        self.btn_1.setFont(QFont(type_font, font_size))

        self.btn_2 = QPushButton('2')
        self.grid.addWidget(self.btn_2, 2, 1)
        self.btn_2.clicked.connect(lambda: self.create_row('2'))
        self.btn_2.setFixedSize(size_x, size_y)
        self.btn_2.setFont(QFont(type_font, font_size))

        self.btn_3 = QPushButton('3')
        self.grid.addWidget(self.btn_3, 2, 2)
        self.btn_3.clicked.connect(lambda: self.create_row('3'))
        self.btn_3.setFixedSize(size_x, size_y)
        self.btn_3.setFont(QFont(type_font, font_size))

        self.btn_4 = QPushButton('4')
        self.grid.addWidget(self.btn_4, 3, 0)
        self.btn_4.clicked.connect(lambda: self.create_row('4'))
        self.btn_4.setFixedSize(size_x, size_y)
        self.btn_4.setFont(QFont(type_font, font_size))

        self.btn_5 = QPushButton('5')
        self.grid.addWidget(self.btn_5, 3, 1)
        self.btn_5.clicked.connect(lambda: self.create_row('5'))
        self.btn_5.setFixedSize(size_x, size_y)
        self.btn_5.setFont(QFont(type_font, font_size))

        self.btn_6 = QPushButton('6')
        self.grid.addWidget(self.btn_6, 3, 2)
        self.btn_6.clicked.connect(lambda: self.create_row('6'))
        self.btn_6.setFixedSize(size_x, size_y)
        self.btn_6.setFont(QFont(type_font, font_size))

        self.btn_7 = QPushButton('7')
        self.grid.addWidget(self.btn_7, 4, 0)
        self.btn_7.clicked.connect(lambda: self.create_row('7'))
        self.btn_7.setFixedSize(size_x, size_y)
        self.btn_7.setFont(QFont(type_font, font_size))

        self.btn_8 = QPushButton('8')
        self.grid.addWidget(self.btn_8, 4, 1)
        self.btn_8.clicked.connect(lambda: self.create_row('8'))
        self.btn_8.setFixedSize(size_x, size_y)
        self.btn_8.setFont(QFont(type_font, font_size))

        self.btn_9 = QPushButton('9')
        self.grid.addWidget(self.btn_9, 4, 2)
        self.btn_9.clicked.connect(lambda: self.create_row('9'))
        self.btn_9.setFixedSize(size_x, size_y)
        self.btn_9.setFont(QFont(type_font, font_size))

        self.btn_dot = QPushButton('.')
        self.grid.addWidget(self.btn_dot, 5, 1)
        self.btn_dot.clicked.connect(lambda: self.create_row('.'))
        self.btn_dot.setFixedSize(size_x, size_y)
        self.btn_dot.setFont(QFont(type_font, font_size))

        self.btn_enter = QPushButton('Enter')
        self.grid.addWidget(self.btn_enter, 6, 0, 6, 5, alignment=Qt.AlignCenter)
        self.btn_enter.clicked.connect(self.enter)
        self.btn_enter.setFixedSize(size_x * 4, size_y * 2)
        self.btn_enter.setFont(QFont(type_font, font_size))

        self.btn_plus = QPushButton('+')
        self.grid.addWidget(self.btn_plus, 2, 3)
        self.btn_plus.clicked.connect(lambda: self.create_row('+'))
        self.btn_plus.setFixedSize(size_x, size_y)
        self.btn_plus.setFont(QFont(type_font, font_size))

        self.btn_minus = QPushButton('-')
        self.grid.addWidget(self.btn_minus, 3, 3)
        self.btn_minus.clicked.connect(lambda: self.create_row('-'))
        self.btn_minus.setFixedSize(size_x, size_y)
        self.btn_minus.setFont(QFont(type_font, font_size))

        self.btn_multiplication = QPushButton('*')
        self.grid.addWidget(self.btn_multiplication, 4, 3)
        self.btn_multiplication.clicked.connect(lambda: self.create_row('*'))
        self.btn_multiplication.setFixedSize(size_x, size_y)
        self.btn_multiplication.setFont(QFont(type_font, font_size))

        self.btn_ac = QPushButton('AC')
        self.grid.addWidget(self.btn_ac, 5, 2)
        self.btn_ac.clicked.connect(lambda: self.clean_row())
        self.btn_ac.setFixedSize(size_x, size_y)
        self.btn_ac.setFont(QFont(type_font, font_size))

        self.btn_delete = QPushButton('<=')
        self.grid.addWidget(self.btn_delete, 5, 3)
        self.btn_delete.clicked.connect(lambda: self.delete_last())
        self.btn_delete.setFixedSize(size_x, size_y)
        self.btn_delete.setFont(QFont(type_font, font_size))

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

    def info_about(self):
        print('ihhj')


def main():
    # Create app and window
    app = QApplication([])
    ex = App()
    ex.setStyle(QStyleFactory.create('CDEstyle'))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
