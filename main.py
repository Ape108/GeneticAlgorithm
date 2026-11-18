
import math


def decimal_to_binary(num: int):
    return bin(num)[2:]

def binary_to_decimal(bin: str):
    # assuming we chop off the base from the string literal
    return int(bin, 2)

class Chromosome:
    # we can use a couple different representations for features here,
    # real-valued is probably better but we can also use binary encoding
    # so that our operations are bit-flips
    def __init__(self, bin_feat_map):
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

def encode_features(feature_map):

    # Room (7) (technically 9 with room numbers)
    # Time (6)
    # Facilitator (10)
    
    for category in feature_map:
        num_bits = math.ceil(math.log2(len(category)))

        for x in category:
            # Convert the feature x into binary and append it to a list
            pass

    pass



def main():

    rooms = [
        ("Beach", "201", 18),
        ("Beach", "301", 25),
        ("Frank", "119", 95),
        ("Loft", "206", 55),
        ("Loft", "310", 48),
        ("James", "325", 110),
        ("Roman", "201", 40),
        ("Roman", "216", 80),
        ("Slater", "003", 32),
    ]

    times = [
        "10 AM",
        "11 AM",
        "12 PM",
        "1 PM",
        "2 PM",
        "3 PM",
    ]

    facilitators = [
        "Lock",
        "Glen",
        "Banks",
        "Richards",
        "Shaw",
        "Singer",
        "Uther",
        "Tyler",
        "Numen",
        "Zeldin",
    ]

    feature_map = {
        "room": rooms,
        "time": times,
        "facilitator": facilitators,
    }



if __name__ == "__main__":
    main()