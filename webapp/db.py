import sqlite3, os, json

DATABASE = 'database.db'
OTHER_DATABASE = 'other_database.db'


def create_reserve_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS reserves \
        (resID, name, tell, date, n_hon, n_kin, res1, n_res1, \
            res2, n_res2, res3, n_res3, res4, n_res4, res5, n_res5, other)")
    con.close()

def create_other_reserve_table():
    con = sqlite3.connect(OTHER_DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS reserves \
        (resID, date, name, quantity, frag)")
    con.close()

def resID_remind():
    if not os.path.exists(os.getcwd() + os.sep + 'webapp' + os.sep + 'count.txt'):
        data = 'c' + str(1)
        with open(os.getcwd() + os.sep + 'webapp' + os.sep + 'count.txt', 'w', encoding='UTF8') as fp:
            fp.write(str(data))

def other_resID_remind():
    if not os.path.exists(os.getcwd() + os.sep + 'webapp' + os.sep + 'count.txt'):
        data = 'c' + str(1)
        with open(os.getcwd() + os.sep + 'webapp' + os.sep + 'other_count.txt', 'w', encoding='UTF8') as fp:
            fp.write(str(data))