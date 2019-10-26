from food import Food
from food import getFoodCost
from food import sumFoods
from descent import descent
import random

weekFood = Food(0.0, 7 * 2000, 7 * 100, 7 * 400, 0)

banana = Food(2.60, 880, 11, 230, 1)
potato = Food(2.00, 760, 20, 170, 0)
rice = Food(5.00, 1300, 27, 280, 1)
chicken = Food(11.00, 1640, 310, 0, 10)
pork = Food(8.50, 2970, 257, 0, 77)
beef = Food(14.00, 2500, 260, 0, 60)
eggs = Food(0.50, 1550, 130, 11, 33)

foods = [banana, potato, rice, chicken, pork, beef, eggs]

def randomStart():
    result = []
    for i in range(len(foods)):
        result.append(random.random() * 7)

    return result

def costFunction(foodKgs):
    return getFoodCost(foods, foodKgs, weekFood)

random.seed()
vals = randomStart()

(result, cost) = descent(costFunction, vals, 1, 0.01)

print(result, cost)

foodRes = sumFoods(foods, result)
print(foodRes)
print(weekFood)