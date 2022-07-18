from lib2to3.pgen2 import driver
from unittest import result
from db.run_sql import run_sql
from models.result import Result

import repositories.scores_repository as scores_repository
import repositories.drivers_repository as drivers_repository
import repositories.races_repository as races_repository

def save(result):
    sql = """
        INSERT INTO results (score_id, driver_id, constructor, race_id)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """
    values = [result.score.id, result.driver.id, result.constructor, result.race.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    result.id = id

def select_all():
    race_results = []

    sql = "SELECT * FROM results"
    results = run_sql(sql)

    for row in results:
        race = races_repository.select(row['race_id'])
        driver = drivers_repository.select(row['driver_id'])
        score = scores_repository.select(row['score_id'])
        result = Result(score, driver, row['constructor'], race, row['id'])
        race_results.append(result)
    return race_results

def select(race_id):
    race_results = []
    sql = """
        SELECT * FROM results
        WHERE race_id = %s
    """
    values = [race_id]
    results = run_sql(sql, values)

    for row in results:
        race = races_repository.select(row['race_id'])
        driver = drivers_repository.select(row['driver_id'])
        score = scores_repository.select(row['score_id'])
        result = Result(score, driver, row['constructor'], race, row['id'])
        race_results.append(result)
    return race_results


def delete_all():
    sql = """
        DELETE FROM results
    """
    run_sql(sql)