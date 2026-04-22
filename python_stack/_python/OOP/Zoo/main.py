from Zoo import Zoo
from Lion import Lion
from Monkey import Monkey
from Bear import Bear

zoo1 = Zoo("Our Zoo")

zoo1.add_animal(Lion("Nala", 5))
zoo1.add_animal(Lion("Simba", 4))
zoo1.add_animal(Monkey("George", 3))
zoo1.add_animal(Bear("Baloo", 7))

zoo1.feed_all()
zoo1.print_all_info()
