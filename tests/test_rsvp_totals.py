
# Import our calculation function
from calculations import calculate_rsvp_totals


# TEST 1: Check normal RSVP totals
def test_rsvp_totals():

    # Simulate guest RSVP statuses
    guests = [
        ("Attending",),
        ("Attending",),
        ("Not Attending",),
        ("Not Responded",),
        ("Not Responded",)
    ]

    totals = calculate_rsvp_totals(guests)
    # Note assert verifies the expected values (provides pass/fail feedback)
    assert totals["total_invited"] == 5
    assert totals["attending"] == 2
    assert totals["not_attending"] == 1
    assert totals["not_responded"] == 2


# TEST2: Check when there are no guests
def test_empty_guest_list():

    guests = []

    totals = calculate_rsvp_totals(guests)

    assert totals["total_invited"] == 0
    assert totals["attending"] == 0
    assert totals["not_attending"] == 0
    assert totals["not_responded"] == 0


# TEST 3: Check calculations with RSVP statuses change
def test_updated_rsvp_totals():

    # Original RSVP information
    guests = [
        ("Attending",),
        ("Not Responded",)
    ]

    totals = calculate_rsvp_totals(guests)

    assert totals["attending"] == 1
    assert totals["not_responded"] == 1

    # Simulate the second guest changing their RSVP
    guests = [
        ("Attending",),
        ("Attending",)
    ]

    totals = calculate_rsvp_totals(guests)

    assert totals["attending"] == 2
    assert totals["not_responded"] == 0
