import requests
from bs4 import BeautifulSoup
import csv
import re
import time

BASE_URL = "https://finance.naver.com/sise/entryJongmok.naver"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
CSV_PATH = r"c:\work\kpi200_top.csv"
MAX_PAGES = 20  # 안전한 상한

def fetch_page(page):
    params = {"type": "KPI200", "page": str(page)}
    r = requests.get(BASE_URL, headers=HEADERS, params=params, timeout=10)
    r.encoding = r.apparent_encoding
    return r.text

def parse_table_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    box = soup.find("div", class_="box_type_m")
    if not box:
        return []
    table = box.find("table", class_="type_1")
    if not table:
        return []
    # 헤더
    ths = [th.get_text(strip=True) for th in table.find_all("th")]
    rows = []
    for tr in table.find_all("tr"):
        tds = tr.find_all("td")
        if not tds:
            continue
        row = {}
        for i, td in enumerate(tds):
            # 첫 컬럼(종목명)은 링크와 종목코드 추출
            if i == 0:
                a = td.find("a")
                if a:
                    name = a.get_text(strip=True)
                    href = a.get("href", "")
                    m = re.search(r"code=(\d+)", href)
                    code = m.group(1) if m else ""
                    row["종목명"] = name
                    row["code"] = code
                else:
                    row["종목명"] = td.get_text(strip=True)
                    row["code"] = ""
            else:
                text = td.get_text(strip=True)
                # 숫자 정리(쉼표 및 공백 제거)
                text = text.replace("\xa0", " ").strip()
                row_key = ths[i] if i < len(ths) else f"col{i}"
                row[row_key] = text
        rows.append(row)
    return rows

def crawl_all_pages(max_pages=MAX_PAGES, delay=0.5):
    all_rows = []
    for p in range(1, max_pages + 1):
        html = fetch_page(p)
        rows = parse_table_from_html(html)
        if not rows:
            break
        all_rows.extend(rows)
        # 페이지 네비게이션이 끝나면 중단할 수 있게 검사
        # (예: 마지막 페이지에 도달하면 다음 페이지에서 rows가 빈 리스트로 반환됨)
        time.sleep(delay)
    return all_rows

def save_csv(rows, path=CSV_PATH):
    if not rows:
        print("수집된 데이터가 없습니다.")
        return
    # fieldnames 순서 지정: 종목명, code, 그 외
    keys = ["종목명", "code"]
    for r in rows:
        for k in r.keys():
            if k not in keys:
                keys.append(k)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
    print(f"CSV 저장: {path}")

def main():
    print("크롤링 시작: 네이버 코스피200 편입종목상위")
    rows = crawl_all_pages()
    print(f"수집된 항목 수: {len(rows)}")
    # 샘플 출력 (최대 10개)
    for i, r in enumerate(rows[:10], 1):
        print(f"{i:02d}. {r.get('종목명','')} ({r.get('code','')}) - {r.get('현재가','')}")
    save_csv(rows)

if __name__ == "__main__":
    main()