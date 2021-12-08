class SentEmail:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def summarize(self):
        return self.b + self.b


class Subtraction(SentEmail):

    def deduction(self):
        return self.a - self.b


class Multiply(SentEmail):

    def multi(self):
        return self.a * self.b

    
print("This is message for PR")
