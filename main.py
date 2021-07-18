from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/agriculture")
def agriculture():
    return render_template('agriculture.html')


@app.route("/art")
def art():
    return render_template('art.html')


@app.route("/Connect")
def connect():
    return render_template('hope.html')


@app.route("/contacts")
def contacts():
    return render_template('books.html')


@app.route("/business")
def business():
    return render_template('business.html')


@app.route("/travel_routes/")
def travel():
    return render_template('economy.html')


@app.route("/Stories of hope")
def hope():
    return render_template('hope.html')


@app.route("/Help")
def help_page():
    return render_template('help.html')


@app.route("/Cuisine")
def cuisine():
    return render_template('cuisine.html')


@app.route("/events")
def events():
    return render_template('events.html')


@app.route("/fashion")
def fashion():
    return render_template('fashion.html')


@app.route("/music")
def music():
    return render_template('music.html')


@app.route("/Investing")
def invest():
    return render_template('invest.html')


@app.route("/tourism")
def tourism():
    return render_template('tourism.html')


@app.route("/Sports")
def sports():
    return render_template('trending.html')


@app.route("/counter")
def counter():
    return render_template('counter.html')


@app.route("/About")
def about():
    return render_template('about.html')


@app.route("/Popular_Music")
def popular():
    return render_template('popular.html')


@app.route("/Hip-Hop_Music")
def hiphop():
    return render_template('hiphop.html')


@app.route("/House_Music")
def house():
    return render_template('house.html')


@app.route("/RnB_Soul_Music")
def rnb():
    return render_template('rnb.html')


@app.route("/Culture_Music")
def culture():
    return render_template('culture.html')


@app.route("/Jazz_Music")
def jazz():
    return render_template('jazz.html')


@app.route("/Other_Music")
def other():
    return render_template('other.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0,')

