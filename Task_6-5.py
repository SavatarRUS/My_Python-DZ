class Stationery:
    title = None

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('отрисовка ручкой')


class Pencil(Stationery):
    def draw(self):
        print('отрисовка карандашом')


class Handle(Stationery):
    def draw(self):
        print('отрисовка маркером')


pen = Pen()
pencil = Pencil()
handle = Handle()
