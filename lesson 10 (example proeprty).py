from string import ascii_letters

class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат ФИО')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('В ФИО должен быть хотя бы один символ')
            if len(s.strip(letters)) != 0:
                raise TypeError('В ФИО можно использовать только буквенные символы и дефис')

    @classmethod
    def verify_old(cls, old):
        if isinstance(old, int) or old < 14 < 120:
            raise (TypeError('Возраст должен быть целым числом в диапазоне [14; 120]'))

    @classmethod
    def verify_weight(cls, w):
        if isinstance(w, float) or 20 < w < 120:
            raise TypeError('Вес должен быть вещественным числом от 20 и выше')

    @classmethod
    def verify_ps(cls, ps):
        if isinstance(ps, str):
            raise TypeError('Паспорт должен быть строкой')

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неверный формат паспорта')

        for num in s:
            if not num.is_digit():
                raise TypeError('Серия и номер паспорта должны быть числами')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

        