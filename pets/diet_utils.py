"""
Advanced Diet Calculation Utilities for Pets
Uses proper veterinary formulas and decision-tree AI logic
"""

def calculate_rer(weight):
    """
    Calculate Resting Energy Requirement (RER)
    Formula: RER = 70 × (body weight in kg)^0.75
    This is the standard veterinary formula
    """
    return 70 * (float(weight) ** 0.75)

def calculate_mer(rer, activity_level, life_stage='adult', health_status='healthy'):
    """
    Calculate Maintenance Energy Requirement (MER) based on multiple factors
    Uses decision-tree logic for accurate calculations
    
    Args:
        rer: Resting Energy Requirement
        activity_level: 'low', 'medium', 'high'
        life_stage: 'puppy', 'kitten', 'adult', 'senior'
        health_status: 'healthy', 'overweight', 'underweight', 'pregnant', 'lactating'
    """
    # Base multipliers by activity level
    activity_multipliers = {
        'low': 1.2,      # Sedentary/indoor pets
        'medium': 1.4,   # Normal activity
        'high': 1.8      # Very active/working animals
    }
    
    # Life stage adjustments
    life_stage_multipliers = {
        'puppy': 2.0,    # Growing puppies need more
        'kitten': 2.5,   # Growing kittens need even more
        'adult': 1.0,    # Standard
        'senior': 0.8    # Older pets need less
    }
    
    # Health status adjustments
    health_multipliers = {
        'healthy': 1.0,
        'overweight': 0.8,    # Weight loss
        'underweight': 1.2,   # Weight gain
        'pregnant': 1.5,      # Pregnancy
        'lactating': 2.0      # Nursing mothers
    }
    
    base_mer = rer * activity_multipliers.get(activity_level, 1.4)
    base_mer *= life_stage_multipliers.get(life_stage, 1.0)
    base_mer *= health_multipliers.get(health_status, 1.0)
    
    return base_mer

def get_species_specific_adjustments(species, weight):
    """
    Decision-tree logic for species-specific dietary needs
    Returns adjustments for protein, fat, and carbs percentages
    """
    species_lower = species.lower()
    
    # Dogs
    if 'dog' in species_lower:
        if weight < 10:  # Small dogs
            return {'protein': 0.28, 'fat': 0.17, 'carbs': 0.55, 'notes': 'Small breed formula'}
        elif weight > 30:  # Large dogs
            return {'protein': 0.25, 'fat': 0.12, 'carbs': 0.63, 'notes': 'Large breed formula'}
        else:  # Medium dogs
            return {'protein': 0.26, 'fat': 0.15, 'carbs': 0.59, 'notes': 'Medium breed formula'}
    
    # Cats
    elif 'cat' in species_lower:
        return {'protein': 0.35, 'fat': 0.20, 'carbs': 0.45, 'notes': 'Obligate carnivore - high protein'}
    
    # Birds
    elif 'bird' in species_lower:
        return {'protein': 0.15, 'fat': 0.05, 'carbs': 0.80, 'notes': 'Seed-based diet with supplements'}
    
    # Rabbits
    elif 'rabbit' in species_lower:
        return {'protein': 0.14, 'fat': 0.03, 'carbs': 0.83, 'notes': 'High fiber herbivore diet'}
    
    # Fish
    elif 'fish' in species_lower:
        return {'protein': 0.40, 'fat': 0.10, 'carbs': 0.50, 'notes': 'High protein aquatic diet'}
    
    # Hamsters/Guinea Pigs/Small mammals
    elif any(x in species_lower for x in ['hamster', 'guinea', 'gerbil', 'mouse', 'rat']):
        return {'protein': 0.16, 'fat': 0.04, 'carbs': 0.80, 'notes': 'Small mammal omnivore diet'}
    
    # Reptiles
    elif any(x in species_lower for x in ['lizard', 'snake', 'turtle', 'tortoise', 'gecko', 'iguana']):
        return {'protein': 0.30, 'fat': 0.10, 'carbs': 0.60, 'notes': 'Reptile species-specific diet'}
    
    # Ferrets
    elif 'ferret' in species_lower:
        return {'protein': 0.38, 'fat': 0.20, 'carbs': 0.42, 'notes': 'Obligate carnivore - high protein/fat'}
    
    # Default for unknown species
    else:
        return {'protein': 0.25, 'fat': 0.15, 'carbs': 0.60, 'notes': 'General balanced diet'}

