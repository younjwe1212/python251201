#Domoform.py
#demoform.ui(화면단) + DemoForm.py(로직단) = DemoForm 완성

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인 문서를 로딩
form_class = uic.loadUiType("Demoform.ui")[0]

class DemoForm(QDialog, form_class):
    #  초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")

if __name__ == "__main__":
    #실행프로세스 생성
    app = QApplication(sys.argv)
    demoform = DemoForm()
    demoform.show()
    app.exec_()
