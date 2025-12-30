from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home/home.html')

@app.route('/about')
def about():
    return render_template('about/about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio/portfolio.html')

@app.route('/team')
def team():
    return render_template('team/team.html')


@app.route('/contact')
def contact():
    return render_template('contact/contact.html')

if __name__ == '__main__':
    app.run(debug=True)