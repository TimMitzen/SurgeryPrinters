from flask import Flask, render_template

app = Flask(__name__)  # creates flask object


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/silver4/')
def silver_4():
    return render_template("silver4.html")


@app.route('/silver5/')
def silver_5():
    return render_template("silver5.html")


@app.route('/silver6/')
def silver_6():
    return render_template('silver6.html')
@app.route('/white6/')
def white_6():
    return render_template('white6.html')
@app.route('/pcam4/')
def pcam_4():
    return render_template('pcam4.html')
@app.route('/pcam3/')
def pcam_3():
    return render_template('pcam3.html')



@app.route('/spe14/')
def spe_14():
    return render_template('spe14.html')
@app.route('/spe10/')
def spe_10():
    return render_template("spe14.html")
@app.route('/spe1/')
def spe_1():
    return render_template('spe1.html')
@app.route('/dul2/')
def dul_2():
    return render_template('dul2.html')
@app.route('/founders013/')
def founders_013():
    return render_template('founder013.html')
@app.route('/founders079/')
def founders_079():
    return render_template('founder079.html')
@app.route('/rav2000/')
def rav_2000():
    return render_template("rav2000.html")
@app.route('/rav5000/')
def rav_5000():
    return render_template('rav5000.html')
@app.route('/presby/')
def presby():
    return render_template('presby.html')
if __name__ == '__main__':
    app.run(debug=True)