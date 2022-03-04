import random
from warranty import InsuranceRow

# Points (1-10) for each data range
POINTS_MILEAGE = [*range(90000, 0, -10000)]
POINTS_BRAND_RELIABILITY = [*range(2, 11)]
POINTS_YEAR = [*range(2004, 2022, 2)]
POINTS_USED_FOR = [*range(18, 0, -2)]
POINTS_ACCIDENTS = [*range(8, -1, -1)]
POINTS_SERVICE_FREQUENCY = [*range(6, 15, 1)]

RANGE_TEEN = [*range(16, 20, 1)]
RANGE_YOUNG_ADULT = [*range(20, 26, 1)]
RANGE_ADULT = [*range(26, 41, 1)]
RANGE_MIDDLE_AGE = [*range(41, 60, 1)]
RANGE_OLDER = [*range(60, 80, 1)]
POINTS_OWNER_AGE = [(RANGE_TEEN, 1), (RANGE_OLDER, 3), (RANGE_YOUNG_ADULT, 5), (RANGE_MIDDLE_AGE, 7), (RANGE_ADULT, 10)]


def calculate_points(row):
    total_points = 0

    points_mileage = get_points_decreasing(POINTS_MILEAGE, row.get_mileage())
    total_points += points_mileage
    row.set_points_mileage(points_mileage)

    points_brand_reliability = get_points_increasing(POINTS_BRAND_RELIABILITY, row.get_brand_reliability())
    total_points += points_brand_reliability
    row.set_points_brand_reliability(points_brand_reliability)

    points_year = get_points_increasing(POINTS_YEAR, row.get_year())
    total_points += points_year
    row.set_points_year(points_year)

    points_used_for = get_points_decreasing(POINTS_USED_FOR, row.get_used_for())
    total_points += points_used_for
    row.set_points_used_for(points_used_for)

    points_accidents = get_points_decreasing(POINTS_ACCIDENTS, row.get_accidents())
    total_points += points_accidents
    row.set_points_accidents(points_accidents)

    points_service_frequency = get_points_increasing(POINTS_SERVICE_FREQUENCY, row.get_service_frequency())
    total_points += points_service_frequency
    row.set_points_service_frequency(points_service_frequency)

    points_owner_age = get_points_owner_age(POINTS_OWNER_AGE, row.get_owner_age())
    total_points += points_owner_age
    row.set_points_owner_age(points_owner_age)

    row.set_total_points(total_points)
    return row


def generate_insurance_months(new_row):
    total_points = new_row.get_total_points()
    new_row.set_insurance_months(total_points - 7)
    return new_row


def generate_row(car_id):
    random.seed(int(car_id))
    year = random.randrange(2002, 2022)
    age = 2022 - year
    used_for = random.randrange(age // 2, age + 1)
    mileage = random.randrange(0, age * 8000)
    brand_reliability = random.randrange(1, 11)
    accidents = random.randrange(0, 10)
    service_frequency = random.randrange(6, 15)
    owner_age = random.randrange(16, 100)

    new_row = InsuranceRow.InsuranceRow(mileage, brand_reliability, year, used_for, accidents, service_frequency, owner_age)
    new_row = calculate_points(new_row)
    new_row = generate_insurance_months(new_row)

    return new_row


def get_points_owner_age(points_owner_age, owner_age):
    for age_range, points in points_owner_age:
        if owner_age in age_range:
            return points
    return 1


def get_points_increasing(points_range, key):
    for index, value in enumerate(points_range):
        if key < value:
            return index + 1
    return 10


def get_points_decreasing(points_range, key):
    for index, value in enumerate(points_range):
        if key > value:
            return index + 1
    return 1


def get_warranty_offer(car):
    row = generate_row(car["car_id"])

    months = row.get_insurance_months()
    cost = 0.045 * int(car["price"])
    formatted_cost = "{:.2f}".format(cost)

    offer = "Warranty offer: " + str(months) + " months long for £" + str(formatted_cost)
    return offer
