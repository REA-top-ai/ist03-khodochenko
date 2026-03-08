#1
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors["pantry"] = 22
print(sensors)
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
print(num_cameras)
#2
translations = {"mountain": "orod","bread": "bass","friend": "mellon","horse": "roch"}
print(translations)
#3
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)
#4
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids["theLooper"] = 138475
user_ids["stringQueen"] = 85739
print(user_ids)
#5
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)
#6
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}
print(drinks_to_caffeine)