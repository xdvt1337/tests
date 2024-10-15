import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """
        Test for walk function in Runner.
        :return:
        """
        runner = Runner.Runner('Timur')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
    def test_run(self):
        """
        Test for run function in Runner.
        :return:
        """
        runner = Runner.Runner('Stepan')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
    def test_challenge(self):
        """
        Test in inequality of results.
        :return:
        """
        runner_1 = Runner.Runner('Fedor')
        runner_2 = Runner.Runner('Alice')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

if __name__ == '__main__':
    unittest.main()