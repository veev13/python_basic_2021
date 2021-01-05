books = list()  # 책 목록 선언
# 책 목록 만들기
books.append({'제목': '개발자의 코드', '출판연도': '2013.02.28', '출판사': 'A출판', '쪽수': 200, '추천유무': False})
books.append({'제목': '클린 코드', '출판연도': '2013.03.04', '출판사': 'B출판', '쪽수': 584, '추천유무': True})
books.append({'제목': '빅데이터 마케팅', '출판연도': '2014.07.02', '출판사': 'A출판', '쪽수': 296, '추천유무': True})
books.append({'제목': '구글드', '출판연도': '2010.02.10', '출판사': 'B출판', '쪽수': 526, '추천유무': False})
books.append({'제목': '강의력', '출판연도': '2013.12.12', '출판사': 'C출판', '쪽수': 248, '추천유무': True})

# 1
one = [i['제목'] for i in books if i['쪽수'] > 250]
print(one)
# 2
two = [i['제목'] for i in books if i['추천유무']]
print(two)
# 3
three = set([i['출판사'] for i in books])
print(three)
