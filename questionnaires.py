# Refactor the code and add Q3 in one step (one PR)

class Questionnaire:
    def __init__(self, answers):
        self.answers = answers

    def calculate_score(self):
        # Basic calculation logic can be defined here
        return sum(self.answers)


class Q1(Questionnaire):
    def calculate_score(self):
        # Override the basic calculator for Q1 if needed
        return super().calculate_score()

class Q2(Questionnaire):
    def calculate_score(self):
        # Override the basic calculator for Q2 if needed
        return super().calculate_score() * 2

# Example usage:
q1 = Q1([1, 2])
q2 = Q2([1, 3])
print("Q1 score:", q1.calculate_score())  # Outputs: Q1 score: 3
print("Q2 score:", q2.calculate_score())  # Outputs: Q2 score: 8
