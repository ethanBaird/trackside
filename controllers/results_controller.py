from flask import Flask, Blueprint, redirect, render_template, request

import repositories.results_repository as results_repository
import repositories.scores_repository as scores_repository
import repositories.drivers_repository as drivers_repository
import repositories.races_repository as races_repository

results_blueprint = Blueprint("results", __name__)

#index
@results_blueprint.route('/races/results/<race_id>')
def race_results(race_id):
    results = results_repository.select(race_id)
    for result in results:
        result.score = scores_repository.select(result.score)
        result.driver = drivers_repository.select(result.driver)
        result.race = races_repository.select(result.race)
    return render_template('races/results/index.html', results=results)