from flask import Flask, Blueprint, redirect, render_template, request

constructors_blueprint = Blueprint('constructors', __name__)

@constructors_blueprint.route('/constructors')
def index():
    return render_template('constructors/index.html')