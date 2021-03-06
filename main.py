from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 70, 301, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_7.setObjectName("btn_7")
        self.gridLayout_2.addWidget(self.btn_7, 1, 0, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_1.setObjectName("btn_1")
        self.gridLayout_2.addWidget(self.btn_1, 3, 0, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_4.setObjectName("btn_4")
        self.gridLayout_2.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_5.setObjectName("btn_5")
        self.gridLayout_2.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_sub = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_sub.setFont(font)
        self.btn_sub.setStyleSheet("background-color: rgb(255, 226, 0);")
        self.btn_sub.setObjectName("btn_sub")
        self.gridLayout_2.addWidget(self.btn_sub, 3, 3, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_8.setMaximumSize(QtCore.QSize(93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_8.setObjectName("btn_8")
        self.gridLayout_2.addWidget(self.btn_8, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.btn_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_2.setObjectName("btn_2")
        self.gridLayout_2.addWidget(self.btn_2, 3, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_3.setObjectName("btn_3")
        self.gridLayout_2.addWidget(self.btn_3, 3, 2, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_0.setObjectName("btn_0")
        self.gridLayout_2.addWidget(self.btn_0, 4, 0, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_6.setObjectName("btn_6")
        self.gridLayout_2.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_del = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_del.setFont(font)
        self.btn_del.setStyleSheet("background-color: rgb(255, 226, 0);")
        self.btn_del.setObjectName("btn_del")
        self.gridLayout_2.addWidget(self.btn_del, 0, 3, 1, 1)
        self.btn_bracket1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_bracket1.setFont(font)
        self.btn_bracket1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_bracket1.setObjectName("btn_bracket1")
        self.gridLayout_2.addWidget(self.btn_bracket1, 0, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout_2.addWidget(self.btn_9, 1, 2, 1, 1)
        self.btn_prod = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_prod.setFont(font)
        self.btn_prod.setStyleSheet("background-color: rgb(255, 226, 0);")
        self.btn_prod.setObjectName("btn_prod")
        self.gridLayout_2.addWidget(self.btn_prod, 2, 3, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_dot.setFont(font)
        self.btn_dot.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout_2.addWidget(self.btn_dot, 4, 1, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_div.setFont(font)
        self.btn_div.setStyleSheet("background-color: rgb(255, 226, 0);")
        self.btn_div.setObjectName("btn_div")
        self.gridLayout_2.addWidget(self.btn_div, 1, 3, 1, 1)
        self.btn_result = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_result.setFont(font)
        self.btn_result.setStyleSheet("background-color: rgb(255, 226, 0);")
        self.btn_result.setObjectName("btn_result")
        self.gridLayout_2.addWidget(self.btn_result, 4, 2, 1, 1)
        self.btn_add = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("background-color: rgb(255, 226, 0);")
        self.btn_add.setObjectName("btn_add")
        self.gridLayout_2.addWidget(self.btn_add, 4, 3, 1, 1)
        self.btn_Clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Clear.setFont(font)
        self.btn_Clear.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_Clear.setObjectName("btn_Clear")
        self.gridLayout_2.addWidget(self.btn_Clear, 0, 0, 1, 1)
        self.btn_bracket2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_bracket2.setFont(font)
        self.btn_bracket2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_bracket2.setObjectName("btn_bracket2")
        self.gridLayout_2.addWidget(self.btn_bracket2, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 300, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

        self.is_res = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_sub.setText(_translate("MainWindow", "-"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_del.setText(_translate("MainWindow", "<--"))
        self.btn_bracket1.setText(_translate("MainWindow", "("))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_prod.setText(_translate("MainWindow", "*"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_result.setText(_translate("MainWindow", "="))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_Clear.setText(_translate("MainWindow", "C"))
        self.btn_bracket2.setText(_translate("MainWindow", ")"))
        self.label.setText(_translate("MainWindow", "0"))


    def add_functions(self):
        self.btn_0.clicked.connect(lambda: self.write(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write(self.btn_9.text()))
        self.btn_add.clicked.connect(lambda: self.write(self.btn_add.text()))
        self.btn_div.clicked.connect(lambda: self.write(self.btn_div.text()))
        self.btn_dot.clicked.connect(lambda: self.write(self.btn_dot.text()))
        self.btn_prod.clicked.connect(lambda: self.write(self.btn_prod.text()))
        self.btn_sub.clicked.connect(lambda: self.write(self.btn_sub.text()))
        self.btn_bracket1.clicked.connect(lambda: self.write(self.btn_bracket1.text()))
        self.btn_bracket2.clicked.connect(lambda: self.write(self.btn_bracket2.text()))

        self.btn_result.clicked.connect(self.results)
        self.btn_Clear.clicked.connect(self.clear)
        self.btn_del.clicked.connect(self.delete)

    def write(self, number):
        if self.label.text() == "0" or self.is_res:
            self.label.setText(number)
            self.is_res = False
        else:
            self.label.setText(self.label.text() + number)

    def results(self):
        try:
            res = eval(self.label.text())
            self.label.setText(str(res))
            self.is_res = True
        except:
            self.label.setText("Wrong input")

    def clear(self):
        self.label.setText("0")

    def delete(self):
        text = self.label.text()
        self.label.setText(text[:len(text) - 1])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
