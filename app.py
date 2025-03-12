# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<password generator>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from flask import Flask, render_template, request
import random
import string
app = Flask(__name__)

class Password_Generator:
    def __init__(self , length , charAllowed, numAllowed):
        self.length = length
        self.charAllowed = charAllowed
        self.numAllowed = numAllowed

    def Generate_Password(self):
        password = ""
        character = string.ascii_letters 

        if self.charAllowed:
            character += string.punctuation

        if self.numAllowed:
            character += string.digits

        password = "".join(random.choice(character) for _ in range(self.length))
        return password
    
@app.route("/", methods=['GET','POST'])
def home():
    password = ""
    length = 0  # Default password length
    numAllowed = False
    charAllowed = False

    if request.method == 'POST':
        length = int(request.form["length"])#user se length lere h form se 
        if length <=0:
            password = "please enter a valid password length"
        else:    
            numAllowed = "numbers" in request.form
            charAllowed = "special" in request.form
            pg = Password_Generator(length ,numAllowed,charAllowed) 
            password = pg.Generate_Password()
    return render_template("passwordGen.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)  # run the app in debug mode