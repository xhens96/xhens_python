import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QApplication, QLineEdit, QComboBox, QPlainTextEdit, QMessageBox


class Search_Window(QWidget):
    def __init__(self, parent=None):
        super(Search_Window, self).__init__(parent)
        self.initUI()
        self.show()


        self.Event_txt1 = ""
        self.Event_txt2 = ""


    def initUI(self):
        Label1 = QLabel("이름 : ", self)
        Label2 = QLabel("위치 : ", self)
        Label3 = QLabel("설명 : ", self)
        self.txt1 = QComboBox(self)
        self.txt2 = QLineEdit(self)
        self.txt3 = QPlainTextEdit(self)

        self.btn1 = QPushButton("돌아가기", self)
        self.btn2 = QPushButton("이벤트 창", self)


        self.txt1.setFixedSize(440, 25)
        self.txt2.setFixedSize(440, 25)
        self.txt3.setFixedSize(500, 300)

        Label1.move(20, 20)
        Label2.move(20, 60)
        Label3.move(20, 100)

        self.txt1.move(80, 20)
        self.txt2.move(80, 60)
        self.txt3.move(20, 140)

        self.btn1.move(437, 450)
        self.btn1.clicked.connect(self.btnAction)

        self.btn2.move(337, 450)
        self.btn2.clicked.connect(self.btn2Action)

        self.txt2.setReadOnly(True)
        self.txt3.setReadOnly(True)

    def btnAction(self, event):
        self.close()

    # 추가 부분
    def btn2Action(self, event):
        QMessageBox.warning(self, self.Event_txt1, self.Event_txt2)
    #


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Search_Window()
    window.show()
    print(app)
    sys.exit(app.exec_())
