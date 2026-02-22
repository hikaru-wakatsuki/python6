def validate_ingredients(ingredients: str) -> str:
    valid_ingredients: list[str] = [
        "fire", "water", "earth", "air"
    ]
    for word in valid_ingredients:
        if word in ingredients:
            return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
