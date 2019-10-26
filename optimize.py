from food import Food
from food import getFoodCost
from food import sumFoods
from descent import descent
import random

weekFood = Food(0.0, 7 * 2000, 7 * 100, 7 * 100, 0, 0)

banana = Food(2.60, 880, 11, 230, 1, 2.8)
potato = Food(2.00, 760, 20, 170, 0, 2.5)
rice = Food(2.50, 1300, 27, 280, 1, 0.8)
chicken = Food(11.00, 1640, 310, 0, 10, 3)
pork = Food(8.50, 2970, 257, 0, 77, 1.0)
beef = Food(14.00, 2500, 260, 0, 60, 1.0)
eggs = Food(0.50, 1550, 130, 11, 33, 1.0)
#oats = Food(4.00, 3890, 169, 663, 0, 1.0)
#yoghurt = Food(2.50, 130, 9, 10.5, 3.2, 4)

# с кисело мляко
oats = Food(8.50 / 3, (260 + 3890) / 3, (18 + 169) / 3, (21 + 663) / 3, 6.4 / 3, 3)

foods = [banana, potato, rice, chicken, pork, beef, eggs, oats]

def randomStart():
    result = []
    for i in range(len(foods)):
        result.append(random.random() * 3)

    return result

saturationConst = 150.0
def getSaturation(foodKgs):
    sum = 0
    for i in range(len(foods)):
        if foodKgs[i] > foods[i].saturation:
            sum += (foodKgs[i] / foods[i].saturation - 1.0) * saturationConst

    return sum

def costFunction(foodKgs):
    return getFoodCost(foods, foodKgs, weekFood) + getSaturation(foodKgs)

bestCost = 999999
bestVals = []
random.seed()

for i in range(1000):
    vals = randomStart()
    (result, cost) = descent(costFunction, vals, 2, 0.000001)

    if cost < bestCost:
        bestCost = cost
        bestVals = result
        #print(result, cost)
        print(["{:.2f}".format(x) for x in result], "{:.2f}".format(cost))

        foodRes = sumFoods(foods, result)
        print(foodRes)

print(weekFood)