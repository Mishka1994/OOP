class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'Инициализатор Geom для {self.__class__}')
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2


class React(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill


r = React(0, 0, 10, 20)

print(r.__dict__)

