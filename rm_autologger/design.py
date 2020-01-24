from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 298)
        self.btn_today = QtWidgets.QPushButton(Form)
        self.btn_today.setGeometry(QtCore.QRect(50, 62, 301, 51))
        self.btn_today.setObjectName("btn_today")
        self.btn_yesterday = QtWidgets.QPushButton(Form)
        self.btn_yesterday.setGeometry(QtCore.QRect(50, 130, 301, 51))
        self.btn_yesterday.setObjectName("btn_yesterday")
        self.btn_lastday = QtWidgets.QPushButton(Form)
        self.btn_lastday.setGeometry(QtCore.QRect(50, 200, 301, 51))
        self.btn_lastday.setObjectName("btn_lastday")
        self.lbl_select_date = QtWidgets.QLabel(Form)
        self.lbl_select_date.setGeometry(QtCore.QRect(50, 15, 301, 31))
        self.lbl_select_date.setObjectName("lbl_select_date")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_today.setText(_translate("Form", "Сегодня"))
        self.btn_yesterday.setText(_translate("Form", "Вчера"))
        self.btn_lastday.setText(_translate("Form", "Позавчера"))
        self.lbl_select_date.setText(_translate("Form", "<html><head/><body><p align=\"center\">Выберите дату промежуточной фиксации:</p></body></html>"))
