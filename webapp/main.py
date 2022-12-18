import os, sys, csv, phonenumbers, sqlite3, json
from datetime import datetime
import pandas as pd
from webapp import app
from flask import render_template, redirect, request, url_for, flash

DATABASE = 'database.db'











@app.route('/')
def index():
    return render_template(
        'index.html'
    )










@app.route('/table', methods=['POST'])
def table():
    global date
    date = request.form['date']     #from index request for selecting table's date
    dt_date = datetime.strptime(date, "%Y-%m-%dT%H:%M")
    target_uni_date = int(datetime.timestamp(dt_date) - dt_date.hour * 60 * 60 - dt_date.minute * 60 - dt_date.second)
    first_baked = 9
    second_baked = 11.5
    third_baked = 12.5
    forth_baked = 14
    tomorrow = 24

    con = sqlite3.connect(DATABASE)
    db_reserves = con.execute("SELECT * FROM reserves").fetchall()      #fetchall → Form type List
    con.close()

    df_reserves = pd.DataFrame(db_reserves, columns=('resID', 'name', 'tell', 'date', 'n_hon', 'n_kin', 'res1', 'n_res1', \
        'res2', 'n_res2', 'res3', 'n_res3', 'res4', 'n_res4', 'res5', 'n_res5', 'other'))
    col = ['resID', 'name', 'tell', 'date', 'n_hon', 'n_kin', 'res1', 'n_res1', \
        'res2', 'n_res2', 'res3', 'n_res3', 'res4', 'n_res4', 'res5', 'n_res5', 'other']

    reserves1 = []
    reserves2 = []
    reserves3 = []
    reserves4 = []

    for i in range(len(df_reserves)):
        if (df_reserves['date'][i] >= target_uni_date) and (df_reserves['date'][i] < target_uni_date + second_baked * 3600):
            reserves1.append({
                'resID': df_reserves['resID'][i],
                'name': df_reserves['name'][i],
                'tell': df_reserves['tell'][i],
                'date': datetime.fromtimestamp(df_reserves['date'][i]).strftime("%m月%d日 %H時%M分"),
                'n_hon': df_reserves['n_hon'][i],
                'n_kin': df_reserves['n_kin'][i],
                'res1': df_reserves['res1'][i],
                'n_res1': df_reserves['n_res1'][i],
                'res2': df_reserves['res2'][i],
                'n_res2': df_reserves['n_res2'][i],
                'res3': df_reserves['res3'][i],
                'n_res3': df_reserves['n_res3'][i],
                'res4': df_reserves['res4'][i],
                'n_res4': df_reserves['n_res4'][i],
                'res5': df_reserves['res5'][i],
                'n_res5': df_reserves['n_res5'][i]
            })
        elif (df_reserves['date'][i] >= target_uni_date + second_baked * 3600) and (df_reserves['date'][i] < target_uni_date + third_baked * 3600):
            reserves2.append({
                'resID': df_reserves['resID'][i],
                'name': df_reserves['name'][i],
                'tell': df_reserves['tell'][i],
                'date': datetime.fromtimestamp(df_reserves['date'][i]).strftime("%m月%d日 %H時%M分"),
                'n_hon': df_reserves['n_hon'][i],
                'n_kin': df_reserves['n_kin'][i],
                'res1': df_reserves['res1'][i],
                'n_res1': df_reserves['n_res1'][i],
                'res2': df_reserves['res2'][i],
                'n_res2': df_reserves['n_res2'][i],
                'res3': df_reserves['res3'][i],
                'n_res3': df_reserves['n_res3'][i],
                'res4': df_reserves['res4'][i],
                'n_res4': df_reserves['n_res4'][i],
                'res5': df_reserves['res5'][i],
                'n_res5': df_reserves['n_res5'][i]
            })
        elif (df_reserves['date'][i] >= target_uni_date + third_baked * 3600) and (df_reserves['date'][i] < target_uni_date + forth_baked * 3600):
            reserves3.append({
                'resID': df_reserves['resID'][i],
                'name': df_reserves['name'][i],
                'tell': df_reserves['tell'][i],
                'date': datetime.fromtimestamp(df_reserves['date'][i]).strftime("%m月%d日 %H時%M分"),
                'n_hon': df_reserves['n_hon'][i],
                'n_kin': df_reserves['n_kin'][i],
                'res1': df_reserves['res1'][i],
                'n_res1': df_reserves['n_res1'][i],
                'res2': df_reserves['res2'][i],
                'n_res2': df_reserves['n_res2'][i],
                'res3': df_reserves['res3'][i],
                'n_res3': df_reserves['n_res3'][i],
                'res4': df_reserves['res4'][i],
                'n_res4': df_reserves['n_res4'][i],
                'res5': df_reserves['res5'][i],
                'n_res5': df_reserves['n_res5'][i]
            })
        elif (df_reserves['date'][i] >= target_uni_date + forth_baked * 3600) and (df_reserves['date'][i] < target_uni_date + tomorrow * 3600):
            reserves4.append({
                'resID': df_reserves['resID'][i],
                'name': df_reserves['name'][i],
                'tell': df_reserves['tell'][i],
                'date': datetime.fromtimestamp(df_reserves['date'][i]).strftime("%m月%d日 %H時%M分"),
                'n_hon': df_reserves['n_hon'][i],
                'n_kin': df_reserves['n_kin'][i],
                'res1': df_reserves['res1'][i],
                'n_res1': df_reserves['n_res1'][i],
                'res2': df_reserves['res2'][i],
                'n_res2': df_reserves['n_res2'][i],
                'res3': df_reserves['res3'][i],
                'n_res3': df_reserves['n_res3'][i],
                'res4': df_reserves['res4'][i],
                'n_res4': df_reserves['n_res4'][i],
                'res5': df_reserves['res5'][i],
                'n_res5': df_reserves['n_res5'][i]
            })


    return render_template(
        'table.html',
        reservers1=reserves1,
        reservers2=reserves2,
        reservers3=reserves3,
        reservers4=reserves4,
        first_baked=datetime.fromtimestamp(target_uni_date+first_baked*3600).strftime("%H時%M分"),
        second_baked=datetime.fromtimestamp(target_uni_date+second_baked*3600).strftime("%H時%M分"),
        third_baked=datetime.fromtimestamp(target_uni_date+third_baked*3600).strftime("%H時%M分"),
        forth_baked=datetime.fromtimestamp(target_uni_date+forth_baked*3600).strftime("%H時%M分")
    )










