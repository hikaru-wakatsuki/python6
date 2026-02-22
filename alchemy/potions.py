def healing_potion() -> str:
    from .elements import create_fire, create_water
    fire_result: str = create_fire()
    water_result: str = create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion() -> str:
    from .elements import create_fire, create_earth
    fire_result: str = create_fire()
    earth_result: str = create_earth()
    return f"Strength potion brewed with {fire_result} and {earth_result}"


def invisibility_potion() -> str:
    from .elements import create_water, create_air
    water_result: str = create_water()
    air_result: str = create_air()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion() -> str:
    from .elements import create_fire, create_water, create_earth, create_air
    fire_result: str = create_fire()
    water_result: str = create_water()
    earth_result: str = create_earth()
    air_result: str = create_air()
    return (f"Wisdom potion brewed with all elements: "
            f"{fire_result}, {water_result}, {earth_result}, {air_result}")
