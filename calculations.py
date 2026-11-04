

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
