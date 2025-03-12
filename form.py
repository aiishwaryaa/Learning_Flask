from flask import Flask , render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit',methods=["POST"])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password= request.form['password']
        return f"Thank you {name} ! Your registration is successful."
    
if __name__ == '__main__':
    app.run(debug=True)