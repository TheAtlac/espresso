import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, \
    QVBoxLayout, QApplication, QMainWindow, QWidget

cur = sqlite3.connect('coffee.sqlite')


class CoffeeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.cur = cur
        self.initUI()

    def initUI(self):
        pass
        # self.setGeometry(500, 500, 740, 400)
        # self.setWindowTitle('кофе')
        # self.w = QWidget()
        # self.setCentralWidget(self.w)
        # self.vbox = QVBoxLayout(self.w)
        # self.table_widget = QTableWidget()
        # self.vbox.addWidget(self.table_widget)
        self.set_values()

    def set_values(self):
        """заполняет таблицу данными"""
        request = "SELECT distinct * FROM sorts order by id"
        # берёт информацию обо всех законченных играх
        result = self.cur.execute(request).fetchall()
        self.table_widget.setColumnCount(7)
        self.table_widget.setRowCount(len(result))
        # Устанавливает заголовки колонок
        self.table_widget.setHorizontalHeaderLabels(['id', 'name', 'roasting', 'type', 'discription',
                                                     'price', 'size (g)'])
        # Распределяет по тоблице нформацию об играх
        for i, elem in enumerate(result):
            elem = list(elem)
            # Заменит id на понятные имена
            elem[3] = self.cur.execute("select name from types where id=?", (str(elem[3]),)) \
                .fetchone()[0]
            for j, val in enumerate(elem):
                self.table_widget.setItem(i, j,
                                          QTableWidgetItem(str(val)))


app = QApplication(sys.argv)
ex = CoffeeWindow()
ex.show()
sys.exit(app.exec())
