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

driver1 = Driver("Charles Leclerc", 100, 6, 10)
driver_repository.save(driver1)

driver2 = Driver("Carlos Sainz", 92, 1, 7)
driver_repository.save(driver2)

race1 = Race('Abu Dhabi', 'Yas Marina')
races_repository.save(race1)
race2 = Race('Bahrain', 'Bahrain International Circuit')
races_repository.save(race2)

score1 = Score(1, 25, True, True)
breakpoint()
scores_repository.save(score1)

result1 = Result(score1.id, driver1.id, 'Ferarri', race1.id)
results_repository.save(result1)




pdb.set_trace()