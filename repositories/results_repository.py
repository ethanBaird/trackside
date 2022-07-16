from db.run_sql import run_sql

def save(result):
    sql = """
        INSERT INTO results (score_id, driver_id, constructor, race_id)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """
    values = [result. score_id, result.driver_id, result.constructor, result.race_id]
    results = run_sql(sql, values)
    breakpoint()
    id = results[0]["id"]
    result.id = id

def delete_all():
    sql = """
        DELETE FROM results
    """
    run_sql(sql)