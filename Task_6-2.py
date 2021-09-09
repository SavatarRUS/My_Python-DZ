class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, weight=30, depth=5):
        return f"{self._length} m * {self._width} m * {weight} кг * {depth} см =" \
               f"{self._length * self._width * weight * depth}"


road_sum = Road(500, 20)
print('Result: ', road_sum.mass())
