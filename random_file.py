# The Random Module
import random
# Print random integer
# print(random.randint(0, 5))

# Print random float
# print(random.random() * 100)

# Print random string
# r = random.choice(["Python", "PHP", "Java", "Ruby"])
# print(r)
# Print a random data type
# r1 = ["string", 123, 5.5, True]
# rnd = random.choice(r1)
# print(rnd)

# list = ["string", "2nd_string", 4587, 2.3, False, 879, True]
# random.shuffle(list)
# print(list)

# Shuffle on a list of numbers
# list = [[i] for i in range(20)]
# random.shuffle(list)
# print(list)

# The randrange() method
for i in range(10):
    print(random.randrange(0, 200))
