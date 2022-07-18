from flask import Flask, Blueprint, redirect, render_template, request
from models.driver import Driver

import repositories.drivers_repository as drivers_repository
import repositories.results_repository as results_repository

drivers_blueprint = Blueprint("drivers", __name__)

#index
@drivers_blueprint.route('/drivers')
def drivers():
    drivers = drivers_repository.select_all()
    drivers.sort(key=lambda x: x.points, reverse=True)
    return render_template('drivers/index.html', drivers=drivers)

# show '/drivers/<id>'
@drivers_blueprint.route('/drivers/<id>')
def show(id):
    driver = drivers_repository.select(id)
    results = results_repository.select_by_driver(id)
    return render_template('drivers/show.html', driver=driver, results=results)

# new '/drivers/new'
@drivers_blueprint.route('/drivers/new')
def new():
    return render_template('drivers/new.html')

# create '/drivers/new' method=['POST']
@drivers_blueprint.route('/drivers/new', methods=['POST'])
def create():
    name = request.form['name']
    constructor = request.form['constructor']
    points = request.form['points']
    wins = request.form['wins']
    podiums = request.form['podiums']
    driver = Driver(name, constructor, points, wins, podiums)
    drivers_repository.save(driver)
    return redirect('/drivers')

# edit 'drivers/<id>/edit
@drivers_blueprint.route('/drivers/<id>/edit')
def edit(id):
    driver = drivers_repository.select(id)
    return render_template('drivers/edit.html', driver=driver)

# update 'drivers/<id> method ['POST']
@drivers_blueprint.route('/drivers/<id>/edit', methods=['POST'])
def update(id):
    name = request.form['name']
    constructor = request.form['constructor']
    points = request.form['points']
    wins = request.form['wins']
    podiums = request.form['podiums']
    driver = Driver(name, constructor, points, wins, podiums, id)
    drivers_repository.update(driver)
    return redirect('/drivers')

# delete 'drivers/<id>/delete
@drivers_blueprint.route('/drivers/<id>/delete', methods=['POST'])
def delete(id):
    drivers_repository.delete(id)
    return redirect('/drivers')

# standings
@drivers_blueprint.route('/standings')
def standings():
    positions = range(1, 20)
    drivers = drivers_repository.select_all()
    drivers.sort(key=lambda x: x.points, reverse=True)
    return render_template('standings/index.html', positions=positions, drivers=drivers)