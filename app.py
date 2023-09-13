from flask import Flask, render_template,url_for,redirect

app= Flask(__name__)

@app.route('/')
def redirect_index():
    return redirect(url_for('index'))

@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5020, debug=True)