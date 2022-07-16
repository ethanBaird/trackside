from db.run_sql import run_sql

def save(score):
    sql = """
        INSERT INTO scores (position, points, win, podium)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """
    values = [score.position, score.points, score.win, score.podium]
    results = run_sql(sql, values)
    id = results[0]["id"]
    score.id = id

def delete_all():
    sql = """
        DELETE FROM scores
    """
    run_sql(sql)