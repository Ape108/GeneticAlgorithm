
class Chromosome:
    # we can use a couple different representations for features here,
    # real-valued is probably better but we can also use binary encoding
    # so that our operations are bit-flips
    def __init__(self):
        # Here we initialize the features
        # Randomly?
        # we are going to initialize the population P(0)
        # with random chromosomes so I think the randomizer 
        # can live in the init here
        pass

class Population:
    _population = []

    def __init__(self, size: int):
        # initializing a new population should
        # generate a desired number of chromosomes with random features
        pass

    def _fitness_evaluation(self) -> list[float]:
        # This should be run once to score each 
        # chromosome in the population,
        # returning a list where score[i] is the 
        # fitness of the i-th chromosome
        pass

    def _parent_selection(self) -> list[Chromosome]:
        # select which parents to breed
        pass

    def _crossover(self, parents: list[Chromosome]) -> list[Chromosome]:
        # conduct breeding with desired crossover method
        pass

    def _mutation(self, children: list[Chromosome], probability: float) -> list[Chromosome]:
        # run as a filter on the generated children 
        # with a certain probability (should be low, 0.01 - 0.1% chance)
        pass

    def _new_generation_formation(self, children: list[Chromosome]):
        # This should update _population with logic concerning
        # which parents are kept/thrown out. Keeping best parents
        # is an elitist filter. Discarding the oldest genes would be
        # a generational filter. The returned size of the population 
        # is a consideration, you don't want it to grow out of control
        # for computational reasons.
        pass

    def _termination_check(self):
        # decide when to stop evolving.
        # Maybe use a fixed number of generations from the beginning.
        pass

    def run(self):
        # Main runner to initiate evolution process.
        pass

    # helpers
    def display(self):
        # update this to print the population
        # in a way that makes sense given the context
        print(self._population)

    

def main():
    pass

if __name__ == "__main__":
    main()