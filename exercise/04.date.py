from datetime import datetime as dt

y = dt.today().year
birth = int(input("태어난 년도: "))
print(f'{y - birth + 1}살')
