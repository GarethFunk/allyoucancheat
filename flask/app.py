from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/fakemydata')
def fakemydata():
    return render_template('fakemydata.html')

if __name__ == '__main__':
    app.run(debug=True)