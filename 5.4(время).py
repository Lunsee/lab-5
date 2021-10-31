SentTh = int(input("Время отправления(Час) = "))
SentTmin = int(input("Время отправления(Мин) = "))
WayTh = int(input("Время в пути(Час) = "))
WayTmin = int(input("Время в пути(Мин) = "))

TDay = 0
THour = 0
TMin = 0

THour = WayTh - SentTh
TMin = WayTmin + SentTmin
if TMin >= 60:
    THour = THour + 1
    TMin = TMin - 60
    if THour > 24:
        TDay = TDay + 1
        THour = THour - 24
print(str(THour) + ":" + str(TMin))
print("Дней в пути " + str(TDay))