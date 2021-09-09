class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income.get('wage') + self._income.get('bonus'))


Mike = Position('Mike', 'Smith', 'director', 100000, 50000)
Mike.get_full_name()
Mike.get_total_income()