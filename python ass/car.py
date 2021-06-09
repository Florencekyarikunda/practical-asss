class Car:
    def __init__(self,color,model,registration,mileage):
        self.color=color
        self.model=model
        self.registration=registration
        self.mileage=mileage

    def start(self):
        return f"Starting to move"

    def stop(self):
        return f"stoping to move"
