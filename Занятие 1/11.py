minute = int(input())
hour = minute // 60
minute -= hour * 60
hour -= 24 * (hour // 24)
print(hour, minute)