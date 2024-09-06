# Initial Setup: Two questionnaires Q1 and Q2 with separate calculator methods

class Q1:
    def __init__(self, answers):
        self.answers = answers

    def calculate_score(self):
        # Example scoring logic for Q1
        score = sum(self.answers)
        return score

class Q2:
    def __init__(self, answers):
        self.answers = answers

    def calculate_score(self):
        # Example scoring logic for Q2
        score = sum(self.answers) * 2
        return score

# Example usage:
q1 = Q1([1, 2])
q2 = Q2([1, 3])
print("Q1 score:", q1.calculate_score())  # Outputs: Q1 score: 3
print("Q2 score:", q2.calculate_score())  # Outputs: Q2 score: 8
