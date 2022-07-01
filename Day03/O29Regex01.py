
import re

# res = re.match(r'^This', st)
# print(f"res :{res}")
# res = re.search(r'string$', st)
# st = "This is a sample string"
# res = re.search(r'b.t', st)  #- matches anything - alphbets, numbers and special characters
# res = re.search(r'ba*t', st)
# res = re.search(r'ba?t', st)
# res = re.search(r'ba+t', st)
# res = re.search(r'ba{3}t', st)
# res = re.search(r'ba{3,}t', st)
# res = re.search(r'ba{3,8}t', st)
# res = re.search(r'b[aeiou]t', st)
# res = re.search(r'b[^aeiou]t', st)
# res = re.search(r'b(ai|es)t', st)

st = "sample.py"

res = re.search(r'\.py$', st)

if res:
    print("Match found....")
    print(res.group(0))                 # string that matched our regex
else:
    print("Match not found.....")
