import os
index='''<meta charset="utf-8">
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>超链接网页</title>
<style>
  body {
      margin: 0;
          padding: 0;
              font-family: Arial, sans-serif;
                  background-color: #3498db; /* 蓝色背景 */
                      color: #ffffff; /* 白色文字 */
                        }

                          .container {
                              display: flex;
                                  flex-direction: column;
                                      align-items: center;
                                          justify-content: center;
                                              height: 100vh;
                                                  text-align: center;
                                                    }

                                                      .link {
                                                          display: block;
                                                              margin: 10px 0;
                                                                  font-size: 24px;
                                                                      font-weight: bold;
                                                                          color: #ffffff; /* 白色文字 */
                                                                              text-decoration: none; /* 去掉超链接下划线 */
                                                                                }
                                                    
  .link2 {
  display: block;                                                                                                 margin: 10px 0;                                                                                                 font-size: 24px;                                                                                                font-weight: bold;                                                                                              color: #ff0000; /*红色文字 */                                                                                  text-decoration: none; /* 去掉超链接下划线 */
        }
        </style>
                                                                                </style>
                                                                                </head>
                                                                                <body>
                                                                                <div class="container">'''
def fu(d):
 index_=index
 for i in os.listdir(d):
    if not i.startswith(".") and os.path.isfile(d+'/'+i) and i!='index.html':
        index_+=f"<a href='/otherrepo.github.io{d[1:]}/{i}' class='link'>{i}</a></br>"
    elif os.path.isdir(d+'/'+i) and not i.startswith('.'):   
        index_+=f"<a href='/otherrepo.github.io{d[1:]}/{i}/index.html' class='link2'>{i}</a></br>"
        fu(d+'/'+i)
 index_+='''</div>
 </body>
 </html>'''
 with open(f"{d}/index.html","w")as f:
     f.write(index_)
fu('.')
