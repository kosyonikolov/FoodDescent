import sys
import math

derivative_step = 0.001

def f(vec):
    x = vec[0]

    sigma = 1
    mean = 3.5

    x -= mean

    return -1 * math.exp(-sigma * x**2)

def derivative(function, args, dIdx):
    low = args[:]
    high = args[:]
    low[dIdx] -= derivative_step
    high[dIdx] += derivative_step

    diff = function(high) - function(low)
    return diff / (2.0 * derivative_step)

def gradient(function, args):
    result = []

    for i in range(len(args)):
        d = derivative(function, args, i)
        result.append(d)

    return result

def vectorDiff(a, b, scale):
    return [a[i] - b[i] * scale for i in range(len(a))]

def scalarProduct(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])

def descent(function, initialArgs, initialStep, minStep):
    bestVal = function(initialArgs)
    args = initialArgs[:]
    step = initialStep

    successCount = 0
    stepIncreaseThr = 5

    while step >= minStep:
        g = gradient(function, args)
        oldVal = bestVal

        #print(args, g, step, function(args), bestVal)
        while True:
            candArgs = vectorDiff(args, g, step)
            candVal = function(candArgs)

            if candVal < bestVal:
                bestVal = candVal
                args = candArgs[:]
                successCount += 1
                break
            else:
                successCount = 0
                step *= 0.5 # jumped the local min

            if step < minStep:
                break

        gradientScalar = scalarProduct(g, g)

        # Armijo rule
        c1 = 0.001
        if bestVal > oldVal + c1 * gradientScalar:
            break

        if successCount >= stepIncreaseThr:
            step *= 1.8
            successCount = 0

    return (args, bestVal)


g = gradient(f, [5, -3])
print(g)

result = descent(f, [9.0, 3, 100], 0.5, 0.001)
print(result)

print("Hello python")