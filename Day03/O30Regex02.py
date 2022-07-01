
import re

ln = "LCNO-KAR-70-2022-0925"

res = re.search(r'LCNO-(KAR|KER|APN|TND|TNS|MAH|GOA)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})-'
                r'(?!0000)([0-9]{4})', ln)

if res:
    print("Match found....")
    print(res.group(0))
    print(res.group(1))
else:
    print("Match not found.....")
