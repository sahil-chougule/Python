import RE
import re

pattern = r"world!$"
s = RE.content2()

match = re.search(pattern,s)

if match:
    print("Match Found")
else:    
    print("Match not found")    