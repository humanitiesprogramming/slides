class Coffee:
    def __init__(self, temp=0, flavor='bland'):
        self.temperature = temp
        self.flavor = flavor

    def change_temp(self, temp):
        self.temperature = temp

    def is_hot(self, temp):
        if temp > 160:
            return True
        else:
            return False

    def display_temp(self):
        print(self.temperature)


c = Coffee(90)
print(c.is_hot(170))
