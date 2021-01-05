# yesterday.txt의 절대경로로 file open
file = open("C:/Users/user/Downloads/multicampus cloud/python/python_programming_stu/mycode/3_string/yesterday.txt", 'r')
# file의 내용을 string으로 반환
yesterday_lyric = file.read()

# YESTERDAY 라는 단어가 몇번 나왔는지
print(yesterday_lyric.upper().count('YESTERDAY'))
# Yesterday 라는 단어가 몇번 나왔는지
print(yesterday_lyric.count('Yesterday'))
# yesterday 라는 단어가 몇번 나왔는지
print(yesterday_lyric.count('yesterday'))
