import os
index='<meta charset="utf-8">'
for i in os.listdir('./'):
    if not i.startswith("."):
        index+=f"<a href='/otherrepo.github.io/{i}'>{i}</a></br>"
with open("index.html","w") as f:
    f.write(index)

         
