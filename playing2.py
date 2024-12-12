class Animal:
    height_ = 0
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.height_ = 0

    def setHeight(self, height):
        self.height_ = height

    def getHeight(self):
        return self.height_
    

dog = Animal("Bella", 40)
print(dog.height_)