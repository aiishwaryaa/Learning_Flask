
from flask import Flask , render_template
from data import data_dict
app = Flask(__name__)

@app.route('/user')
def get_id():
    return render_template('hello.html',users= data_dict) 

    
 
     
