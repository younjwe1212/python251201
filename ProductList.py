import sys
import sqlite3
import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QFont

# DB 파일 생성 및 접속
DB_FILE = "MyProducts.db"

if os.path.exists(DB_FILE):
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
else:
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE Products (
            prodID INTEGER PRIMARY KEY AUTOINCREMENT,
            prodName TEXT NOT NULL,
            prodPrice INTEGER NOT NULL
        )
    """)
    con.commit()

class ProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadProducts()

    def initUI(self):
        self.setWindowTitle("전자제품 관리 시스템")
        self.setGeometry(100, 100, 800, 600)
        
        # 중앙 위젯
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 레이아웃
        layout = QVBoxLayout()
        
        # 입력 영역
        input_layout = QHBoxLayout()
        
        # 제품ID (읽기 전용)
        input_layout.addWidget(QLabel("제품ID:"))
        self.prodID = QLineEdit()
        self.prodID.setReadOnly(True)
        self.prodID.setMaximumWidth(80)
        input_layout.addWidget(self.prodID)
        
        # 제품명
        input_layout.addWidget(QLabel("제품명:"))
        self.prodName = QLineEdit()
        self.prodName.setMaximumWidth(200)
        input_layout.addWidget(self.prodName)
        
        # 제품가격
        input_layout.addWidget(QLabel("가격:"))
        self.prodPrice = QLineEdit()
        self.prodPrice.setMaximumWidth(100)
        input_layout.addWidget(self.prodPrice)
        
        input_layout.addStretch()
        layout.addLayout(input_layout)
        
        # 버튼 영역
        btn_layout = QHBoxLayout()
        
        self.btn_add = QPushButton("추가")
        self.btn_add.clicked.connect(self.addProduct)
        btn_layout.addWidget(self.btn_add)
        
        self.btn_update = QPushButton("수정")
        self.btn_update.clicked.connect(self.updateProduct)
        btn_layout.addWidget(self.btn_update)
        
        self.btn_delete = QPushButton("삭제")
        self.btn_delete.clicked.connect(self.deleteProduct)
        btn_layout.addWidget(self.btn_delete)
        
        self.btn_search = QPushButton("검색")
        self.btn_search.clicked.connect(self.searchProduct)
        btn_layout.addWidget(self.btn_search)
        
        self.btn_clear = QPushButton("초기화")
        self.btn_clear.clicked.connect(self.clearInput)
        btn_layout.addWidget(self.btn_clear)
        
        btn_layout.addStretch()
        layout.addLayout(btn_layout)
        
        # 테이블 위젯
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 300)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.doubleClicked.connect(self.doubleClick)
        layout.addWidget(self.tableWidget)
        
        central_widget.setLayout(layout)

    def addProduct(self):
        prodName = self.prodName.text().strip()
        prodPrice = self.prodPrice.text().strip()
        
        if not prodName or not prodPrice:
            QMessageBox.warning(self, "경고", "제품명과 가격을 입력해주세요.")
            return
        
        try:
            cur.execute("INSERT INTO Products (prodName, prodPrice) VALUES (?, ?)",
                       (prodName, int(prodPrice)))
            con.commit()
            QMessageBox.information(self, "성공", "제품이 추가되었습니다.")
            self.clearInput()
            self.loadProducts()
        except Exception as e:
            QMessageBox.critical(self, "오류", f"추가 실패: {str(e)}")

    def updateProduct(self):
        prodID = self.prodID.text().strip()
        prodName = self.prodName.text().strip()
        prodPrice = self.prodPrice.text().strip()
        
        if not prodID or not prodName or not prodPrice:
            QMessageBox.warning(self, "경고", "모든 필드를 입력해주세요.")
            return
        
        try:
            cur.execute("UPDATE Products SET prodName=?, prodPrice=? WHERE prodID=?",
                       (prodName, int(prodPrice), int(prodID)))
            con.commit()
            QMessageBox.information(self, "성공", "제품이 수정되었습니다.")
            self.clearInput()
            self.loadProducts()
        except Exception as e:
            QMessageBox.critical(self, "오류", f"수정 실패: {str(e)}")

    def deleteProduct(self):
        prodID = self.prodID.text().strip()
        
        if not prodID:
            QMessageBox.warning(self, "경고", "제품ID를 선택해주세요.")
            return
        
        reply = QMessageBox.question(self, "삭제 확인", "정말 삭제하시겠습니까?",
                                    QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            try:
                cur.execute("DELETE FROM Products WHERE prodID=?", (int(prodID),))
                con.commit()
                QMessageBox.information(self, "성공", "제품이 삭제되었습니다.")
                self.clearInput()
                self.loadProducts()
            except Exception as e:
                QMessageBox.critical(self, "오류", f"삭제 실패: {str(e)}")

    def searchProduct(self):
        prodName = self.prodName.text().strip()
        
        if not prodName:
            QMessageBox.warning(self, "경고", "검색할 제품명을 입력해주세요.")
            return
        
        self.tableWidget.setRowCount(0)
        try:
            cur.execute("SELECT * FROM Products WHERE prodName LIKE ?",
                       (f"%{prodName}%",))
            row = 0
            for item in cur:
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item[0])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(item[2])))
                row += 1
            
            if row == 0:
                QMessageBox.information(self, "검색 결과", "검색 결과가 없습니다.")
        except Exception as e:
            QMessageBox.critical(self, "오류", f"검색 실패: {str(e)}")

    def loadProducts(self):
        self.tableWidget.setRowCount(0)
        try:
            cur.execute("SELECT * FROM Products ORDER BY prodID DESC")
            row = 0
            for item in cur:
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item[0])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(item[2])))
                row += 1
        except Exception as e:
            QMessageBox.critical(self, "오류", f"데이터 로드 실패: {str(e)}")

    def doubleClick(self):
        current_row = self.tableWidget.currentRow()
        if current_row < 0:
            return
        
        prodID = self.tableWidget.item(current_row, 0).text()
        prodName = self.tableWidget.item(current_row, 1).text()
        prodPrice = self.tableWidget.item(current_row, 2).text()
        
        self.prodID.setText(prodID)
        self.prodName.setText(prodName)
        self.prodPrice.setText(prodPrice)

    def clearInput(self):
        self.prodID.clear()
        self.prodName.clear()
        self.prodPrice.clear()
        self.prodName.setFocus()
        self.loadProducts()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductWindow()
    window.show()
    sys.exit(app.exec_())