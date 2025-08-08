class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.horsepower = horsepower

    def drive(self) -> None:
        print(f'{self.brand} is driving!')

    def get_info(self) -> None:
        print(f'{self.brand} with {self.horsepower} horsepower.')

toyota: Car = Car('Toyota', 300)
toyota.drive()
toyota.get_info()
