from django.db import models
from pets.models import Pet

class DietRecommendation(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    recommendation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diet for {self.pet.name}"