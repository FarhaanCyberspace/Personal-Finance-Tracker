import unittest
from tracker.goal import GoalManager

class TestGoalManager(unittest.TestCase):
    def setUp(self):
        self.manager = GoalManager()

    def test_set_goal(self):
        self.manager.set_goal("Save for Vacation", 2000)
        self.assertEqual(len(self.manager.get_goals()), 1)

if __name__ == '__main__':
    unittest.main()
