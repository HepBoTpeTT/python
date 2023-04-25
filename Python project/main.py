import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
from MailCheker import mail_cheker

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        uic.loadUi('UI\\MainUI.ui',self)
        self.show()


class SignUp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        uic.loadUi('UI\\SignUpUI.ui',self)
        self.show()

        self.registerbtn.clicked.connect(self.signUp)
        self.toLoginBtn.clicked.connect(self.to_login)
    
    def signUp(self):
        uMail = self.email.text()
        uLogin = self.login.text()
        uPass = self.password.text()
        uControlPass = self.password2.text()

        if (uPass == uControlPass and mail_cheker(uMail) and uLogin and uPass):
            with open("Users.txt", "a+", encoding="utf-8") as file:
                file.write(uLogin + "\t" + uPass + "\t" + uMail + '\n')
                self.registerbtn.clicked = SignIn()
                self.close()

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

    def to_login(self):
        self.toLoginBtn.clicked = SignIn()
        self.close()

class SignIn(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        uic.loadUi('UI\\SignInUI.ui',self)
        self.show()

        self.loginbtn.clicked.connect(self.sign_in)
        self.toRegisterBtn.clicked.connect(self.to_register)

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

    def to_register(self):
        self.toRegisterBtn.clicked = SignUp()
        self.close()

if __name__ == '__main__':
    os.chdir('C:\\Users\\Денис\\Desktop\\AutoMes\\Python project\\')
    app = QApplication(sys.argv)
    window = SignIn()
    sys.exit(app.exec())