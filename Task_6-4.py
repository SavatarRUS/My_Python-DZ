class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print("Сбавьте скорость!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print("Сбавьте скорость!")


class PoliceCar(Car):
    pass


t_car = TownCar(61, 'red', 'name1', False)
t_car.go()
t_car.show_speed()
t_car.speed = 50
t_car.show_speed()
t_car.turn("направо")
t_car.stop()
