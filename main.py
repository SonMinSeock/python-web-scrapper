player = {
    "name": "Son",
    "age": 26,
    "alive": True,
    "fav_food": ["🍕", "🍔"]
}

print(player.get("age"))
# print(player.get("fav_food"))
print(player["fav_food"])

player["xp"] = 1500
print(player)

player["fav_food"].append("🍜")
print(player["fav_food"])