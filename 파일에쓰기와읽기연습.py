#파일에쓰기와읽기연습.py

#demo.txt 파일에 문자열을

f = open("demo.txt", "wt", encoding="utf-8")
f.write("안녕하세요\n")
f.write("파이썬 파일 입출력 연습입니다.\n")
f.close()

#demo.txt 파일에서 문자열을 읽기
f = open("demo.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()
