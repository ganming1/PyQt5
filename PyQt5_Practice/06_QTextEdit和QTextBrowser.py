import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QTextBrowser
# 文本编辑框QTextEdit和文本浏览框QTextBrowser
class Demo(QWidget):
    def __init__(self):   # 初试化函数
        super(Demo, self).__init__()
        self.edit_label = QLabel("QTextEdit", self)
        self.browser_label = QLabel("QTextBrowser", self)
        self.text_edit = QTextEdit(self)
        self.text_browser = QTextBrowser(self)

        self.edit_v_layout = QVBoxLayout()
        self.browser_v_layout = QVBoxLayout()
        self.all_h_layout = QHBoxLayout()

        self.layout_init()
        self.text_edit_init()

    def layout_init(self):      # 布局初试化
        self.edit_v_layout.addWidget(self.edit_label)
        self.edit_v_layout.addWidget(self.text_edit)
        self.browser_v_layout.addWidget(self.browser_label)
        self.browser_v_layout.addWidget(self.text_browser)
        self.all_h_layout.addLayout(self.edit_v_layout)
        self.all_h_layout.addLayout(self.browser_v_layout)

        self.setLayout(self.all_h_layout)

    def text_edit_init(self):    # 文本编辑框初试化   可以在文本编辑框中写Html代码
        self.text_edit.textChanged.connect(self.show_text_func)   # 链接槽函数1

    def show_text_func(self):   # 定义槽函数1
        # self.text_edit.toPlainText()获取文本编辑框文本。不是.text()
        self.text_browser.setText(self.text_edit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())