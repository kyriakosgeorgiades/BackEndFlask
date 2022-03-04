class InsuranceRow:
    def __init__(self, mileage, brand_reliability, year, used_for, accidents, service_frequency, owner_age):
        self._mileage = mileage
        self._points_mileage = 0

        self._brand_reliability = brand_reliability
        self._points_brand_reliability = 0

        self._year = year
        self._points_year = 0

        self._used_for = used_for
        self._points_used_for = 0

        self._accidents = accidents
        self._points_accidents = 0

        self._service_frequency = service_frequency
        self._points_service_frequency = 0

        self._owner_age = owner_age
        self._points_owner_age = 0

        self._total_points = 0
        self._insurance_months = 0

    def get_mileage(self):
        return self._mileage

    def get_brand_reliability(self):
        return self._brand_reliability

    def get_year(self):
        return self._year

    def get_used_for(self):
        return self._used_for

    def get_accidents(self):
        return self._accidents

    def get_service_frequency(self):
        return self._service_frequency

    def get_owner_age(self):
        return self._owner_age

    def get_total_points(self):
        return self._total_points

    def get_insurance_months(self):
        return self._insurance_months

    def set_points_mileage(self, points_mileage):
        self._points_mileage = points_mileage

    def set_points_brand_reliability(self, points_brand_reliability):
        self._points_brand_reliability = points_brand_reliability

    def set_points_year(self, points_year):
        self._points_year = points_year

    def set_points_used_for(self, points_used_for):
        self._points_used_for = points_used_for

    def set_points_accidents(self, points_accidents):
        self._points_accidents = points_accidents

    def set_points_service_frequency(self, points_service_frequency):
        self._points_service_frequency = points_service_frequency

    def set_points_owner_age(self, points_owner_age):
        self._points_owner_age = points_owner_age

    def set_total_points(self, total_points):
        self._total_points = total_points

    def set_insurance_months(self, insurance_months):
        self._insurance_months = insurance_months

    def __str__(self):
        return "Year: " + str(self._year) + " (" + str(self._points_year) + \
               "), Used for: " + str(self._used_for) + " (" + str(self._points_used_for) + \
               "), Mileage: " + str(self._mileage) + " (" + str(self._points_mileage) + \
               "), Brand reliability: " + str(self._brand_reliability) + " (" + str(self._points_brand_reliability) + \
               "), \nAccidents: " + str(self._accidents) + " (" + str(self._points_accidents) + \
               "), \nService frequency: " + str(self._service_frequency) + " (" + str(self._points_service_frequency) + \
               "), Owner age: " + str(self._owner_age) + "(" + str(self._points_owner_age) + \
               "), Total points: " + str(self._total_points) + \
               ", \nInsurance months offered: " + str(self._insurance_months)
