import statistics
import math
from collections import Counter

data = [73, 44, 92, 296, 2, 7, 9, 32, 11, 19, 102, 7, 5, 65, 296]


def variance(x):
    sigma_n = 0
    for i in x:
        xi_min_xbar = i - statistics.mean(x)
        xi_min_xbar_kuadrat = xi_min_xbar**2
        sigma_n = sigma_n + xi_min_xbar_kuadrat

    hasil = sigma_n / (len(x) - 1)
    return hasil


def stdevs(x):
    hasil = math.sqrt(variance(x))
    return hasil


def modus(x):
    count_values = Counter(x)
    hasil = max(count_values, key=count_values.get)
    return hasil


def z_score(x):
    hasil = []
    for i in x:
        z = i - statistics.mean(x) / stdevs(x)
        hasil.append(z)
    return hasil


print("Modus: ", modus(data))
print("Variance: ", variance(data))
print("Standard Deviasi: ", stdevs(data))
print("Z_Score: ", z_score(data))
