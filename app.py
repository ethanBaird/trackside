from flask import Flask, render_template
from controllers.drivers_controller import drivers_blueprint
from controllers.races_controller import races_blueprint
from controllers.results_controller import results_blueprint


app = Flask(__name__)

app.register_blueprint(drivers_blueprint)
app.register_blueprint(races_blueprint)
app.register_blueprint(results_blueprint)


@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)