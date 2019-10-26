from dataclasses import dataclass
import math

@dataclass
class Food:
    price: float
    energy: float
    protein: float
    carbs: float
    badFat: float

# absolute
priceConst = 2.0
badFatConst = 3.0

# relative
energyConst = 300.0
proteinConst = 7300.0
carbConst = 0.0

def sumFoods(foods, kgs):
    result = Food(0, 0, 0, 0, 0)

    result.price = sum([foods[i].price * kgs[i] for i in range(len(foods))])
    result.energy = sum([foods[i].energy * kgs[i] for i in range(len(foods))])
    result.protein = sum([foods[i].protein * kgs[i] for i in range(len(foods))])
    result.carbs = sum([foods[i].carbs * kgs[i] for i in range(len(foods))])
    result.badFat = sum([foods[i].badFat * kgs[i] for i in range(len(foods))])

    return result

def getFoodCost(foods, kgs, refFood):
    sumFood = sumFoods(foods, kgs)

    cost = 0

    cost += sumFood.price * priceConst
    cost += abs(1.0 - sumFood.energy / refFood.energy) * energyConst
    cost += max(0.0, 1.0 - sumFood.protein / refFood.protein) * proteinConst
    cost += abs(1.0 - sumFood.carbs / refFood.carbs) * carbConst
    cost += sumFood.badFat * badFatConst

    return cost
