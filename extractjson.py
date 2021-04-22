from urllib.request import urlopen

html=urlopen(" http://py4e-data.dr-chuck.net/comments_1127081.json")
count=0
data=''''''
for line in html:
    data=data+line.strip().decode()
print(data)

import json
info=json.loads(data)
comments=info["comments"]
count=0
for comment in comments:
    count=count+comment["count"]
print(count)
