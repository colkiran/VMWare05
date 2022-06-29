
"""
1. sort     - will sort the original list
2. sorted   - will return a copy of the sorted list

"""
l1 = [4, 7, 1, 10, 6, 9, 5, 2, 8, 3]
print(f"l1 :{l1}")

# we have to sort the list (asc, desc)
srtl1 = sorted(l1)
print(f"srtl1 :{srtl1}")

srtl2 = sorted(l1, reverse=True)
print(f"srtl2:{srtl2}")

print('-' * 40)
l1 = [4, 'zebra', 'apple', 7, 'yellow', 'blue', 1, 'white', 'cat', 10, 'violet', 'green',
      6, 'purple', 'orange', 9, 'red', 'saw', 5, 2, 8, 3, 19, 1024, 145, 25, 209, 2185]
print(f"l1 :{l1}")
print('-' * 40)
res = sorted(l1, key=ascii)
print(f"res :{res}")

print('=' * 40)
cities = ['thiruvananthapuram', 'bangalore', 'mumbai', 'delhi', 'vishakapatnam', 'ooty',
          'kanyakumari', 'hyderabad', 'pune', 'coimbatore']
print(f"cities :{cities}")

print('-' * 40)
res = sorted(cities, key=ascii)
print(f"res :{res}")

print('-' * 40)
res = sorted(cities, key=len)
print(f"res :{res}")

print('-' * 40)
from calendar import month_name
def srt(mon):
    l = []
    for m in list(month_name):
        l.append(m[0:3].lower())
    if mon in l:
        return l.index(mon)

months = ['dec', 'sep', 'aug', 'jan', 'mar', 'nov', 'feb', 'apr', 'jun', 'may', 'oct', 'jul']
# sort these months as per calender
print(f"Months :{months}")

print('-' * 40)
srtMon = sorted(months, key=srt)
print(f"Sorted Months :{srtMon}")
