import pdb
from models.driver import Driver
from models.race import Race
from models.result import Result
from models.score import Score
import repositories.drivers_repository as driver_repository
import repositories.races_repository as races_repository
import repositories.scores_repository as scores_repository
import repositories.results_repository as results_repository

driver_repository.delete_all()
races_repository.delete_all()
results_repository.delete_all()
scores_repository.delete_all()

score1 = Score(1, 25, True, True)
scores_repository.save(score1)
score2 = Score(2, 19, False, True)
scores_repository.save(score2)
score3 = Score(3, 15, False, True)
scores_repository.save(score1)
score4 = Score(2, 12, False, False)
scores_repository.save(score2)
score5 = Score(1, 10, False, False)
scores_repository.save(score1)
score6 = Score(2, 8, False, False)
scores_repository.save(score2)
score7 = Score(1, 6, False, False)
scores_repository.save(score1)
score8 = Score(2, 4, False, False)
scores_repository.save(score2)
score9 = Score(1, 2, False, False)
scores_repository.save(score1)
score10 = Score(2, 1, False, False)
scores_repository.save(score2)

driver1 = Driver("Charles Leclerc", 0, 0, 0)
driver_repository.save(driver1)
driver2 = Driver("Carlos Sainz", 0, 0, 0)
driver_repository.save(driver2)

race1 = Race('Abu Dhabi', 'Yas Marina')
races_repository.save(race1)
result1 = Result(score1.id, driver1.id, 'Ferarri', race1.id)
results_repository.save(result1)
result2 = Result(score2.id, driver2.id, 'Ferarri', race1.id)
results_repository.save(result2)


race2 = Race('Bahrain', 'Bahrain International Circuit')
races_repository.save(race2)
result1 = Result(score1.id, driver1.id, 'Ferarri', race1.id)
results_repository.save(result1)
result2 = Result(score2.id, driver2.id, 'Ferarri', race1.id)
results_repository.save(result2)





pdb.set_trace()