import sys

from PyQt5 import uic, QtGui
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui')
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        view = QTableView(self)
        view.setModel(model)
        view.resizeColumnsToContents()
        view.resize(638, 315)

        self.setGeometry(300, 100, 638, 450)
        self.setWindowTitle('Пример работы с QtSql')

    # def initUI(self):
    #     # Зададим тип базы данных
    #     db = QSqlDatabase.addDatabase('QSQLITE')
    #     # Укажем имя базы данных
    #     db.setDatabaseName('Chinook_Sqlite.sqlite')
    #     # И откроем подключение
    #     db.open()
    #
    #     # QTableView - виджет для отображения данных из базы
    #     view = QTableView(self)
    #     # Создадим объект QSqlTableModel,
    #     # зададим таблицу, с которой он будет работать,
    #     #  и выберем все данные
    #     model = QSqlTableModel(self, db)
    #     model.setTable('artist')
    #     model.
    #     model.select()
    #
    #     # Для отображения данных на виджете
    #     # свяжем его и нашу модель данных
    #     view.setModel(model)
    #     view.move(10, 10)
    #     view.resize(617, 315)
    #
    #     self.setGeometry(300, 100, 650, 450)
    #     self.setWindowTitle('Пример работы с QtSql')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
