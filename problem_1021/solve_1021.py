value = float(input())
cents = int(round(value * 100))

# Define note values in cents
notes = [10000, 5000, 2000, 1000, 500, 200]
note_names = ["100.00", "50.00", "20.00", "10.00", "5.00", "2.00"]

# Define coin values in cents
coins = [100, 50, 25, 10, 5, 1]
coin_names = ["1.00", "0.50", "0.25", "0.10", "0.05", "0.01"]

print("NOTAS:")
for i in range(len(notes)):
    count = cents // notes[i]
    print(f"{count} nota(s) de R$ {note_names[i]}")
    cents %= notes[i]

print("MOEDAS:")
for i in range(len(coins)):
    count = cents // coins[i]
    print(f"{count} moeda(s) de R$ {coin_names[i]}")
    cents %= coins[i]