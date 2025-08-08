import random

# CONSTANTS (weights in grams) 
GOAL = 50000
NUM_RATS = 20  # number of adult breeding rats in each generation
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS = 0.01
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 500

def populate(num_rats,min_wt,max_wt,mode_wt):
    list =[]
    for i in range(num_rats):
        list.append(int(random.triangular(min_wt,max_wt,mode_wt)))
    return list

def fitness(population,goal):
    average = sum(population)/len(population)
    score = average/goal
    return (score)

def select(po)

def main():
    rat_init = populate(NUM_RATS,INITIAL_MIN_WT,INITIAL_MAX_WT,INITIAL_MODE_WT)
    print(rat_init)

    fitness_init = fitness(rat_init,GOAL)
    print(fitness_init) 





    print()


if __name__=="__main__":
    main()