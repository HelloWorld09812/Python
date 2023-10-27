mass, height = float(input()), float(input())

body_mass_index = mass / (height * height)

if body_mass_index <= 25 and body_mass_index >= 18.5:
    print("Оптимальная масса")
elif body_mass_index < 18.5:
    print("Недостаточная масса")
else:
    print("Избыточная масса")

#a
