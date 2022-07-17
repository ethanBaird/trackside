from unittest import result
from db.run_sql import run_sql
from models.result import Result

def save(result):
    sql = """
        INSERT INTO results (score_id, driver_id, constructor, race_id)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """
    values = [result. score_id, result.driver_id, result.constructor, result.race_id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    result.id = id

def select(race_id):
    race_results = []
    sql = """
        SELECT * FROM results
        WHERE race_id = %s
    """
    values = [race_id]
    results = run_sql(sql, values)

    for row in results:
        result = Result(row['score_id'], row['driver_id'], row['constructor'], row['id'])
        race_results.append(result)
    return race_results


def delete_all():
    sql = """
        DELETE FROM results
    """
    run_sql(sql)