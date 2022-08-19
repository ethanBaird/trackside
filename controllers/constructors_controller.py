from flask import Flask, Blueprint, redirect, render_template, request

import repositories.constructors_repository as constructors_repository
import repositories.drivers_repository as drivers_repository

constructors_blueprint = Blueprint('constructors', __name__)

@constructors_blueprint.route('/constructors')
def index():
    constructors = constructors_repository.select_all()
    drivers = drivers_repository.select_all()
    constructors.sort(key=lambda x: x.points, reverse=True)
    drivers.sort(key=lambda x: x.points, reverse=True)
    return render_template('constructors/index.html', constructors=constructors, drivers=drivers)