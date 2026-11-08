
# Import meal function I'm testing
from calculations import calculate_meal_totals


# Test 1: Origional meal selections
def test_meal_totals():
    # Meal name and ID pairs
    meal_options = [
        (1, "Chicken"),
        (2, "Beef"),
        (3, "Vegetarian")
    ]
    # simulated pull of selected meal ID's from database
    meal_selections = [
        (1,),
        (3,),
        (1,),
        (1,)
    ]
    # Ensure calculation is correct (pass or fail)
    totals = calculate_meal_totals(meal_options, meal_selections) # calling the function to calculate meal totals
    # Ensure the calculated totals match the expected values
    assert totals["Chicken"] == 3
    assert totals["Beef"] == 0
    assert totals["Vegetarian"] == 1


# Test 2: No saved meal selections (Empty)
def test_empty_meal_selections():
    # Use original meal options again
    meal_options = [
        (1, "Chicken"),
        (2, "Beef"),
        (3, "Vegetarian")
    ]
    # Simulate empty meal selections from database
    meal_selections = []
    # Ensure calculation is correct (pass or fail)
    totals = calculate_meal_totals(meal_options, meal_selections) # calling the function to calculate meal totals
    # Ensure all meal totals are zero when no selections are made
    assert totals["Chicken"] == 0
    assert totals["Beef"] == 0
    assert totals["Vegetarian"] == 0


# Test 3: Meal totals change after new selections
def test_updated_meal_totals():
    # Expanded meal options
    meal_options = [
        (1, "Chicken"),
        (2, "Beef"),
        (3, "Vegetarian"),
        (4, "Pasta"),
        (5, "Salad"),
        (6, "Nothing"),
        (7, "Steak"),
        (8, "Fish")
    ]
    # Simulate a lot of saved meal selections
    meal_selections = [
        (1,),
        (3,),
        (4,),
        (4,),
        (1,),
        (7,),
        (8,),
        (7,),
        (1,),
        (3,),
        (4,),
        (4,),
        (1,),
        (7,),
        (8,),
        (7,),        
    ]
    # Ensure calculation is correct (pass or fail)
    original_totals = calculate_meal_totals(meal_options, meal_selections) # calling the function to calculate meal totals
    # Ensure the calculated totals match the expected values
    assert original_totals["Chicken"] == 4
    assert original_totals["Beef"] == 0
    assert original_totals["Vegetarian"] == 2
    assert original_totals["Pasta"] == 4
    assert original_totals["Salad"] == 0
    assert original_totals["Nothing"] == 0
    assert original_totals["Steak"] == 4
    assert original_totals["Fish"] == 2

    # Simulate two additional saved selections
    meal_selections.append((1,)) # append a new meal selection
    meal_selections.append((2,)) # append a new meal selection

    updated_totals = calculate_meal_totals(meal_options, meal_selections) # calling the function to calculate updated meal totals
    # Ensure the updated totals match the expected values
    assert updated_totals["Chicken"] == 5
    assert updated_totals["Beef"] == 1
    assert updated_totals["Vegetarian"] == 2
    assert updated_totals["Pasta"] == 4
    assert updated_totals["Salad"] == 0
    assert updated_totals["Nothing"] == 0
    assert updated_totals["Steak"] == 4
    assert updated_totals["Fish"] == 2
