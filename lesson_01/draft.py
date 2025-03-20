"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distace = 1600
fuel_consumption_per_100_km = 9
fuel_tank_capacity = 48
total_fuel = (1600 / 100) * 9
fuel_top_ups = total_fuel / fuel_tank_capacity
print(f"family will spend {total_fuel} l of petrol")
print(f"Family need to top up petrol {fuel_top_ups} times")
