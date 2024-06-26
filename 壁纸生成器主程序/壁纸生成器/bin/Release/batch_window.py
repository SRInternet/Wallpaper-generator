# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batch.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
import sys
from tkinter import *
from tkinter import messagebox

root1 = Tk()
root1.withdraw()

number = 10

class Ui_Dialog(object):
    def __init__(self, generate_type):
        self.generate_type = generate_type

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(670, 196)
        Dialog.setWindowFlags(Dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        Dialog.setFixedSize(Dialog.width(), Dialog.height());
        Dialog.setWindowIcon(QtGui.QIcon("bikini60s_layers.ico"))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(310, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.ok_clicked)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 110, 641, 21))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setValue(10)
        self.horizontalSlider.valueChanged.connect(self.updateLineEdit)
        self.textEdit = QtWidgets.QLineEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(70, 60, 91, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText("10")
        self.textEdit.textChanged.connect(self.updateTextEdit)
        self.validator = QIntValidator()
        self.textEdit.setValidator(self.validator)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 631, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 631, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label_2.raise_()
        self.buttonBox.raise_()
        self.horizontalSlider.raise_()
        self.textEdit.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "批量生成 - 配置"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>生成的类型：{}</p></body></html>").format(self.generate_type))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>数量：</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:10pt; font-weight:600; color:#ff0000;\">某些时候，可能无法获取100张图片，最多99张</span></p></body></html>"))
        self.label_3.hide()

    def updateLineEdit(self, value):
        self.textEdit.setText(str(value))

    def updateTextEdit(self, text):
        try:
            if int(text) < 1:
                text = 1
                self.textEdit.setText(str(text))
            elif int(text) > 100:
                text = 100
                self.textEdit.setText(str(text))
            else:
                pass

            if int(text) >= 100:
                self.label_3.show()
            else:
                self.label_3.hide()

            self.horizontalSlider.setValue(int(text))
        except ValueError:
            pass

    def ok_clicked(self):
        global number
        number = self.horizontalSlider.value()
        self.number = number


# app = QtWidgets.QApplication(sys.argv)
# dialog = QtWidgets.QDialog()  # 创建一个QDialog对象
# ui = Ui_Dialog("666")
# ui.setupUi(dialog)  # 将Ui_Dialog实例与QDialog对象关联
# dialog.show()
# sys.exit(app.exec_())
