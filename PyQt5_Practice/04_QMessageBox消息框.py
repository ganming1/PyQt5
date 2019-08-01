import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

# QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel |
# QMessageBox.Ok | QMessageBox.Close | QMessageBox.Open |
# QMessageBox.Save
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton("Click Me!", self)
        self.button.clicked.connect(self.show_messagebox)
# -------<各种类型的信号框>开始----------------------------------------------------
#     def show_messagebox(self):
#     # information 信号框
#         QMessageBox.information(self, "Title", "Content",
#                                 QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
#     # question 问答框
#         QMessageBox.question(self, "Title", "Content",
#                                 QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
#     # warning 警告框
#         QMessageBox.warning(self, "Title", "Content",
#                              QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
#     # critical 错误框
#         QMessageBox.critical(self, "Title", "Content",
#                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
#     # about 关于框
#         QMessageBox.about(self, "Title", "Content",
#                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
# -----------------------------------------------------------<各种类型的信号框>结束

# -------<与消息框交互>开始---------------------------------------------------------
    def show_messagebox(self):
        choice = QMessageBox.question(self, "Change Text?", "Would you like to change the button text?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            self.button.setText("Changed!")
        elif choice == QMessageBox.No:
            pass
# ----------------------------------------------------------------<与消息框交互>结束



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())