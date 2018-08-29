# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import random
import csv

## names = []

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/result")
def result():
    # 한글 써봄, 한글, 주석 써도 에러 안나요
    #1. "/" 날아온 이름 두개를 가져온다.
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    #2. 궁합을 구라친다. (50~100사이의 숫자를 랜덤하게 뽑는다.)
    match = random.randrange(50, 101)
    # 'names.csv' 파일을 만들어서 저장한다.
    f = open('names.csv', 'a+')
    a = csv.writer(f)
    a.writerow([name1, name2])
    f.close
    ## names라는 배열에 입력된 두 이름을 넣는다.
##    names.append(name1)
##    names.append(name2)
    return render_template('result.html', name1 = name1, name2 = name2, match=match)
    
@app.route("/admin")
def admin():
    # names에 들어가 있는 모든 이름을 출력한다.
    f = open('names.csv', 'r', encoding='utf-8')
    rr = csv.reader(f)
    names = rr
    return render_template('admin.html', names=names)
    
app.run(host='0.0.0.0', port='8080', debug=True)