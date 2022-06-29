
fruits = [
    ('apple', 285),
    ('orange', 160),
    ('grapes', 120),
    ('Pine', 85),
    ('Banana', 65),
    ('Gauva', 105),
    ('WaterMelon', 78),
    ("Straberry", 350)
]

print(f"fruits :{fruits}")
print("-" * 40)

price = ["fruit" for fruit in fruits]
print(f"price :{price}")
print("-" * 40)

price = [fruit for fruit in fruits]
print(f"price :{price}")
print("-" * 40)

price = [fruit[0] for fruit in fruits]
print(f"price :{price}")
print("-" * 40)

price = [fruit[1] for fruit in fruits]
print(f"price :{price}")
print("-" * 40)

price = [fruit[1] * 0.9 for fruit in fruits]
print(f"price :{price}")
print("-" * 40)

price = [fruit[1] * 0.75 for fruit in fruits]
print(f"price :{price}")
print("-" * 40)

price = [fruit for fruit in fruits if fruit[1] >= 100]
print(f"price :{price}")
print("-" * 40)

price = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits if fruit[1] >= 100]
print(f"price :{price}")
print("-" * 40)

setence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{setence}")
print("-" * 40)

words = [word for word in setence.split()]
print(f"words :{words}")

words = [(word, len(word)) for word in words if word != 'the']
print(f"words :{words}")
