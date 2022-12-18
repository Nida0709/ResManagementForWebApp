#cd dir.....
#export FLASK_APP=webapp
#flask run -h 0.0.0.0 -p 3000
from flask import Flask
app = Flask(__name__)

import webapp.main


from webapp import db
db.create_reserve_table()

db.resID_remind()