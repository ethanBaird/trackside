from db.run_sql import run_sql
from models.score import Score

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

def select_all():
    scores = []
    sql = """
        SELECT  * FROM scores
    """
    results = run_sql(sql)

    for row in results:
        score = Score(row['position'], row['points'], row['win'], row['podium'], row['id'])
        scores.append(score)
    return scores

def select(id):
    scores = []
    sql = """
        SELECT * FROM scores
        WHERE id = %s
    """
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        score = Score(result['position'], result['points'], result['win'], result['podium'], result['id'])
    return score

def delete_all():
    sql = """
        DELETE FROM scores
    """
    run_sql(sql)