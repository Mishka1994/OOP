class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть целым числом')
        self.seconds = seconds

    @classmethod
    def verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Операнд справа должен иметь тип int и Clock')

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.verify_data(other)
        return self.seconds < sc


c1 = Clock(1000)
c2 = Clock(2000)
print(c1 != c2)

