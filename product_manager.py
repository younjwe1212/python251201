import sqlite3
from typing import List, Tuple

class ProductManager:
    def __init__(self, db_name: str = "MyProduct.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect()
        self.create_table()
    
    def connect(self):
        """데이터베이스 연결"""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
    
    def create_table(self):
        """Products 테이블 생성"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                productID INTEGER PRIMARY KEY AUTOINCREMENT,
                productName TEXT NOT NULL,
                productPrice INTEGER NOT NULL
            )
        ''')
        self.connection.commit()
    
    def insert(self, product_name: str, product_price: int) -> int:
        """제품 데이터 삽입"""
        self.cursor.execute(
            'INSERT INTO Products (productName, productPrice) VALUES (?, ?)',
            (product_name, product_price)
        )
        self.connection.commit()
        return self.cursor.lastrowid
    
    def select_all(self) -> List[Tuple]:
        """모든 제품 조회"""
        self.cursor.execute('SELECT * FROM Products')
        return self.cursor.fetchall()
    
    def select_by_id(self, product_id: int) -> Tuple:
        """ID로 제품 조회"""
        self.cursor.execute('SELECT * FROM Products WHERE productID = ?', (product_id,))
        return self.cursor.fetchone()
    
    def update(self, product_id: int, product_name: str, product_price: int) -> bool:
        """제품 정보 수정"""
        self.cursor.execute(
            'UPDATE Products SET productName = ?, productPrice = ? WHERE productID = ?',
            (product_name, product_price, product_id)
        )
        self.connection.commit()
        return self.cursor.rowcount > 0
    
    def delete(self, product_id: int) -> bool:
        """제품 삭제"""
        self.cursor.execute('DELETE FROM Products WHERE productID = ?', (product_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0
    
    def insert_sample_data(self, count: int = 100000):
        """샘플 데이터 대량 삽입"""
        sample_products = [
            (f"제품_{i}", 10000 + (i % 100) * 1000) 
            for i in range(1, count + 1)
        ]
        
        self.cursor.executemany(
            'INSERT INTO Products (productName, productPrice) VALUES (?, ?)',
            sample_products
        )
        self.connection.commit()
        print(f"{count}개의 샘플 데이터가 삽입되었습니다.")
    
    def get_total_count(self) -> int:
        """전체 제품 개수 조회"""
        self.cursor.execute('SELECT COUNT(*) FROM Products')
        return self.cursor.fetchone()[0]
    
    def close(self):
        """데이터베이스 연결 종료"""
        if self.connection:
            self.connection.close()


# 사용 예시
if __name__ == "__main__":
    # ProductManager 초기화
    manager = ProductManager("MyProduct.db")
    
    # 샘플 데이터 10만개 삽입
    print("샘플 데이터 생성 중...")
    manager.insert_sample_data(100000)
    
    # 전체 개수 확인
    print(f"전체 제품 개수: {manager.get_total_count()}")
    
    # 개별 조회
    product = manager.select_by_id(1)
    print(f"\nID 1 제품: {product}")
    
    # 수정
    manager.update(1, "수정된_제품_1", 25000)
    print(f"수정 후: {manager.select_by_id(1)}")
    
    # 삭제
    manager.delete(2)
    print(f"\nID 2 제품 삭제 완료")
    
    # 데이터베이스 연결 종료
    manager.close()