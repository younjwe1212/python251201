#문자열 처리 메서드 연습

strA ="python programming"
strB ="파이썬은 강력해"

print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))

data ="    spam and ham   "
result = data.strip()
print(data)
print(result)

#치환
result2 = strA.replace("spam","spam egg")
print(result2)

#리스트로 분할
lst =result2.split()
print(lst)
#문자열 합치기
joined = ":)".join(lst)
print(joined)

#정규표현식:특정한 패턴을 찾아서 바로 작업

import re

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

#이메일 주소 검증#이메일 주소 검증




























        print(f"✗ {email} - 무효함")    else:        print(f"✓ {email} - 유효함")    if re.match(email_pattern, email):for email in emails:print("=== 이메일 주소 검증 결과 ===")# 이메일 검증 결과 출력]    "wrong@domain"    "a@b.co",    "valid_email+tag@test.org",    "double@@domain.com",    "spaces in@email.com",    "no-at-sign.com",    "invalid.email@",    "test123@gmail.com",    "john.doe@company.co.kr",    "user@example.com",emails = [# 테스트할 이메일 주소 10개email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'# 이메일 패턴 정규표현식import reimport re

# 이메일 패턴 정규표현식
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# 테스트할 이메일 주소 10개
emails = [
    "user@example.com",
    "john.doe@company.co.kr",
    "test123@gmail.com",
    "invalid.email@",
    "no-at-sign.com",
    "spaces in@email.com",
    "double@@domain.com",
    "valid_email+tag@test.org",
    "a@b.co",
    "wrong@domain"
]

# 이메일 검증 결과 출력
print("=== 이메일 주소 검증 결과 ===")
for email in emails:
    if re.match(email_pattern, email):
        print(f"✓ {email} - 유효함")
    else:
        print(f"✗ {email} - 무효함")

