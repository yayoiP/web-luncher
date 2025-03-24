import csv,pyperclip as ppc,subprocess,os
from flask import *
def dataget():
    with open("./.csv",encoding="utf-8") as f:
        reader = csv.reader(f)
        data=[i for i in reader]
    return list(reversed(data))
def delete(number):
    aaa=dataget()
    del aaa[number]
    with open("./.csv","w",encoding="utf-8",newline="") as f:
        writer = csv.writer(f)
        
        writer.writerow(aaa)
def dataadd(data):
    aaa=dataget()
    with open("./.csv","w",encoding="utf-8",newline="") as f:
        writer = csv.writer(f)
        print([str(len(aaa)+1)]+data)
        aaa=[[str(len(aaa)+1)]+data]+aaa
        print(aaa)
        writer.writerows(aaa)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html',datas=dataget()) # templatesフォルダ内のindex.htmlを表示する

@app.route("/link/<value>")
def valuu(value):
    access = "/".join(request.url.split("/")[0:3])
    ppc.copy(f"{access}/app/{value}")
    return redirect("/")
@app.route("/app/<value>")
def valee(value):
    if str(int(value[0])-1)=="-":
        return "不正"
    print(dataget()[int(value)-1][2])
    subprocess.run(["start",dataget()[int(value)-1][2]],shell=True)
    return "<script>window.close()</script>タブを閉じてください。"
if __name__ == '__main__':
    app.run()
