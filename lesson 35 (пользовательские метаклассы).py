# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0


def create_class_point(name, base, attrs):
    attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
    return type(name, base, attrs)


class Point(metaclass=create_class_point):
    def get_coords(self):
        return (0, 0)


pt = Point()

print(pt.MAX_COORD)
print(pt.get_coords())


