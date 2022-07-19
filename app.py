from flask import Flask, render_template
from controllers.drivers_controller import drivers_blueprint
from controllers.races_controller import races_blueprint

app = Flask(__name__)

app.register_blueprint(drivers_blueprint)
app.register_blueprint(races_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)