def get_weight_based_recommendations(species, weight, age_months):
    """
    Decision-tree for weight and age-based recommendations
    """
    recommendations = []
    species_lower = species.lower()
    
    # Dogs
    if 'dog' in species_lower:
        if weight < 5:
            recommendations.append("Very small breed - feed small, frequent meals (3-4 times daily)")
        elif weight > 40:
            recommendations.append("Large breed - monitor for joint health, consider joint supplements")
        
        if age_months < 12:
            recommendations.append("Puppy - use puppy-specific food for proper growth")
        elif age_months > 84:  # 7 years
            recommendations.append("Senior dog - consider senior formula with joint support")
    
    # Cats
    elif 'cat' in species_lower:
        if weight < 3:
            recommendations.append("Small cat - ensure adequate protein intake")
        elif weight > 6:
            recommendations.append("Large cat - monitor weight, consider weight management formula")
        
        if age_months < 12:
            recommendations.append("Kitten - use kitten formula for growth")
        elif age_months > 84:
            recommendations.append("Senior cat - consider senior formula with kidney support")
    
    # General recommendations
    if weight < 2:
        recommendations.append("Very small pet - consult vet for specialized feeding plan")
    
    return recommendations

def generate_diet(pet):
    """
    Generate comprehensive diet recommendation using veterinary formulas
    and decision-tree AI logic
    
    Returns dict with calories, protein, fat, carbs, and detailed recommendations
    """
    weight = float(pet.weight)
    activity = pet.activity_level.lower()
    age_months = pet.age_months
    species = pet.get_species_name()
    
    # Determine life stage
    if age_months < 12:
        life_stage = 'puppy' if 'dog' in species.lower() else 'kitten' if 'cat' in species.lower() else 'adult'
    elif age_months > 84:
        life_stage = 'senior'
    else:
        life_stage = 'adult'
    
    # Calculate energy requirements
    rer = calculate_rer(weight)
    mer = calculate_mer(rer, activity, life_stage)
    
    # Get species-specific macronutrient distribution
    species_adjustments = get_species_specific_adjustments(species, weight)
    
    # Calculate macronutrients in kcal
    protein_kcal = mer * species_adjustments['protein']
    fat_kcal = mer * species_adjustments['fat']
    carbs_kcal = mer * species_adjustments['carbs']
    
    # Convert to grams (protein: 4 kcal/g, fat: 9 kcal/g, carbs: 4 kcal/g)
    protein_grams = protein_kcal / 4
    fat_grams = fat_kcal / 9
    carbs_grams = carbs_kcal / 4
    
    # Build comprehensive recommendations
    recommendations = []
    
    # Add species-specific note
    recommendations.append(species_adjustments['notes'])
    
    # Add weight-based recommendations
    weight_recs = get_weight_based_recommendations(species, weight, age_months)
    recommendations.extend(weight_recs)
    
    # Add activity-based recommendations
    if activity == 'high':
        recommendations.append("High activity level - ensure adequate hydration and recovery time")
    elif activity == 'low':
        recommendations.append("Low activity - monitor weight to prevent obesity")
    
    # Add life stage recommendations
    if life_stage == 'senior':
        recommendations.append("Senior pet - consider supplements for joint and organ health")
    elif life_stage in ['puppy', 'kitten']:
        recommendations.append("Growing pet - ensure proper calcium and phosphorus balance")
    
    # General recommendations
    recommendations.append("Always provide fresh, clean water")
    recommendations.append("Divide daily food into 2-3 meals for better digestion")
    recommendations.append("Consult your veterinarian for personalized dietary advice")
    
    return {
        "calories": round(mer, 2),
        "protein": round(protein_kcal, 2),
        "fat": round(fat_kcal, 2),
        "carbs": round(carbs_kcal, 2),
        "protein_grams": round(protein_grams, 2),
        "fat_grams": round(fat_grams, 2),
        "carbs_grams": round(carbs_grams, 2),
        "rer": round(rer, 2),
        "life_stage": life_stage,
        "species": species,
        "recommendation": "\n".join(f"• {rec}" for rec in recommendations)
    }
