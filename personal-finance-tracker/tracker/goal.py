class GoalManager:
    def __init__(self):
        self.goals = []

    def set_goal(self, name, amount):
        self.goals.append({"name": name, "amount": amount})

    def get_goals(self):
        return self.goals
