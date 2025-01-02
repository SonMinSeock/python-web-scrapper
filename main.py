def make_juice(fruit):
    return f"{fruit}+🥤"

def add_ice(juice):
    return f"{juice}+🧊"

def add_sugar(iced_juice):
    return f"{iced_juice}+🍭"


juice = make_juice("🍎")
cold_juice = add_ice(juice)
final_juice = add_sugar(cold_juice)

print(final_juice)


def part(bolt):
    return f"{bolt}+🔩"

def raw(metal):
    return f"{metal}+🔨"

def parts(engine):
    return f"{engine}+🔥"

def build(car):
    return f"{car}+ =🏎️"

piece = part("⚙️")
side = raw(piece)
body = parts(side)
whole = build(body)

print(whole)