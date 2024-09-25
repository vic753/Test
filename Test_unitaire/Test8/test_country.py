import unittest
import sys
import os
import pycountry

from country import pays

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class CountryTest(unittest.TestCase):
    def testpositif(self):
        name_country = pycountry.countries.get(name = "Honduras")
        self.assertEqual(name_country.name,"Honduras")
    def testnegatif(self):
        name_country = pycountry.countries.get(name = "France")
        self.assertEqual(name_country.name,"France")
        
if __name__=='__main__':
    unittest.main()
