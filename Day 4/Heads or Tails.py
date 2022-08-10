import random
	 
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

random_size = random.randint(0,1)
if random_size ==1:
    print("Heads")
else:
    print("Tails")