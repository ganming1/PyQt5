#-----------------------------------------------------------------------------------------------
# # 垂直布局---QVBoxLayout---

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
#
# class Demo(QWidget):
#
#     def __init__(self):
#         super(Demo, self).__init__()
#         self.user_label = QLabel('Username:', self)
#         self.pwd_label = QLabel('Password:', self)
#
#         self.v_layout = QVBoxLayout()
#         self.v_layout.addWidget(self.user_label)
#         self.v_layout.addWidget(self.pwd_label)
#
#         self.setLayout(self.v_layout)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec())
#-----------------------------------------------------------------------------------------------

# # 水平布局---QHBoxLayout---

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout
#
# class Demo(QWidget):
#     def __init__(self):
#         super(Demo, self).__init__()
#         self.user_label = QLabel('Username:', self)
#         self.user_line = QLineEdit(self)
#
#         self.h_layout = QHBoxLayout()
#         self.h_layout.addWidget(self.user_label)
#         self.h_layout.addWidget(self.user_line)
#
#         self.setLayout(self.h_layout)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec())
#-----------------------------------------------------------------------------------------------

# # 混合使用----QVBoxLayout 和 QHBoxLayout----

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel,\
#     QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
#
#
# class Demo(QWidget):
#     def __init__(self):
#         super(Demo, self).__init__()
#
#         self.user_label = QLabel('Username:', self)
#         self.pwd_label = QLabel("Password:", self)
#         self.user_line = QLineEdit(self)
#         self.pwd_line = QLineEdit(self)
#         self.login_button = QPushButton('Log in', self)
#         self.signin_button = QPushButton('Sign in', self)
#         # # -----方式一
#         # self.label_v_layout = QVBoxLayout()
#         # self.line_v_layout = QVBoxLayout()
#         # self.label_line_h_layout = QHBoxLayout()
#         # self.button_h_layout = QHBoxLayout()
#         # self.all_v_layout = QVBoxLayout()
#         #
#         # self.label_v_layout.addWidget(self.user_label)
#         # self.label_v_layout.addWidget(self.pwd_label)
#         # self.line_v_layout.addWidget(self.user_line)
#         # self.line_v_layout.addWidget(self.pwd_line)
#         # self.label_line_h_layout.addLayout(self.label_v_layout)
#         # self.label_line_h_layout.addLayout(self.line_v_layout)
#         # self.button_h_layout.addWidget(self.login_button)
#         # self.button_h_layout.addWidget(self.signin_button)
#         # self.all_v_layout.addLayout(self.label_line_h_layout)
#         # self.all_v_layout.addLayout(self.button_h_layout)
#         # self.setLayout(self.all_v_layout)
#         # 方式二
#         self.user_line_h_layout = QHBoxLayout()
#         self.pwd_line_h_layout = QHBoxLayout()
#         self.button_h_layout = QHBoxLayout()
#         self.all_v_layout = QVBoxLayout()
#         self.user_line_h_layout.addWidget(self.user_label)
#         self.user_line_h_layout.addWidget(self.user_line)
#         self.pwd_line_h_layout.addWidget(self.pwd_label)
#         self.pwd_line_h_layout.addWidget(self.pwd_line)
#         self.button_h_layout.addWidget(self.login_button)
#         self.button_h_layout.addWidget(self.signin_button)
#         self.all_v_layout.addLayout(self.user_line_h_layout)
#         self.all_v_layout.addLayout(self.pwd_line_h_layout)
#         self.all_v_layout.addLayout(self.button_h_layout)
#         self.setLayout(self.all_v_layout)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec())
#-----------------------------------------------------------------------------------------------

# 表单布局----QFormLayout-----

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit,\
#     QPushButton,QHBoxLayout, QVBoxLayout, QFormLayout
# class Demo(QWidget):
#     def __init__(self):
#         super(Demo, self).__init__()
#
#         self.user_label = QLabel('Username:', self)
#         self.pwd_label = QLabel('Password:', self)
#         self.user_line = QLineEdit(self)
#         self.pwd_line = QLineEdit(self)
#         self.login_button = QPushButton('Log in', self)
#         self.signin_button = QPushButton('Sign', self)
#
#         self.f_layout = QFormLayout()
#         self.button_h_layout = QHBoxLayout()
#         self.all_v_layout = QVBoxLayout()
#
#         self.f_layout.addRow(self.user_label, self.user_line)  # 表单布局通过--addRow--方法添加label和line
#         self.f_layout.addRow(self.pwd_label, self.pwd_line)
#         self.button_h_layout.addWidget(self.login_button)
#         self.button_h_layout.addWidget(self.signin_button)
#         self.all_v_layout.addLayout(self.f_layout)
#         self.all_v_layout.addLayout(self.button_h_layout)
#
#         self.setLayout(self.all_v_layout)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec())
#-----------------------------------------------------------------------------------------------

# 网格布局----QGridLayout-----

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit,\
    QPushButton,QHBoxLayout, QVBoxLayout, QGridLayout
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign', self)

        self.grid_layout = QGridLayout()
        self.button_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)  # 表单布局通过--addRow--方法添加label和line
        self.grid_layout.addWidget(self.pwd_label, 1, 0)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1)
        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_button)
        self.all_v_layout.addLayout(self.grid_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())