import os
index='<meta charset="utf-8>"'
for i in os.listdir('./'):
    if not i.startswith("."):
        index+=f"<a href=/{i}>{i}</a></br>"
with open("index.html","w") as f:
    f.write(index)

         
