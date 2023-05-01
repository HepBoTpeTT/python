import sys
import os
import typing
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5 import QtCore, uic
from MailCheker import mail_cheker

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        uic.loadUi('UI\\MainUI.ui',self)

        self.addMsgBtn.clicked.connect(self.initMsgForm)

        self.show()

    def initMsgForm(self):
        self.addMsgBtn.clicked = NewMsgForm()

class NewMsgForm(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        uic.loadUi('UI\\NewMesGiag.ui', self)
        self.clientName = self.nameLine.text()
        self.clientData = self.dataLine.text()
        self.clientTime = self.timeLine.text()

        self.calendarWidget.setVisible(False)
        self.dataBtn.clicked.connect(self.open_calendar)
        self.calendarWidget.clicked.connect(self.close_calendar)

    def open_calendar(self):
        self.calendarWidget.setVisible(True)

    def close_calendar(self):
        self.dataLine.setText(self.calendarWidget.selectedDate().toString('dd.MM.yyyy'))
        self.calendarWidget.setVisible(False)

class SignWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        uic.loadUi('UI\\SignUP-IN.ui', self)
        self.stackedWidget.setCurrentIndex(0)
        self.show()

        self.toLoginBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.toRegisterBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.registerbtn.clicked.connect(self.sign_up)
        self.loginbtn.clicked.connect(self.sign_in)

    def sign_up(self):
        uMail = self.email.text()
        uLogin = self.login.text()
        uPass = self.password.text()
        uControlPass = self.password2.text()

        if (uPass == uControlPass and mail_cheker(uMail) and uLogin and uPass):
            with open("Users.txt", "a+", encoding="utf-8") as file:
                file.write(uLogin + "\t" + uPass + "\t" + uMail + '\n')
                self.registerbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        elif(uPass != uControlPass):
            self.password.setText('')
            self.password2.setText('')
            self.errorLabel.setText('Пароли не совпадают.')

        elif(not mail_cheker(uMail)):
            self.email.setText('')
            self.login.setText('')
            self.password.setText('')
            self.password2.setText('')
            self.errorLabel.setText('Такого E-mail не существует.')
        else:
            self.email.setText('')
            self.login.setText('')
            self.password.setText('')
            self.password2.setText('')
            self.errorLabel.setText('Заполните все поля.')

    def sign_in(self):
        data = {}
        with open('Users.txt', "r+", encoding='utf-8') as file:
            for string in file.readlines():
                data[string.strip().split()[0]] = string.strip().split()[1]
            
        if (self.login_2.text() in data.keys()):
            if (data[self.login_2.text()] == self.password_2.text()):
                self.loginbtn.clicked = Main()
                self.close()
            else:
                self.password_2.setText('')
                self.lerrorLabel_2.setText('Неверный пароль')
        elif(not self.login_2.text() or not self.password_2.text()):
            self.lerrorLabel_2.setText('Заполните все поля.')
        else:
            self.login_2.setText('')
            self.password_2.setText('')
            self.lerrorLabel_2.setText('Учётной записи не существует')

if __name__ == '__main__':
    os.chdir('C:\\Users\\root\\Downloads\\python-main\\Python project')
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec())