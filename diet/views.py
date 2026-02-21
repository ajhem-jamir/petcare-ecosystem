from django.shortcuts import render, get_object_or_404
from pets.models import Pet
from .algorithm import generate_diet
from .models import DietRecommendation


def diet_recommendation_view(request, pet_id):

    # get pet from database
    pet = get_object_or_404(Pet, id=pet_id)

    # generate diet using AI algorithm
    diet_data = generate_diet(pet)

    # save recommendation to database
    recommendation = DietRecommendation.objects.create(
        pet=pet,
        calories=diet_data["calories"],
        protein=diet_data["protein"],
        fat=diet_data["fat"],
        carbs=diet_data["carbs"],
        recommendation=diet_data["recommendation"]
    )

    context = {
        "pet": pet,
        "diet": recommendation
    }

    return render(request, "diet/diet_result.html", context)