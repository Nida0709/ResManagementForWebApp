import os, sys, csv, phonenumbers, sqlite3
from datetime import datetime
import pandas as pd
from webapp import app
from flask import render_template, redirect, request, url_for

DATABASE = 'database.db'


@app.route('/')
def index():
    return render_template(
        'index.html',
    )

@app.route('/table', methods=['POST'])
def table():
    con = sqlite3.connect(DATABASE)
    db_reserves = con.execute("SELECT * FROM reserves").fetchall()      #fetchall → Form type List
    con.close()

    columns=('name', 'tell', 'date', 'n_hon', 'n_kin', 'res1', 'n_res1', \
        'res2', 'n_res2', 'res3', 'n_res3', 'res4', 'n_res4', 'res5', 'n_res5', 'other')
    return render_template(
        'index.html',
        reservers=reserves
    )


@app.route('/form')
def form():
    return render_template(
        'form.html',
    )



@app.route('/register', methods=['POST'])
def register():
    res = []
    n_res = []
    name = request.form['name']
    tel = '(+81)' + str(request.form['tel'])
    day = request.form['day']
    n_hon = request.form['n_hon']
    n_kin = request.form['n_kin']
    res.append(request.form['res1'])
    n_res.append(request.form['n_res1'])
    res.append(request.form['res2'])
    n_res.append(request.form['n_res2'])
    res.append(request.form['res3'])
    n_res.append(request.form['n_res3'])
    res.append(request.form['res4'])
    n_res.append(request.form['n_res4'])
    res.append(request.form['res5'])
    n_res.append(request.form['n_res5'])
    other = request.form['other']

    tel_hyphen = phonenumbers.parse(tel, 'JP')
    str_tel = phonenumbers.format_number(tel_hyphen, phonenumbers.PhoneNumberFormat.NATIONAL)

    dt = datetime.strptime(day, "%Y-%m-%dT%H:%M")
    unixday = datetime.timestamp(dt)

    if n_hon == '':
        n_hon = 0
    if n_kin == '':
        n_kin = 0

    res_text = ''
    if res[0] != '' and n_res[0] != '':
        res_text = res[0] + 'x' + n_res[0]
    for i in range(1, 5):
        if res[i] != '' and n_res[i] != '':
            res_text = res_text + 'nn' + res[i] + 'x' + n_res[i]
    insertdata = [name, str_tel, unixday, n_hon, n_kin, res_text, other]
    
    dataPath = os.getcwd() + os.sep + 'rm' + os.sep + 'rmDatabase.csv'
    with open(dataPath, encoding='shift-jis') as f:           #scan to method_index
        csvreader = csv.reader(f)
        rmDatabase = [row for row in csvreader]
    rmDatabase.append(insertdata)
    df = pd.DataFrame(rmDatabase)
    df.to_csv(dataPath, encoding='shift-jis', header=False, index=False)
    return redirect(url_for('form'))