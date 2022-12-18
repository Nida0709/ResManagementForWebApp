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

    df_reserves = pd.DataFrame(db_reserves, columns=('name', 'tell', 'date', 'n_hon', 'n_kin', 'res1', 'n_res1', \
        'res2', 'n_res2', 'res3', 'n_res3', 'res4', 'n_res4', 'res5', 'n_res5', 'other'))

    restext1 = []
    restext2 = []
    restext3 = []
    restext4 = []
    for i in range(len(df_reserves)):
        if df_reserves['date'][i] >= target_uni_date and df_reserves['date'][i] < target_uni_date * second_baked * 3600:
            text = '　 氏名 　：' + df_reserves['name'][i] + '\n'\
                    + ' 電話番号 ：' + df_reserves['tell'][i] + '\n'\
                    + '　 日付 　：' + df_reserves['date'][i] + '\n'\
                    + '食パン(本)：' + df_reserves['n_hon'][i] + '本' + '\n'\
                    + '食パン(斤)：' + df_reserves['n_kin'][i] + '斤' + '\n'\
                    + '　 予約 　：' + '\n'\
                        + df_reserves['res1'][i] + 'x' + df_reserves['n_res1'][i] + '\n'\
                        + df_reserves['res2'][i] + 'x' + df_reserves['n_res2'][i] + '\n'\
                        + df_reserves['res3'][i] + 'x' + df_reserves['n_res3'][i] + '\n'\
                        + df_reserves['res4'][i] + 'x' + df_reserves['n_res4'][i] + '\n'\
                        + df_reserves['res5'][i] + 'x' + df_reserves['n_res5'][i] + '\n'\
                    + ' 伝達事項 ：' + df_reserves['other'][i]
            restext1.append(text)
        elif df_reserves['date'][i] >= target_uni_date * second_baked * 3600 and df_reserves['date'][i] < target_uni_date * third_baked * 3600:
            text = '　 氏名 　：' + df_reserves['name'][i] + '\n'\
                    + ' 電話番号 ：' + df_reserves['tell'][i] + '\n'\
                    + '　 日付 　：' + df_reserves['date'][i] + '\n'\
                    + '食パン(本)：' + df_reserves['n_hon'][i] + '本' + '\n'\
                    + '食パン(斤)：' + df_reserves['n_kin'][i] + '斤' + '\n'\
                    + '　 予約 　：' + '\n'\
                        + df_reserves['res1'][i] + 'x' + df_reserves['n_res1'][i] + '\n'\
                        + df_reserves['res2'][i] + 'x' + df_reserves['n_res2'][i] + '\n'\
                        + df_reserves['res3'][i] + 'x' + df_reserves['n_res3'][i] + '\n'\
                        + df_reserves['res4'][i] + 'x' + df_reserves['n_res4'][i] + '\n'\
                        + df_reserves['res5'][i] + 'x' + df_reserves['n_res5'][i] + '\n'\
                    + ' 伝達事項 ：' + df_reserves['other'][i]
            restext2.append(text)
        elif df_reserves['date'][i] >= target_uni_date * third_baked * 3600 and df_reserves['date'][i] < target_uni_date * forth_baked * 3600:
            text = '　 氏名 　：' + df_reserves['name'][i] + '\n'\
                    + ' 電話番号 ：' + df_reserves['tell'][i] + '\n'\
                    + '　 日付 　：' + df_reserves['date'][i] + '\n'\
                    + '食パン(本)：' + df_reserves['n_hon'][i] + '本' + '\n'\
                    + '食パン(斤)：' + df_reserves['n_kin'][i] + '斤' + '\n'\
                    + '　 予約 　：' + '\n'\
                        + df_reserves['res1'][i] + 'x' + df_reserves['n_res1'][i] + '\n'\
                        + df_reserves['res2'][i] + 'x' + df_reserves['n_res2'][i] + '\n'\
                        + df_reserves['res3'][i] + 'x' + df_reserves['n_res3'][i] + '\n'\
                        + df_reserves['res4'][i] + 'x' + df_reserves['n_res4'][i] + '\n'\
                        + df_reserves['res5'][i] + 'x' + df_reserves['n_res5'][i] + '\n'\
                    + ' 伝達事項 ：' + df_reserves['other'][i]
            restext3.append(text)
        elif df_reserves['date'][i] >= target_uni_date * forth_baked * 3600 and df_reserves['date'][i] < target_uni_date * tomorrow * 3600:
            text = '　 氏名 　：' + df_reserves['name'][i] + '\n'\
                    + ' 電話番号 ：' + df_reserves['tell'][i] + '\n'\
                    + '　 日付 　：' + df_reserves['date'][i] + '\n'\
                    + '食パン(本)：' + df_reserves['n_hon'][i] + '本' + '\n'\
                    + '食パン(斤)：' + df_reserves['n_kin'][i] + '斤' + '\n'\
                    + '　 予約 　：' + '\n'\
                        + df_reserves['res1'][i] + 'x' + df_reserves['n_res1'][i] + '\n'\
                        + df_reserves['res2'][i] + 'x' + df_reserves['n_res2'][i] + '\n'\
                        + df_reserves['res3'][i] + 'x' + df_reserves['n_res3'][i] + '\n'\
                        + df_reserves['res4'][i] + 'x' + df_reserves['n_res4'][i] + '\n'\
                        + df_reserves['res5'][i] + 'x' + df_reserves['n_res5'][i] + '\n'\
                    + ' 伝達事項 ：' + df_reserves['other'][i]
            restext4.append(text)


    reserves1 = [{'content': restext1}]
    reserves2 = [{'content': restext2}]
    reserves3 = [{'content': restext3}]
    reserves4 = [{'content': restext4}]

    return render_template(
        'index.html',
        reservers1=reserves1,
        reservers2=reserves2,
        reservers3=reserves3,
        reservers4=reserves4
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