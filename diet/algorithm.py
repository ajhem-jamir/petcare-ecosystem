import math

def calculate_rer(weight):
    return 70 * (weight ** 0.75)

def calculate_mer(rer, activity_level):
    if activity_level == "low":
        return rer * 1.2
    elif activity_level == "high":
        return rer * 1.8
    else:
        return rer * 1.4

def generate_diet(pet):

    weight = pet.weight
    activity = pet.activity_level.lower()

    rer = calculate_rer(weight)
    mer = calculate_mer(rer, activity)

    protein = mer * 0.30
    fat = mer * 0.20
    carbs = mer * 0.50

    recommendation = ""

    if weight > 30:
        recommendation = "Low fat diet recommended"
    elif weight < 10:
        recommendation = "High protein diet recommended"
    else:
        recommendation = "Balanced diet recommended"

    return {
        "calories": mer,
        "protein": protein,
        "fat": fat,
        "carbs": carbs,
        "recommendation": recommendation
    }