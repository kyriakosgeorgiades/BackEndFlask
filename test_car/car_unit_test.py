import unittest
import sqlite3


# unit testing class
class TestCars(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        c = self.conn.cursor()
        cmd = ('CREATE TABLE car (car_id INT, brand TEXT, model TEXT, year	INTEGER, price INTEGER,' +
               'km_driven INTEGER, fuel_type TEXT, seller_type TEXT, transmission TEXT, owners_info TEXT,' +
               'fuel_consumption REAL, engine REAL, max_power INTEGER, torque INTEGER, seats INTEGER,' +
               'image_url TEXT, user_id INT)')
        c.execute(cmd)
        cmd = ('INSERT INTO "car" ("car_id","brand","model","year","price","km_driven","fuel_type","seller_type",'
               '"transmission","owners_info","fuel_consumption","engine","max_power","torque","seats","image_url",'
               '"user_id") VALUES ("1","Ford","Focus","2017","42995","22378","Petrol","Individual","Manual",'
               '"First Owner","59.06","2.3","345","325","5",'
               '"https://m.atcdn.co.uk/a/media/w800h600/5851b353a37d4541aa3d1c7c50a16848.jpg","1") ')
        c.execute(cmd)
        self.conn.commit()

    def test_get_all(self):
        try:
            self.conn.row_factory = sqlite3.Row
            c = self.conn.cursor()
            c.execute('SELECT * FROM car')
            cars = c.fetchone()
            self.assertTrue(cars)
            print('  test_get_all: SUCCESS. query returned: db record as object')
        except sqlite3.OperationalError:  # catch database error
            self.fail("  test_get_all: FAIL. database unable to connect")
        except AssertionError:  # catch assertion error
            self.fail("  test_get_all: FAIL. database query error")

    def test_view_car(self):
        try:
            self.conn.row_factory = sqlite3.Row
            c = self.conn.cursor()
            car_id = 1
            c.execute('SELECT * FROM car WHERE car_id = ?', (car_id,))
            cars = dict(c.fetchone())
            self.assertTrue(cars["car_id"])
            print('  test_view_car: SUCCESS. query returned: db record as accessible dictionary')
        except sqlite3.OperationalError:  # catch database error
            self.fail("  test_view_car: FAIL. database unable to connect")
        except AssertionError:  # catch assertion error
            self.fail("  test_view_car: FAIL. database query error")

    def test_find_similar(self):
        try:
            self.conn.row_factory = sqlite3.Row
            c = self.conn.cursor()
            car_id = 1
            c.execute('SELECT * FROM car WHERE car_id = ?', (car_id,))
            cars = c.fetchone()

            self.assertTrue(cars["brand"])
            self.assertTrue(int(cars["price"]))
            self.assertTrue(float(cars["engine"]))

            print('  test_find_similar stage 1: SUCCESS. query returned: db record as accessible dictionary')

            try:
                c.execute('SELECT * FROM car WHERE engine < ? AND fuel_consumption > ? AND year >= ? AND price < ? ',
                          (float(cars["engine"]), float(cars["fuel_consumption"]), int(cars["year"]) - 2,
                           int(cars["price"]) + 5000))
                print('  test_find_similar stage 2: SUCCESS. second query executed successfully')
            except sqlite3.OperationalError:  # catch database error
                self.fail("  test_find_similar stage 2: FAIL. error occurred during database query")

        except sqlite3.OperationalError:  # catch database error
            self.fail("  test_find_similar stage 1: FAIL. database unable to connect")
        except AssertionError:  # catch assertion error
            self.fail("  test_find_similar stage 1: FAIL. database query error")


if __name__ == '__main__':
    unittest.main()
