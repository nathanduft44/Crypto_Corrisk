  
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route("/vis_2017")
def year_2017_vis() :
     return render_template('year_2017_visuals.html')

@app.route("/vis_2018")
def year_2018_vis() :
     return render_template('year_2018_visuals.html')

@app.route("/vis_2019")
def year_2019_vis() :
     return render_template('year_2019_visuals.html')

@app.route("/vis_2020")
def year_2020_vis() :
     return render_template('year_2020_visuals.html')

if __name__ == '__main__':
    app.run(debug=True)