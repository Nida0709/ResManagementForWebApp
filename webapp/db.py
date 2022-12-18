import sqlite3

DATABASE = 'database.db'


def create_reserve_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS reserves \
        (name, tell, date, n_hon, n_kin, res1, n_res1, \
            res2, n_res2, res3, n_res3, res4, n_res4, res5, n_res5, other)")
    con.close()