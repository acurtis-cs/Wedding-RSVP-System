

# Calculate overall RSVP attendance totals
def calculate_rsvp_totals(guests):
    # Starting counts and utilizing dictionary to store totals
    totals = {
        "total_invited": 0,
        "attending": 0,
        "not_attending": 0,
        "not_responded": 0
    }
    # Count every invited guest and categorize them based on their RSVP status
    for guest in guests:
        status = guest[0]

        totals["total_invited"] += 1

        if status == "Attending":
            totals["attending"] += 1

        elif status == "Not Attending":
            totals["not_attending"] += 1

        elif status == "Not Responded":
            totals["not_responded"] += 1
    # Return all four totals
    return totals


# Calculate total selections for each meal
def calculate_meal_totals(meal_options, meal_selections):
    # Creating dictionary variable to store meal names
    meal_names = {}
    # Creating dictionary variable to store meal totals
    totals = {}

    # Match meal IDs to names and initialize totals
    for meal in meal_options:
        meal_id = meal[0]
        meal_name = meal[1]
        # Store meal name and initialize its total to zero
        meal_names[meal_id] = meal_name
        totals[meal_name] = 0

    # Count saved meal selections
    for selection in meal_selections:
        # Get the meal ID from the selection
        meal_id = selection[0]
        # Get the meal name from the meal ID
        meal_name = meal_names[meal_id]
        # Increase the total for the selected meal
        totals[meal_name] += 1

    return totals


