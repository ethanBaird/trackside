import pdb
from models.driver import Driver
from models.race import Race
from models.result import Result
from models.score import Score
import repositories.drivers_repository as driver_repository
import repositories.races_repository as races_repository
import repositories.scores_repository as scores_repository
import repositories.results_repository as results_repository

results_repository.delete_all()
scores_repository.delete_all()
driver_repository.delete_all()
races_repository.delete_all()

score1 = Score(1, 25, True, True)
scores_repository.save(score1)
score2 = Score(2, 19, False, True)
scores_repository.save(score2)
score3 = Score(3, 15, False, True)
scores_repository.save(score3)
score4 = Score(4, 12, False, False)
scores_repository.save(score4)
score5 = Score(5, 10, False, False)
scores_repository.save(score5)
score6 = Score(6, 8, False, False)
scores_repository.save(score6)
score7 = Score(7, 6, False, False)
scores_repository.save(score7)
score8 = Score(8, 4, False, False)
scores_repository.save(score8)
score9 = Score(9, 2, False, False)
scores_repository.save(score9)
score10 = Score(10, 1, False, False)
scores_repository.save(score10)

driver1 = Driver("Charles Leclerc", 10, 0, 0)
driver_repository.save(driver1)
driver2 = Driver("Carlos Sainz", 15, 0, 0)
driver_repository.save(driver2)

race1 = Race('Abu Dhabi', 'Yas Marina')
races_repository.save(race1)
result1 = Result(score1, driver1, 'Ferarri', race1)
results_repository.save(result1)
result2 = Result(score2, driver2, 'Ferarri', race1)
results_repository.save(result2)


race2 = Race('Bahrain', 'Bahrain International Circuit')
races_repository.save(race2)
result1 = Result(score1, driver1, 'Ferarri', race2)
results_repository.save(result1)
result2 = Result(score2, driver2, 'Ferarri', race2)
results_repository.save(result2)





pdb.set_trace()