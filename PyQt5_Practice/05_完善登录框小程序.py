import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QPushButton,\
    QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox, QFormLayout

USER_PWD = {
    "ganming": "123456"
}

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 100)

        self.user_label = QLabel("Username:", self)
        self.pwd_label = QLabel("Password", self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton("Log in", self)
        self.signin_button = QPushButton("Sign in",self)

        self.grid_layout = QGridLayout()   # 网格布局管理器
        self.h_layout = QHBoxLayout()      # 水平布局管理器
        self.v_layout = QVBoxLayout()      # 垂直布局管理器

        self.lineedit_init()
        self.pushbutton_init()
        self.layout_init()
        self.signin_page = SigninPage()    # 实例化SigninPage()

    def layout_init(self):
        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)



    def lineedit_init(self):     # QLineEdit空间的初始化
        self.user_line.setPlaceholderText("Please enter your username")
        self.pwd_line.setPlaceholderText("Please enter your password")
        self.pwd_line.setEchoMode(QLineEdit.Password)   # 将输入的密码用原点表示

        self.user_line.textChanged.connect(self.check_input_func)     # 链接槽函数1
        self.pwd_line.textChanged.connect(self.check_input_func)

    def pushbutton_init(self):    # QPushButton空间的初始化
        self.login_button.setEnabled(False)
        self.login_button.clicked.connect(self.check_login_func)      # 链接槽函数2
        self.signin_button.clicked.connect(self.show_signin_page_func)   # 链接槽函数3

    def check_input_func(self):     # 定义槽函数1
        if self.user_line.text() and self.pwd_line.text():
            self.login_button.setEnabled(True)
        else:
            self.login_button.setEnabled(False)

    def check_login_func(self):      # 定义槽函数2
        if USER_PWD.get(self.user_line.text()) == self.pwd_line.text():
            # print("登录成功！")
            QMessageBox.information(self, 'Information', 'Log in Successgully!')
        else:
            # print("登录失败")
            QMessageBox.critical(self, "Wrong", "Wrong Username or Password!")

        self.user_line.clear()
        self.pwd_line.clear()

    def show_signin_page_func(self):   # 定义槽函数3
        # 在槽函数中，我们用exec_方法来执行注册界面。为什么要使用exec_而不是show()？
        # 下面来详细解释下这两个方法的区别：
        # 若使用exec_()的话，那么显示出来的注册界面就是模态的，意思就是当前智能对该注册界面进行操作，
        # 只有关闭了该界面才能对其他界面进行操作；若使用show()的话，那注册界面就是非模态的，
        # 则在显示了注册界面后，还能同时对登录界面进行操作(QDialog有ecec_()方法，而QWidget没有)。
        # self.signin_page.show()
        self.signin_page.exec_()

class SigninPage(QDialog):
    def __init__(self):
        super(SigninPage, self).__init__()
        self.signin_user_label = QLabel("Username:", self)
        self.signin_pwd_label = QLabel("Password:", self)
        self.signin_pwd2_label = QLabel("Password:", self)
        self.signin_user_line = QLineEdit(self)
        self.signin_pwd_line = QLineEdit(self)
        self.signin_pwd2_line = QLineEdit(self)
        self.signin_button = QPushButton("Sign in", self)

        self.f_layout = QFormLayout()
        self.v_layout = QVBoxLayout()

        self.layout_init()
        self.lineedit_init()
        self.pushbutton_init()

    def layout_init(self):
        self.f_layout.addRow(self.signin_user_label, self.signin_user_line)
        self.f_layout.addRow(self.signin_pwd_label, self.signin_pwd_line)
        self.f_layout.addRow(self.signin_pwd2_label, self.signin_pwd2_line)
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.signin_button)

        self.setLayout(self.v_layout)

    def lineedit_init(self):
        self.signin_pwd_line.setEchoMode(QLineEdit.Password)
        self.signin_pwd2_line.setEchoMode(QLineEdit.Password)
        self.signin_user_line.textChanged.connect(self.check_input_func)
        self.signin_pwd_line.textChanged.connect(self.check_input_func)
        self.signin_pwd2_line.textChanged.connect(self.check_input_func)

    def pushbutton_init(self):
        self.signin_button.setEnabled(False)
        self.signin_button.clicked.connect(self.check_signin_func)

    def check_input_func(self):
        if self.signin_user_line.text() and self.signin_pwd_line.text() and self.signin_pwd2_line.text():
            self.signin_button.setEnabled(True)
        else:
            self.signin_button.setEnabled(False)

    def check_signin_func(self):
        if self.signin_pwd_line.text() != self.signin_pwd2_line.text():
            QMessageBox.critical(self, "Wrong", "Two Passwords Typed Are Not Same!")
        elif self.signin_user_line.text() not in USER_PWD:
            USER_PWD[self.signin_user_line.text()] = self.signin_pwd_line.text()
            QMessageBox.information(self, "Information", "Register Successfully!")
            print(USER_PWD)
            self.close()    # 当注册成功时，注册页面要关闭
        else:
            QMessageBox.critical(self, "Wrong", "This Username Has Been Registered!")

        self.signin_user_line.clear()
        self.signin_pwd_line.clear()
        self.signin_pwd2_line.clear()


if __name__ == '__main__':
    print(USER_PWD)
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())