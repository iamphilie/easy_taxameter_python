#Taxirechner für Hamburg. Quelle: https://www.hamburg.de/taxi/2936756/taxi-fahrpreise/
start_price = 3.90
km = int(input("Bitte geben Sie ihre gewünschten Kilometer ein:"))
if km < 4:
    cost = 2.6
if km > 4 and km < 9:
    cost = 2.40
else:
    cost = 1.7
total_expenses = start_price + cost * km
print("Deine Taxifahrt in Hamburg kostet", total_expenses, "Euro")