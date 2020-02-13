from unittest import TestLoader, TestSuite, TextTestRunner
from uk_smoke_test import Uk_smoke_test
from belgium_smoke_test import Belgium_smoke_test
from germany_smoke_test import Germany_smoke_test
from middle_east_smoke_test import Middle_east_smoke_test
from misc_smoke_test import MiscTests
from norway_smoke_test import Norway_smoke_test
from portugal_smoke_test import Portugal_smoke_test
from singapore_smoke_test import Singapore_smoke_test
from turkey_smoke_test import Turkey_smoke_test
from Report import HTMLTestRunner

united_kingdom = TestLoader().loadTestsFromTestCase(Uk_smoke_test)
belgium = TestLoader().loadTestsFromTestCase(Belgium_smoke_test)
germany = TestLoader().loadTestsFromTestCase(Germany_smoke_test)
middle_east = TestLoader().loadTestsFromTestCase(Middle_east_smoke_test)
misc_tests = TestLoader().loadTestsFromTestCase(MiscTests)
norway = TestLoader().loadTestsFromTestCase(Norway_smoke_test)
portugal = TestLoader().loadTestsFromTestCase(Portugal_smoke_test)
singapore = TestLoader().loadTestsFromTestCase(Singapore_smoke_test)
turkey = TestLoader().loadTestsFromTestCase(Turkey_smoke_test)

full_test_suite = TestSuite([united_kingdom,belgium,germany,middle_east,misc_tests,norway,portugal,singapore,turkey])
# individual = TestSuite([middle_east])

variable = HTMLTestRunner(title= "Report",description="CPW AUTOMATION SUITE: SMOKE TESTS",verbosity=1)
variable.run(full_test_suite)
print ("yolo")

# variable = HTMLTestRunner(title= "Report",description="CPW AUTOMATION SUITE: SMOKE TESTS",verbosity=1)
# variable.run(individual)