@app.route('/table2')
def table2():
    dt_date = datetime.strptime(date, "%Y-%m-%dT%H:%M")
    target_uni_date = int(datetime.timestamp(dt_date) - dt_date.hour * 60 * 60 - dt_date.minute * 60 - dt_date.second)
    first_baked = 9
    second_baked = 11.5
    third_baked = 12.5
    forth_baked = 14
    tomorrow = 24

    con = sqlite3.connect(DATABASE)
    db_reserves = con.execute("SELECT * FROM reserves").fetchall()      #fetchall → Form type List
    con.close()

    df_reserves = pd.DataFrame(db_reserves, columns=('resID', 'name', 'tell', 'date', 'n_hon', 'n_kin', 'res1', 'n_res1', \
        'res2', 'n_res2', 'res3', 'n_res3', 'res4', 'n_res4', 'res5', 'n_res5', 'other'))
    col = ['resID', 'name', 'tell', 'date', 'n_hon', 'n_kin', 'res1', 'n_res1', \
        'res2', 'n_res2', 'res3', 'n_res3', 'res4', 'n_res4', 'res5', 'n_res5', 'other']

    reserves1 = []
    reserves2 = []
    reserves3 = []
    reserves4 = []

    for i in range(len(df_reserves)):
        if (df_reserves['date'][i] >= target_uni_date) and (df_reserves['date'][i] < target_uni_date + second_baked * 3600):
            reserves1.append({
                'resID': df_reserves['resID'][i],
                'name': df_reserves['name'][i],
                'tell': df_reserves['tell'][i],
                'date': datetime.fromtimestamp(df_reserves['date'][i]).strftime("%m月%d日 %H時%M分"),
                'n_hon': df_reserves['n_hon'][i],
                'n_kin': df_reserves['n_kin'][i],
                'res1': df_reserves['res1'][i],
                'n_res1': df_reserves['n_res1'][i],
                'res2': df_reserves['res2'][i],
                'n_res2': df_reserves['n_res2'][i],
                'res3': df_reserves['res3'][i],
                'n_res3': df_reserves['n_res3'][i],
                'res4': df_reserves['res4'][i],
                'n_res4': df_reserves['n_res4'][i],
                'res5': df_reserves['res5'][i],
                'n_res5': df_reserves['n_res5'][i]
            })
        elif (df_reserves['date'][i] >= target_uni_date + second_baked * 3600) and (df_reserves['date'][i] < target_uni_date + third_baked * 3600):
            reserves2.append({
                'resID': df_reserves['resID'][i],
                'name': df_reserves['name'][i],
                'tell': df_reserves['tell'][i],
                'date': datetime.fromtimestamp(df_reserves['date'][i]).strftime("%m月%d日 %H時%M分"),
                'n_hon': df_reserves['n_hon'][i],
                'n_kin': df_reserves['n_kin'][i],
                'res1': df_reserves['res1'][i],
                'n_res1': df_reserves['n_res1'][i],
                'res2': df_reserves['res2'][i],
                'n_res2': df_reserves['n_res2'][i],
                'res3': df_reserves['res3'][i],
                'n_res3': df_reserves['n_res3'][i],
                'res4': df_reserves['res4'][i],
                'n_res4': df_reserves['n_res4'][i],
                'res5': df_reserves['res5'][i],
                'n_res5': df_reserves['n_res5'][i]
            })
        elif (df_reserves['date'][i] >= target_uni_date + third_baked * 3600) and (df_reserves['date'][i] < target_uni_date + forth_baked * 3600):
            reserves3.append({
                'resID': df_reserves['resID'][i],
                'name': df_reserves['name'][i],
                'tell': df_reserves['tell'][i],
                'date': datetime.fromtimestamp(df_reserves['date'][i]).strftime("%m月%d日 %H時%M分"),
                'n_hon': df_reserves['n_hon'][i],
                'n_kin': df_reserves['n_kin'][i],
                'res1': df_reserves['res1'][i],
                'n_res1': df_reserves['n_res1'][i],
                'res2': df_reserves['res2'][i],
                'n_res2': df_reserves['n_res2'][i],
                'res3': df_reserves['res3'][i],
                'n_res3': df_reserves['n_res3'][i],
                'res4': df_reserves['res4'][i],
                'n_res4': df_reserves['n_res4'][i],
                'res5': df_reserves['res5'][i],
                'n_res5': df_reserves['n_res5'][i]
            })
        elif (df_reserves['date'][i] >= target_uni_date + forth_baked * 3600) and (df_reserves['date'][i] < target_uni_date + tomorrow * 3600):
            reserves4.append({
                'resID': df_reserves['resID'][i],
                'name': df_reserves['name'][i],
                'tell': df_reserves['tell'][i],
                'date': datetime.fromtimestamp(df_reserves['date'][i]).strftime("%m月%d日 %H時%M分"),
                'n_hon': df_reserves['n_hon'][i],
                'n_kin': df_reserves['n_kin'][i],
                'res1': df_reserves['res1'][i],
                'n_res1': df_reserves['n_res1'][i],
                'res2': df_reserves['res2'][i],
                'n_res2': df_reserves['n_res2'][i],
                'res3': df_reserves['res3'][i],
                'n_res3': df_reserves['n_res3'][i],
                'res4': df_reserves['res4'][i],
                'n_res4': df_reserves['n_res4'][i],
                'res5': df_reserves['res5'][i],
                'n_res5': df_reserves['n_res5'][i]
            })


    return render_template(
        'table.html',
        reservers1=reserves1,
        reservers2=reserves2,
        reservers3=reserves3,
        reservers4=reserves4,
        first_baked=datetime.fromtimestamp(target_uni_date+first_baked*3600).strftime("%H時%M分"),
        second_baked=datetime.fromtimestamp(target_uni_date+second_baked*3600).strftime("%H時%M分"),
        third_baked=datetime.fromtimestamp(target_uni_date+third_baked*3600).strftime("%H時%M分"),
        forth_baked=datetime.fromtimestamp(target_uni_date+forth_baked*3600).strftime("%H時%M分")
    )









