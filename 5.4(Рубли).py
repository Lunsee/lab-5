k = input("Введите сумму покупки в копейках: ")
s = 0
lenght = len(k)
k = int(k)
r = k // 100
d = 1
rword = 0
kword = 0
i = 1
for i in range(lenght):
    d = d * 10
kword = k % 100  # узнаем 2 последние цифры
if k > 999:
    rword = k - kword
    r = rword / 100
    r = int(r)
    r1 = r
    r = r % 100
if int((r >= 5 and r <= 20) or (r >= 25 and r <= 30) or (r >= 35 and r <= 40) or (r >= 45 and r <= 50) or (
        r >= 55 and r <= 60) or (r >= 65 and r <= 70) or (r >= 75 and r <= 80) or (r >= 85 and r <= 90) or (
               r >= 95 and r <= 99) or (k / 100 == 1000) or (k / 1000 == 100)):
    print(str(int(k - kword) / 100) + " рублей")
if int((r >= 2 and r <= 4) or (r >= 22 and r <= 24) or (r >= 32 and r <= 34) or (r >= 42 and r <= 44) or (
        r >= 52 and r <= 54) or (r >= 62 and r <= 64) or (r >= 72 and r <= 74) or (r >= 82 and r <= 84) or (
               r >= 92 and r <= 94)):
    print(str(int(k - kword) / 100) + " рубля")
if int((r == 1) or (r == 21) or (r == 31) or (r == 41) or (r == 51) or (r == 61) or (r == 71) or (r == 81) or (
        r == 91)):
    print(str(int(k - kword) / 100) + " рубль")

if int((kword >= 5 and kword <= 20) or (kword >= 25 and kword <= 30) or (kword >= 35 and kword <= 40) or (
        kword >= 45 and kword <= 50) or (kword >= 55 and kword <= 60) or (kword >= 65 and kword <= 70) or (
               kword >= 75 and kword <= 80) or (kword >= 85 and kword <= 90) or (kword >= 95 and kword <= 99)):
    print(str(kword) + " копеек")
if int((kword >= 2 and kword <= 4) or (kword >= 22 and kword <= 24) or (kword >= 32 and kword <= 34) or (
        kword >= 42 and kword <= 44) or (kword >= 52 and kword <= 54) or (kword >= 62 and kword <= 64) or (
               kword >= 72 and kword <= 74) or (kword >= 82 and kword <= 84) or (kword >= 92 and kword <= 94)):
    print(str(kword) + " копейки")
if int((kword == 1) or (kword == 21) or (kword == 31) or (kword == 41) or (kword == 51) or (kword == 61) or (
        kword == 71) or (kword == 81) or (kword == 91)):
    print(str(kword) + " копейка")