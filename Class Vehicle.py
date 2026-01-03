class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX = Vehicle(240, 18)
print("Max Speed:", modelX.max_speed)
print("Mileage:", modelX.mileage)
print("Model Max Speed:", modelX.max_speed)
print("Model Mileage:", modelX.mileage)