@app.route('/form')
def form():
    return render_template(
        'form.html'
    )










@app.route('/register', methods=['POST'])
def register():
    with open(os.getcwd() + os.sep + 'webapp' + os.sep + 'count.txt', 'r', encoding='UTF8') as fp:
        count = fp.read()
    count = int(count[1:])

        


    resID = int(count)
    name = request.form['name']
    tel = '(+81)' + str(request.form['tel'])
    date = request.form['day']
    n_hon = request.form['n_hon']
    n_kin = request.form['n_kin']
    res1 = request.form['res1']
    n_res1 = request.form['n_res1']
    res2 = request.form['res2']
    n_res2 = request.form['n_res2']
    res3 = request.form['res3']
    n_res3 = request.form['n_res3']
    res4 = request.form['res4']
    n_res4 = request.form['n_res4']
    res5 = request.form['res5']
    n_res5 = request.form['n_res5']
    other = request.form['other']

    tel_hyphen = phonenumbers.parse(tel, 'JP')
    str_tel = phonenumbers.format_number(tel_hyphen, phonenumbers.PhoneNumberFormat.NATIONAL)

    dt_date = datetime.strptime(date, "%Y-%m-%dT%H:%M")
    uni_date = datetime.timestamp(dt_date)

    if n_hon == '':
        n_hon = 0
    if n_kin == '':
        n_kin = 0
    
    con = sqlite3.connect(DATABASE)
    con.execute("INSERT INTO reserves VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
        [resID, name, str_tel, uni_date, n_hon, n_kin, res1, n_res1, res2, n_res2, res3, n_res3, res4, n_res4, res5, n_res5, other])
    con.commit()
    con.close()

    resID = resID + 1
    resID = 'c' + str(resID)
    with open(os.getcwd() + os.sep + 'webapp' + os.sep + 'count.txt', 'w', encoding='UTF8') as fp:
        fp.write(resID)
    return redirect(url_for('form'))










@app.route("/<int:id>/delete",methods=["GET"])
def delete(id):
    con = sqlite3.connect(DATABASE)
    con.execute("DELETE FROM reserves WHERE resID="+str(id))
    con.commit()
    con.close()

    return redirect(url_for('table2'))