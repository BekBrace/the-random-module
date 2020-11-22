# Flip a virtual coin 10,000 times and count how many times it will land on heads or tails
import random
output = {"Heads": 0, "Tails": 0}
coin = list(output.keys())
# print(coin)
for i in range(10000):
    output[random.choice(coin)] += 1
print("Heads:", output["Heads"])
print("Tails:", output["Tails"])
