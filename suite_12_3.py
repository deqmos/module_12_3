import unittest
import Tournament_test, Runner_test

general_test = unittest.TestSuite()
general_test.addTest(unittest.TestLoader().loadTestsFromTestCase(Tournament_test.TournamentTest))
general_test.addTest(unittest.TestLoader().loadTestsFromTestCase(Runner_test.RunnerTest))

show_result_test = unittest.TextTestRunner(verbosity=2)
show_result_test.run(general_test)
